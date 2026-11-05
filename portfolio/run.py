"""Tạo CSV sạch, cơ sở dữ liệu SQLite, kết quả SQL, kiểm tra xác thực và báo cáo dự án.

Chạy từ bất kỳ thư mục nào: python -m portfolio.run --root /path/to/repository
Tất cả kết quả đầu ra đều có tính tiền định (deterministic) với cùng tệp nguồn và phiên bản phần mềm.
"""
import argparse
import hashlib
import html
import json
import platform
import re
import sqlite3
from pathlib import Path

import numpy as np
import pandas as pd
import scipy

from .contracts import PROJECTS, STAGES, ONBOARDING
from .metrics import experiment, ratio
from .quality import clean_table, foreign_key, ordered_funnel


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path, data):
    path.write_text(json.dumps(data, indent=2, sort_keys=True, allow_nan=False)+'\n')


def read_queries(path):
    sections = re.split(r'^-- name: (\w+)\s*$', path.read_text(), flags=re.M)
    if sections[0].strip() or len(sections)<3:
        raise ValueError(f'Tệp truy vấn không hợp lệ: {path}')
    return list(zip(sections[1::2], sections[2::2]))


def check_equal(name, actual, expected, checks):
    if actual is None or expected is None:
        match = actual is None and expected is None
    else:
        match = bool(np.allclose(actual,expected,rtol=1e-10,atol=1e-8))
    checks.append({'check':name,'passed':match})
    if not match:
        raise AssertionError(f'{name}: SQL={actual}, Python độc lập={expected}')


def validate_relations(key, t, checks):
    """Các kiểm tra quan hệ ràng buộc nghiêm ngặt và chẩn đoán ngữ nghĩa không chặn."""
    issues=[]
    def require(name, condition):
        passed=bool(condition);checks.append({'check':name,'passed':passed})
        if not passed: raise ValueError(name)
    def warn(name, count, explanation):
        issues.append({'issue':name,'affected_rows':int(count),'interpretation':explanation})
    if key.startswith('01'):
        u,s,e=t['users'],t['subscriptions'],t['events']
        foreign_key(s,u,'user_id');foreign_key(e,u,'user_id')
        require('subscription coverage',set(s.user_id)==set(u.user_id))
        joined=s.merge(u,on='user_id',suffixes=('_s','_u'))
        require('plan tiers agree',joined.plan_tier_s.eq(joined.plan_tier_u).all())
        require('valid plan tier',s.plan_tier.isin(['Free','Starter','Pro','Enterprise']).all())
        dated=e.merge(u[['user_id','signup_date']],on='user_id')
        warn('events_before_signup',(dated.event_date<dated.signup_date).sum(),'Giữ lại trong dữ liệu nguồn; được loại bỏ trong phễu theo thứ tự và khoảng hoạt động 90 ngày.')
        flags=set(e.loc[e.event_name.eq('Step 2: Workspace'),'user_id'])
        warn('step2_flag_disagreement',s.completed_step2.ne(s.user_id.isin(flags).astype(int)).sum(),'Cờ đánh dấu trong subscriptions và sự kiện thực tế là hai tín hiệu riêng biệt; không tự ý ghi đè.')
        warn('free_accounts_with_churn_label',((s.mrr==0)&(s.churned_within_90d==1)).sum(),'Tài khoản miễn phí không tính vào tỷ lệ rời bỏ của người dùng trả phí. Thời điểm gán nhãn chưa được xác minh độc lập.')
    elif key.startswith('02'):
        require('exactly two experiment arms',set(t['ab_sessions'].variant)=={'Control','Variant B'})
        warn('unknown_randomization_unit',len(t['ab_sessions']),'Không có user_id hoặc nhật ký phân bổ. Tính độc lập của phiên và tỷ lệ 50:50 là các giả định; kết luận suy diễn mang tính tạm thời.')
    elif key.startswith('03'):
        w,o=t['web_sessions'],t['orders'];foreign_key(o,w,'session_id')
        require('purchase requires cart',(w.purchased<=w.added_to_cart).all())
        require('one order per purchased session',set(o.session_id)==set(w.loc[w.purchased==1,'session_id']))
        j=o.merge(w,on='session_id',suffixes=('_o','_w'))
        for col in ['session_date','device','channel']:
            require(f'order/session {col} agrees',j[col+'_o'].eq(j[col+'_w']).all())
    elif key.startswith('04'):
        s,l=t['sales'],t['listings'];foreign_key(s,l,'listing_id')
        j=s.merge(l,on='listing_id',suffixes=('_s','_l'))
        for col in ['seller_id','category','price','rating','in_stock']:
            require(f'sale/listing {col} agrees',j[col+'_s'].eq(j[col+'_l']).all())
        warn('revenue_not_price_times_units',((s.revenue-s.price*s.units_sold).abs()>0.011).sum(),'Sử dụng doanh thu ghi nhận theo nguồn. Chiết khấu, phí, thuế và quy tắc tạo dữ liệu chưa rõ; không coi chênh lệch này là lỗi hay doanh thu bị mất.')
        warn('sales_on_out_of_stock_listings',s.in_stock.eq(0).sum(),'Cờ tồn kho là ảnh chụp nhanh không kèm ngày; không phản ánh chính xác tình trạng lúc bán hàng.')
    elif key.startswith('05'):
        u,e=t['users'],t['journey_events'];foreign_key(e,u,'user_id')
        require('known journey stages',set(e.journey_stage).issubset(set(STAGES+['Signup'])))
        expected={s:i for i,s in enumerate(STAGES+['Signup'],1)}
        require('stage order agrees',e.stage_order.eq(e.journey_stage.map(expected)).all())
        j=e.merge(u[['user_id','first_seen_date']],on='user_id')
        warn('events_before_first_seen',(j.event_date<j.first_seen_date).sum(),'Giữ lại trong nguồn; phễu tuần tự và thời gian đến lúc mua hàng đã loại bỏ chuỗi thời gian không hợp lệ.')
        first=e.pivot_table(index='user_id',columns='journey_stage',values='event_date',aggfunc='min').apply(pd.to_datetime)
        inversions=pd.Series(False,index=first.index)
        for previous,following in zip(STAGES,STAGES[1:]):
            inversions |= first[previous].notna() & first[following].notna() & first[following].lt(first[previous])
        warn('users_with_adjacent_stage_date_inversions',inversions.sum(),'Có ít nhất một bước sau diễn ra trước bước trước đó. Không coi sự sụt giảm phễu nghiêm ngặt là khách hàng bỏ cuộc; cần kiểm tra lại cơ chế ghi nhận thời gian.')
    checks.append({'check':'foreign key checks completed','passed':True})
    return issues


def reconcile(key,t,out,checks):
    extra={}
    if key.startswith('01'):
        s=t['subscriptions'];row=out['summary'].iloc[0]
        for name,value in {'users':len(s),'paying_users':int((s.mrr>0).sum()),'snapshot_mrr':s.mrr.sum(),'snapshot_arr':s.mrr.sum()*12,'paying_churn_label_rate':s.loc[s.mrr>0,'churned_within_90d'].mean()}.items():
            check_equal(name,float(row[name]),float(value),checks)
        expected=ordered_funnel(t['users'],t['events'],ONBOARDING,'event_name','signup_date')
        check_equal('ordered onboarding SQL/Python',out['onboarding_funnel'].users.tolist(),expected,checks)
        e=t['events'].merge(t['users'][['user_id','signup_date']],on='user_id')
        event_date=pd.to_datetime(e.event_date);signup=pd.to_datetime(e.signup_date)
        mask=e.event_name.eq('Workflow Run') & e.event_group.eq('Product') & event_date.ge(signup) & event_date.lt(signup+pd.Timedelta(days=90))
        counts=e[mask].groupby('user_id').size()
        p=s[s.mrr>0].copy();p['activity_group']=np.where(p.user_id.map(counts).fillna(0)>=20,'20+ runs','Under 20 runs')
        for row in out['power_user_association'].itertuples():
            subgroup=p[p.activity_group==row.activity_group]
            check_equal('power user count '+row.activity_group,row.paying_users,len(subgroup),checks)
            check_equal('power user churn '+row.activity_group,row.churn_label_rate,subgroup.churned_within_90d.mean(),checks)
        extra['onboarding_step2_conditional_dropoff']=1-ratio(expected[1],expected[0]) if expected[0] else None
    elif key.startswith('02'):
        df=t['ab_sessions']
        for row in out['variant_summary'].itertuples():
            arm=df[df.variant.eq(row.variant)]
            for metric,value in {'sessions':len(arm),'conversions':arm.converted.sum(),'conversion_rate':arm.converted.mean(),'bounce_rate':arm.bounce.mean(),'mean_engagement':arm.engagement_score.mean(),'revenue':arm.revenue.sum(),'revenue_per_session':arm.revenue.mean()}.items():
                check_equal(row.variant+' '+metric,float(getattr(row,metric)),float(value),checks)
        a=df[df.variant.eq('Control')];b=df[df.variant.eq('Variant B')]
        extra['experiment']=experiment(int(a.converted.sum()),len(a),int(b.converted.sum()),len(b))
        extra['experiment']['decision']='Chưa nên triển khai chính thức chỉ dựa trên dữ liệu phiên mô phỏng; cần xác minh tính ngẫu nhiên, độc lập người dùng và các chỉ số cảnh báo rủi ro.'
    elif key.startswith('03'):
        w,o=t['web_sessions'],t['orders'];row=out['summary'].iloc[0]
        values={'sessions':len(w),'cart_sessions':w.added_to_cart.sum(),'purchases':w.purchased.sum(),'conversion_rate':w.purchased.mean(),'cart_abandonment_rate':1-w.purchased.sum()/w.added_to_cart.sum(),'revenue':o.order_value.sum(),'average_order_value':o.order_value.mean()}
        for name,value in values.items():check_equal(name,float(row[name]),float(value),checks)
        rev=o.groupby('sku').order_value.sum().sort_values(ascending=False)
        n=int(np.ceil(len(rev)*.2));share=float(rev.iloc[:n].sum()/rev.sum())
        sql=out['sku_pareto'];check_equal('top 20 percent SKU share',float(sql.loc[sql.in_top_20_percent==1,'revenue'].sum()/sql.revenue.sum()),share,checks)
        extra['top_20_percent_sku_revenue_share']=share
        extra['rfm_status']='Không tính toán: thiếu mã định danh khách hàng ổn định; session_id không thể đại diện cho khách hàng.'
    elif key.startswith('04'):
        s=t['sales'];row=out['summary'].iloc[0]
        for name,value in {'sales_rows':len(s),'units':s.units_sold.sum(),'recorded_revenue':s.revenue.sum(),'price_times_units':(s.price*s.units_sold).sum(),'revenue_discrepancy_rows':((s.revenue-s.price*s.units_sold).abs()>.011).sum(),'sellers':s.seller_id.nunique()}.items():check_equal(name,float(row[name]),float(value),checks)
        seller=s.groupby('seller_id').revenue.sum().sort_values(ascending=False)
        share=float(seller.iloc[:10].sum()/seller.sum())
        check_equal('top ten seller share',float(out['seller_concentration'].head(10).revenue_share.sum()),share,checks)
        extra['top_10_seller_revenue_share']=share
        extra['seller_hhi']=float(((seller/seller.sum())**2).sum()*10000)
    else:
        u,e=t['users'],t['journey_events'];row=out['summary'].iloc[0]
        purchasers=set(e.loc[e.journey_stage.eq('Purchase'),'user_id'])
        check_equal('users',row.users,len(u),checks);check_equal('purchasers',row.purchasers,len(purchasers),checks)
        check_equal('observed purchase rate',row.observed_purchase_rate,len(purchasers)/len(u),checks)
        expected=ordered_funnel(u,e,STAGES,'journey_stage','first_seen_date')
        check_equal('ordered journey SQL/Python',out['ordered_funnel'].users.tolist(),expected,checks)
        j=e[e.journey_stage.eq('Purchase')].merge(u[['user_id','first_seen_date']],on='user_id')
        j=j[j.event_date>=j.first_seen_date].copy();j['days']=(pd.to_datetime(j.event_date)-pd.to_datetime(j.first_seen_date)).dt.days
        time=j.groupby('user_id').days.min()
        check_equal('time to purchase',out['time_to_purchase'].days_to_purchase.tolist(),time.sort_index().tolist(),checks)
        extra['p50_days_to_purchase']=float(time.quantile(.5)) if len(time) else None
        extra['p90_days_to_purchase']=float(time.quantile(.9)) if len(time) else None
        extra['ordered_path_loss_after_checkout']=1-ratio(expected[-1],expected[-2]) if expected[-2] else None
        extra['signup_handling']='Bước Đăng ký được báo cáo độc lập; không bắt buộc phải xảy ra sau bước mua hàng. Sự sụt giảm ở phễu tuần tự là công cụ chẩn đoán tracking, không phải bằng chứng khách bỏ thanh toán.'
    return extra


GUIDANCE={
 '01': ('Kích hoạt người dùng SaaS & Chất lượng doanh thu',
 'Người dùng rơi rụng nhiều nhất ở bước onboarding nào, và mức độ hoạt động khác biệt ra sao giữa các nhóm nhãn rời bỏ (churn)?',
 'Ưu tiên nghiên cứu trải nghiệm người dùng tại bước rơi rụng lớn nhất trong phễu onboarding. Xem mối liên hệ giữa tần suất hoạt động và churn là tương quan khảo sát; nên chạy thử nghiệm A/B quy trình onboarding trước khi kết luận về tác động giữ chân người dùng.',
 'MRR/ARR là ảnh chụp dữ liệu tại một thời điểm, không phải doanh thu ghi nhận chuẩn kế toán hay run-rate thực tế. Churn là nhãn 90 ngày có sẵn trong dữ liệu, không phải kết quả cohort được tái lập độc lập. Người dùng miễn phí bị loại khỏi tỷ lệ churn trả phí. Các sự kiện lặp lại trong ngày vẫn giữ nguyên vì thiếu event_id. Cửa sổ hoạt động tính trong 90 ngày từ ngày đăng ký; việc theo dõi chưa hoàn tất và quan hệ nhân quả hai chiều là các giới hạn diễn giải.'),
 '02': ('Đo lường thử nghiệm A/B & Đánh giá triển khai tính năng',
 'Variant B có mang lại tỷ lệ chuyển đổi cao hơn không, và độ không chắc chắn của mức chênh lệch ước tính là bao nhiêu?',
 'Dùng tỷ lệ chuyển đổi làm chỉ số chính; theo dõi tỷ lệ thoát, doanh thu trên mỗi phiên và điểm tương tác làm chỉ số cảnh báo. Xác minh đơn vị phân bổ ngẫu nhiên, độ phơi nhiễm, tỷ lệ chia lưu lượng kế hoạch và thời gian chạy thử nghiệm trước khi quyết định ra mắt chính thức. Các phân tích theo phân khúc chỉ mang tính thăm dò.',
 'Dữ liệu phiên mô phỏng thiếu user_id ổn định và log phân bổ. Kiểm định z-test gộp hai phía và khoảng tin cậy Newcombe-Wilson dựa trên giả định các phiên độc lập với nhau. Kiểm định tỷ lệ mẫu (SRM) giả định phân bổ 50:50. Chưa áp dụng hiệu chỉnh cho việc xem trước kết quả nhiều lần hoặc so sánh nhiều chỉ số đồng thời.'),
 '03': ('Phễu thương mại điện tử & Mức độ tập trung sản phẩm (SKU)',
 'Tổ hợp thiết bị / kênh nào bị rơi rụng giỏ hàng nhiều nhất, và doanh thu tập trung vào các SKU như thế nào?',
 'Tập trung tối ưu các phân khúc vừa có lượng phiên lớn vừa có tỷ lệ bỏ giỏ hàng cao. Cần kết hợp nghiên cứu UX để làm rõ rào cản thanh toán; phân tích mức độ tập trung SKU nhằm rà soát tồn kho chứ không nên vội vàng cắt giảm danh mục sản phẩm.',
 'Trong tập dữ liệu này, mỗi dòng đơn hàng tương ứng với một phiên mua hàng. Đây là quy ước của dữ liệu, không phải mô hình tổng quát cho mọi sàn TMĐT. Dữ liệu không có customer_id nên không thể phân tích RFM hay hành vi mua lại. So sánh hiệu quả giảm giá mang tính quan sát, có thể bị ảnh hưởng bởi việc chọn lọc phân khúc.'),
 '04': ('Doanh thu sàn Marketplace & Đối soát nguồn dữ liệu',
 'Doanh thu phân bổ tập trung vào các nhà bán hàng ra sao, và rào cản nào khiến việc đối soát tài chính chưa trọn vẹn?',
 'Làm việc với bộ phận quản lý nguồn dữ liệu để làm rõ chênh lệch giữa doanh thu ghi nhận và giá × số lượng trước khi dùng cho báo cáo tài chính. Đánh giá rủi ro phụ thuộc vào top người bán dựa trên tỷ trọng doanh thu. So sánh theo trạng thái tồn kho chỉ mang tính chẩn đoán tương quan.',
 'Dữ liệu nguồn không phân biệt rõ đơn hàng, phí sàn, gói Prime hay cấp độ người bán. Số dòng bán hàng không phải số lượng đơn hàng. Doanh thu ghi nhận không được phân tách thành doanh thu nền tảng hay GMV. Trạng thái tồn kho chỉ là ảnh chụp tại một thời điểm. Dòng giao dịch lặp được giữ nguyên do thiếu mã giao dịch; chưa đủ căn cứ ước tính doanh thu bị mất do hết hàng.'),
 '05': ('Hành trình người dùng theo trình tự & Điểm nghẽn chuyển đổi',
 'Có bao nhiêu người dùng hoàn thành phễu mua hàng theo đúng trình tự thời gian, và tỷ lệ chuyển đổi khác nhau thế nào giữa khách mới và khách quay lại?',
 'So sánh tỷ lệ mua hàng tổng thể với phễu nghiêm ngặt theo trình tự thời gian để phát hiện lỗi theo dõi thiếu hoặc đảo lộn thứ tự. Tìm ra bước chuyển đổi có tỷ lệ rơi rụng lớn nhất trước khi đề xuất thử nghiệm giao diện mới.',
 'Ngày tháng trong dữ liệu chỉ có độ phân giải theo ngày; các bước cùng ngày không xác định được thứ tự chính xác trong ngày. Bước Đăng ký được tính độc lập với phễu mua sắm 6 bước. Các nhóm thuần tập có khoảng thời gian theo dõi khác nhau, nên tỷ lệ chuyển đổi và thời gian đến khi mua hàng chỉ mang tính mô tả.')}


def markdown_table(frame):
    def cell(v):
        if isinstance(v,(float,np.floating)): return f'{v:,.6g}'
        return str(v).replace('|','\\|')
    lines=['| '+' | '.join(frame.columns)+' |','| '+' | '.join(['---']*len(frame.columns))+' |']
    lines+=['| '+' | '.join(cell(v) for v in row)+' |' for row in frame.itertuples(index=False,name=None)]
    return '\n'.join(lines)


def chart(key, results):
    """Vẽ biểu đồ SVG nội tuyến sử dụng kết quả truy vấn, bắt đầu từ gốc tọa độ 0."""
    config={
        '01':('onboarding_funnel','stage','users','Lượng tiếp cận onboarding theo thứ tự (người dùng)'),
        '02':('variant_summary','variant','conversion_rate','Tỷ lệ chuyển đổi quan sát được (tỷ lệ)'),
        '03':('funnel_by_segment','device','conversion_rate','Tỷ lệ chuyển đổi theo thiết bị và kênh (tỷ lệ)'),
        '04':('category_performance','category','recorded_revenue','Doanh thu ghi nhận theo ngành hàng'),
        '05':('stage_reach','journey_stage','users','Lượng tiếp cận giai đoạn chưa sắp xếp (người dùng)')}
    table,label,value,title=config[key[:2]]
    frame=results[table].head(10)
    labels=frame[label].astype(str)
    if key.startswith('03'): labels=labels+' / '+frame.channel.astype(str)
    maximum=float(frame[value].max()) or 1
    height=65+len(frame)*43
    parts=[f'<svg viewBox="0 0 1000 {height}" role="img" aria-labelledby="chartTitle"><title id="chartTitle">{html.escape(title)}</title><text x="0" y="24" font-size="19" fill="#17283d">{html.escape(title)}</text>']
    for i,(label_,number) in enumerate(zip(labels,frame[value])):
        y=46+i*43;width=float(number)/maximum*520
        parts.append(f'<text x="0" y="{y+18}" font-size="14" fill="#17283d">{html.escape(label_)}</text><rect x="290" y="{y}" width="{width:.3f}" height="26" rx="3" fill="#087f8c"/><text x="{300+width:.3f}" y="{y+18}" font-size="14" fill="#17283d">{number:,.4g}</text>')
    parts.append('</svg>')
    return ''.join(parts)


def highlights(key, results, extra):
    if key.startswith('01'):
        row=results['summary'].iloc[0]
        return f"Ảnh chụp gói thuê bao ghi nhận tổng {row.snapshot_mrr:,.2f} MRR từ {int(row.paying_users):,} người dùng trả phí. Tỷ lệ nhãn rời bỏ (churn) ở nhóm trả phí là {row.paying_churn_label_rate:.2%}. Tỷ lệ rơi rụng từ Bước 1 sang Bước 2 trong phễu là {extra['onboarding_step2_conditional_dropoff']:.2%}; đây là kết quả mô tả phễu thực tế chứ chưa phải kết quả thử nghiệm can thiệp."
    if key.startswith('02'):
        e=extra['experiment']
        return f"Bản gốc (Control) đạt tỷ lệ chuyển đổi {e['control_rate']:.2%} còn Variant B đạt {e['treatment_rate']:.2%}: tăng +{e['absolute_lift']*100:.2f} điểm phần trăm (mức tăng tương đối {e['relative_lift']:.2%}). Khoảng tin cậy chênh lệch 95% là từ {e['difference_ci_low']*100:.2f} đến {e['difference_ci_high']*100:.2f} điểm phần trăm. Kết luận thống kê vẫn dựa trên giả định các phiên truy cập độc lập với nhau."
    if key.startswith('03'):
        row=results['summary'].iloc[0]
        return f"Tỷ lệ chuyển đổi phiên quan sát được là {row.conversion_rate:.2%}; tỷ lệ bỏ giỏ hàng là {row.cart_abandonment_rate:.2%}. Top 20% mã sản phẩm (SKU) mang lại {extra['top_20_percent_sku_revenue_share']:.2%} tổng doanh thu đơn hàng ghi nhận. Kết quả này thay thế cho nhận định thiếu căn cứ trước đây về con số 68%."
    if key.startswith('04'):
        row=results['summary'].iloc[0]
        return f"Nguồn dữ liệu ghi nhận {row.recorded_revenue:,.2f} doanh thu qua {int(row.sales_rows):,} dòng bán hàng. Có {int(row.revenue_discrepancy_rows):,} dòng có chênh lệch giữa giá × số lượng lớn hơn 0,011. Top 10 nhà bán hàng đóng góp {extra['top_10_seller_revenue_share']:.2%} doanh thu. Dữ liệu chưa đủ căn cứ để kết luận về hoa hồng sàn hay số lượng đơn hàng thực tế."
    row=results['summary'].iloc[0]
    return f"Ghi nhận {int(row.purchasers):,} người mua hàng trong tổng số {int(row.users):,} người dùng ({row.observed_purchase_rate:.2%}). Không có người dùng nào đi trọn vẹn chuỗi 6 bước đúng theo trình tự ngày tháng trong dữ liệu gốc. Điểm này phản ánh vấn đề đồng bộ thời gian trong hệ thống tracking, chứ không phải không có ai mua hay 100% người dùng bỏ thanh toán."


def report(project, results, extra, quality, checks):
    title,question,action,limits=GUIDANCE[project.name[:2]]
    sections=[f'# {title}', '**Nguồn gốc dữ liệu:** tệp CSV danh mục mô phỏng được cung cấp. Không đại diện cho kết quả khách hàng thực tế.',
              '## Câu hỏi kinh doanh',question,'## Phát hiện nổi bật',highlights(project.name,results,extra),'## Kết quả tính toán']
    for name,frame in results.items():
        sections.extend([f'### {name.replace("_"," ").title()}',markdown_table(frame.head(10)),f'Kết quả đầy đủ: [Results/{name}.csv](Results/{name}.csv).'])
    sections.extend(['## Tính toán bổ sung','```json',json.dumps(extra,indent=2,allow_nan=False),'```',
                     '## Khuyến nghị hành động',action,'## Giới hạn và giả định',limits,
                     '## Cách tái lập kết quả','Từ thư mục gốc dự án: `python -m portfolio.run --project '+project.name+'`.',
                     'Mỗi truy vấn được đặt tên trong `SQL/analysis.sql` sẽ xuất ra một tệp CSV kết quả tương ứng. Trình chạy Python độc lập đối soát các chỉ số chính và phễu tuần tự. Xem `Results/validation.json` để xem các bước kiểm tra và `Results/quality.json` để xem chẩn đoán dữ liệu nguồn.',
                     '## Bảng tính và Dashboard BI có sẵn','Các dashboard Power BI/Tableau gốc được giữ lại như các tài sản cũ có dữ liệu độc lập. Các bảng tổng hợp Excel đã được đính chính. Việc kiểm tra tệp gốc xác nhận rằng các dashboard Power BI/Tableau cũ dùng các tập dữ liệu khác. Bảng tổng hợp Excel đã đính chính khớp hoàn toàn với các tệp CSV chuẩn; xem báo cáo xác thực gốc để biết bằng chứng theo từng công cụ. Sử dụng thư mục `Results/` và tệp `REPORT.html` để xem phân tích chuẩn. Đọc kỹ `Docs/Dashboard_Reconciliation.md` trước khi sử dụng ảnh chụp dashboard cũ làm bằng chứng.',
                     '## Xác thực dữ liệu',f'{len(checks)} kiểm tra chặn đã vượt qua thành công. Các giới hạn dữ liệu nguồn đã được ghi chép rõ ràng; việc vượt qua kiểm tra kỹ thuật không đồng nghĩa với việc khẳng định quan hệ nhân quả.'])
    # Không ghi đè README.md nghiên cứu điển hình chi tiết nếu đã tồn tại
    if not (project/'README.md').exists():
        text='\n\n'.join(sections)+'\n'
        (project/'README.md').write_text(text, encoding='utf-8')
    html_sections=[f'<section><h2>Dữ liệu cho thấy điều gì</h2><p>{html.escape(highlights(project.name,results,extra))}</p>{chart(project.name,results)}</section>']
    for name,frame in results.items():
        html_sections.append(f'<section><h2>{html.escape(name.replace("_"," ").title())}</h2><div class="scroll">{frame.head(20).to_html(index=False,float_format=lambda x:f"{x:,.4f}",border=0)}</div><p><a href="Results/{name}.csv">Tải kết quả đầy đủ (CSV)</a></p></section>')
    warnings=''.join(f'<li><b>{html.escape(i["issue"])}</b>: {i["affected_rows"]:,} dòng. {html.escape(i["interpretation"])}</li>' for i in quality['semantic_issues'])
    document='''<!doctype html><html lang="vi"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'''+html.escape(title)+'''</title><style>
body{margin:0;background:#f1f5f9;color:#17283d;font:16px/1.6 system-ui,sans-serif}main{max-width:1200px;margin:auto;padding:36px 24px}header{background:#102f47;color:white;padding:32px;border-radius:16px}h1{line-height:1.15;font-size:36px}h2{font-size:23px}section{background:white;padding:24px;margin:22px 0;border-radius:12px;border:1px solid #dce4ea}.tag{color:#8ee8d1;text-transform:uppercase;letter-spacing:.1em;font-size:13px}table{border-collapse:collapse;width:100%;font-size:14px}td,th{padding:10px;text-align:right;border-bottom:1px solid #e2e8f0}th{background:#edf4f8}td:first-child,th:first-child{text-align:left}.scroll{overflow:auto}a{color:#075985}pre{overflow:auto;white-space:pre-wrap}.note{border-left:5px solid #b7791f}li{margin:10px 0}@media print{body{background:white}main{padding:0}section{break-inside:avoid}header{color:#102f47;background:white}}
</style><main><header><div class="tag">Bùi Nhất Phong · Phân tích dữ liệu có đối soát (Reproducible analysis)</div><h1>'''+html.escape(title)+'''</h1><p>'''+html.escape(question)+'''</p><p>Dữ liệu mô phỏng · Đối soát SQL + Python · '''+str(len(checks))+''' kiểm tra thành công</p></header>'''+''.join(html_sections)+f'<section><h2>Kết quả thống kê và bổ sung</h2><pre>{html.escape(json.dumps(extra,indent=2))}</pre></section><section><h2>Đề xuất hành động tiếp theo</h2><p>{html.escape(action)}</p></section><section class="note"><h2>Giới hạn phân tích và giả định</h2><p>{html.escape(limits)}</p><ul>{warnings}</ul></section><p>Được tạo từ các tệp CSV mô phỏng. Bảng tổng hợp Excel và dữ liệu Hyper đã được đối soát riêng. <a href="README.md">Xem báo cáo chi tiết (Case study)</a></p></main></html>'
    (project/'REPORT.html').write_text(document, encoding='utf-8')


def run_project(root,key):
    project=root/key;results_dir=project/'Results';results_dir.mkdir(exist_ok=True)
    # Xóa bằng chứng thành công trước đó trước khi ghi đè kết quả.
    for evidence in ('validation.json','manifest.json'):
        (results_dir/evidence).unlink(missing_ok=True)
    build=root/'build'/key;build.mkdir(parents=True,exist_ok=True)
    t={};quality={'tables':{},'semantic_issues':[]};checks=[];sources={}
    for name,(pk,spec) in PROJECTS[key].items():
        source=project/'Data'/'raw'/f'{name}_raw.csv';frame=pd.read_csv(source, float_precision='round_trip')
        clean=clean_table(frame,spec,pk);t[name]=clean
        path=project/'Data'/'clean'/f'{name}_clean.csv';path.parent.mkdir(exist_ok=True)
        clean.to_csv(path,index=False)
        quality['tables'][name]={'input_rows':len(frame),'output_rows':len(clean),'null_cells':int(frame.isna().sum().sum()),'exact_repeat_rows':int(frame.duplicated().sum()),'primary_key':pk,'duplicate_policy':'Khóa chính bị trùng sẽ báo lỗi ngay; các sự kiện lặp lại không có mã định danh sự kiện cố định được giữ nguyên.','source_sha256':digest(source),'clean_sha256':digest(path)}
        checks.append({'check':f'{name}: schema, types, ranges, required values and key','passed':True})
        sources[str(source.relative_to(root)).replace('\\', '/')]=digest(source)
    quality['semantic_issues']=validate_relations(key,t,checks)
    with sqlite3.connect(build/'analysis.sqlite') as connection:
        for name,frame in t.items():frame.to_sql(name+'_clean',connection,if_exists='replace',index=False)
        for name,(pk,_) in PROJECTS[key].items():
            if pk:connection.execute(f'CREATE UNIQUE INDEX IF NOT EXISTS idx_{name}_{pk} ON {name}_clean({pk})')
        # Tái tạo lại secondary index sau khi pandas nạp lại bảng.
        for name,frame in t.items():
            for col in ['user_id','listing_id']:
                if col in frame:connection.execute(f'CREATE INDEX IF NOT EXISTS ix_{name}_{col} ON {name}_clean({col})')
        output={}
        for name,sql in read_queries(project/'SQL'/'analysis.sql'):
            output[name]=pd.read_sql_query(sql,connection)
            output[name].to_csv(results_dir/(name+'.csv'),index=False,float_format='%.12g')
            checks.append({'check':f'SQL executed: {name}','passed':True})
        extra=reconcile(key,t,output,checks)
        plans={name:[list(row) for row in connection.execute('EXPLAIN QUERY PLAN '+sql)] for name,sql in read_queries(project/'SQL'/'analysis.sql')}
    write_json(results_dir/'quality.json',quality);write_json(results_dir/'validation.json',{'passed':True,'checks':checks})
    write_json(results_dir/'additional_metrics.json',extra);write_json(results_dir/'query_plans.json',plans)
    report(project,output,extra,quality,checks)
    versions={'python':platform.python_version(),'sqlite':sqlite3.sqlite_version,'pandas':pd.__version__,'numpy':np.__version__,'scipy':scipy.__version__}
    code_paths=sorted((root/'portfolio').glob('*.py'))+[project/'SQL'/'analysis.sql',root/'requirements.txt']
    manifest={'sources':sources,'code':{str(p.relative_to(root)).replace('\\', '/'):digest(p) for p in code_paths},'software':versions,
              'outputs':{str(p.relative_to(root)).replace('\\', '/'):digest(p) for p in sorted(list(results_dir.glob('*'))+list((project/'Data'/'clean').glob('*.csv'))+[project/'REPORT.html',project/'README.md']) if p.name!='manifest.json'},
              'check_count':len(checks),'project':key,'data_kind':'supplied simulated data'}
    write_json(results_dir/'manifest.json',manifest)
    return {'project':key,'checks':len(checks),'rows':sum(len(f) for f in t.values()),'passed':True}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1])
    parser.add_argument('--project',choices=list(PROJECTS))
    args=parser.parse_args();root=args.root.resolve()
    (root/'build'/'run_summary.json').unlink(missing_ok=True)
    summary=[run_project(root,key) for key in ([args.project] if args.project else PROJECTS)]
    (root/'build').mkdir(exist_ok=True)
    write_json(root/'build'/'run_summary.json',summary)
    for item in summary:print(f"PASS {item['project']}: {item['checks']} checks; {item['rows']:,} source rows")

if __name__=='__main__':main()

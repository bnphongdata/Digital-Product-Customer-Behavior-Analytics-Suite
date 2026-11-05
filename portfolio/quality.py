"""Ngắt xử lý ngay khi vi phạm ràng buộc dữ liệu (fail-closed); giữ lại các sự kiện lặp hợp lệ."""
import numpy as np
import pandas as pd


def clean_table(frame, specification, primary_key=None):
    expected = dict(token.split(':') for token in specification.split())
    if set(frame.columns) != set(expected):
        raise ValueError(f'Schema không khớp: kỳ vọng {list(expected)}, nhận được {list(frame.columns)}')
    if frame.isna().any().any():
        raise ValueError('Thiếu giá trị bắt buộc; cần sửa nguồn hoặc cập nhật quy ước xử lý dữ liệu')
    clean = frame.copy()
    for column, kind in expected.items():
        if kind == 's':
            clean[column] = clean[column].astype(str).str.strip()
            if clean[column].eq('').any():
                raise ValueError(f'Chuỗi rỗng: {column}')
        elif kind == 'd':
            clean[column] = pd.to_datetime(clean[column], format='%Y-%m-%d', errors='raise').dt.strftime('%Y-%m-%d')
        elif kind == 'b':
            values = clean[column].astype(str).str.lower().str.strip().map({'true':1,'false':0,'1':1,'0':0})
            if values.isna().any():
                raise ValueError(f'Giá trị nhị phân không hợp lệ: {column}')
            clean[column] = values.astype('int64')
        else:
            values = pd.to_numeric(clean[column], errors='raise')
            if not np.isfinite(values).all():
                raise ValueError(f'Giá trị số không hữu hạn: {column}')
            if kind == 'i' and not (values % 1 == 0).all():
                raise ValueError(f'Không phải số nguyên: {column}')
            if (values < 0).any():
                raise ValueError(f'Số âm nằm ngoài quy ước: {column}')
            clean[column] = values.astype('int64' if kind == 'i' else 'float64')
    if primary_key and clean[primary_key].duplicated().any():
        raise ValueError(f'Trùng lặp khóa chính: {primary_key}')
    if 'rating' in clean and not clean.rating.between(0,5).all():
        raise ValueError('Điểm đánh giá (rating) nằm ngoài khoảng 0–5')
    for column in [c for c in clean if c.endswith('_id') or c in ('seats','units','units_sold')]:
        if (clean[column] <= 0).any():
            raise ValueError(f'ID hoặc số đếm không dương: {column}')
    return clean


def foreign_key(child, parent, key):
    missing = set(child[key]) - set(parent[key])
    if missing:
        raise ValueError(f'Khóa ngoại mồ côi (Orphan {key}): {len(missing)} giá trị không tồn tại ở bảng cha')


def ordered_funnel(users, events, stages, event_column, start_column=None):
    """Phễu tích lũy theo từng người dùng duy nhất; chấp nhận trùng ngày ở độ phân giải ngày.

    Lấy sự kiện thỏa điều kiện sớm nhất tại hoặc sau bước trước đó, chứ không chỉ lấy
    sự kiện sớm nhất của nhãn đó. Chưa hiệu chỉnh giới hạn quan sát (censoring).
    """
    current = {int(row.user_id): getattr(row,start_column) if start_column else '0001-01-01'
               for row in users.itertuples()}
    results = []
    for stage in stages:
        matching = events[events[event_column].eq(stage)].sort_values('event_date')
        following = {}
        for row in matching.itertuples():
            uid = int(row.user_id)
            if uid in current and uid not in following and row.event_date >= current[uid]:
                following[uid] = row.event_date
        results.append(len(following))
        current = following
    return results

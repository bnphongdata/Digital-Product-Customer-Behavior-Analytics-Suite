# Nguồn Gốc KPI & Quy Tắc Nghiệp Vụ (KPI Lineage)

Phương ngữ SQL: SQLite 3.25+; môi trường kiểm thử thực tế được ghi lại trong manifest. Mỗi tên kết quả tương ứng với một phần truy vấn có tên trong `SQL/analysis.sql`. Các ước lượng thống kê bổ sung được tính toán trong `portfolio/metrics.py` và đối soát chéo tại `portfolio/run.py`.

| Chỉ số | Cách tính / Mẫu số | Tệp kết quả | Cách hiểu đúng |
| --- | --- | --- | --- |
| snapshot_mrr | SUM(mrr), toàn bộ các dòng đăng ký được cung cấp | summary.csv | Chỉ là ảnh chụp dữ liệu tại thời điểm; không phải MRR đang hoạt động đã kiểm chứng. |
| snapshot_arr | 12 × snapshot_mrr | summary.csv | Ước tính quy năm, không phải doanh thu ghi nhận chuẩn kế toán. |
| paying_churn_label_rate | SUM(churned label với mrr > 0) / COUNT(mrr > 0) | summary.csv | Đã loại bỏ các tài khoản Free; nhãn churn không được tái dựng độc lập. |
| ordered onboarding | Số người dùng duy nhất hoàn thành tuần tự tất cả các bước trước đó vào/sau ngày đăng ký theo thứ tự ngày không giảm | onboarding_funnel.csv | Chấp nhận các bước diễn ra cùng ngày; lấy lần thử hợp lệ sớm nhất. |
| power-user association | Có từ 20 sự kiện Workflow Run trở lên trong [signup, signup+90 ngày), so sánh trong nhóm người dùng trả phí | power_user_association.csv | Đưa cả những người dùng có 0 hoạt động vào so sánh; chỉ mang tính tương quan. |

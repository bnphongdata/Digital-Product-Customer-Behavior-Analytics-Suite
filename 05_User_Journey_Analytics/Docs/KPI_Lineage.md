# Nguồn Gốc KPI & Quy Tắc Nghiệp Vụ (KPI Lineage)

Phương ngữ SQL: SQLite 3.25+; môi trường kiểm thử thực tế được ghi lại trong manifest. Mỗi tên kết quả tương ứng với một phần truy vấn có tên trong `SQL/analysis.sql`. Các ước lượng thống kê bổ sung được tính toán trong `portfolio/metrics.py` và đối soát chéo tại `portfolio/run.py`.

| Chỉ số | Cách tính / Mẫu số | Tệp kết quả | Cách hiểu đúng |
| --- | --- | --- | --- |
| observed_purchase_rate | Số người dùng duy nhất có sự kiện Purchase / tổng số người dùng | summary.csv | Tỷ lệ chạm mốc không xét thứ tự; thời gian theo dõi giữa các người dùng là khác nhau. |
| ordered_funnel | Số người dùng duy nhất hoàn thành tất cả 6 giai đoạn theo thứ tự ngày không giảm sau first_seen | ordered_funnel.csv | Chuẩn đoán phễu theo thứ tự thời gian nghiêm ngặt; cần phân biệt với tỷ lệ tiếp cận từng bước đơn lẻ. |
| returning conversion | Số người mua duy nhất / tổng số người dùng, tách riêng theo cờ người dùng quay lại | returning_user_conversion.csv | Mối liên hệ mang tính mô tả. |
| time to purchase | Ngày mua hàng hợp lệ đầu tiên − first_seen_date | time_to_purchase.csv | Điều kiện trên tập người dùng đã mua hàng quan sát được; không phải phân tích sống sót (survival analysis). |
| p50 / p90 | Phân vị tuyến tính (Pandas linear quantile) của số ngày chuyển đổi mua hàng hợp lệ quan sát được | additional_metrics.json | Chưa hiệu chỉnh cho hiện tượng dữ liệu bị kiểm duyệt phải (right-censoring). |

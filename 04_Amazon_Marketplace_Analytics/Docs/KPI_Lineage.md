# Nguồn Gốc KPI & Quy Tắc Nghiệp Vụ (KPI Lineage)

Phương ngữ SQL: SQLite 3.25+; môi trường kiểm thử thực tế được ghi lại trong manifest. Mỗi tên kết quả tương ứng với một phần truy vấn có tên trong `SQL/analysis.sql`. Các ước lượng thống kê bổ sung được tính toán trong `portfolio/metrics.py` và đối soát chéo tại `portfolio/run.py`.

| Chỉ số | Cách tính / Mẫu số | Tệp kết quả | Cách hiểu đúng |
| --- | --- | --- | --- |
| recorded_revenue | SUM(sales.revenue) | summary.csv | Không được dán nhãn là GMV hay doanh thu hoa hồng sàn. |
| sales_rows | COUNT(sales rows) | summary.csv | Không phải số lượng đơn hàng vì không có mã đơn hàng. |
| revenue discrepancy | ABS(doanh thu ghi nhận − giá × số lượng) > 0.011 | summary.csv | Dung sai trên 1 cent; chưa rõ nguyên nhân dữ liệu nguồn. |
| top-ten share | Doanh thu ghi nhận của top 10 người bán / tổng doanh thu ghi nhận | additional_metrics.json | Thứ hạng rút ra từ các mã người bán được cung cấp. |
| seller HHI | 10000 × SUM(tỷ phần doanh thu người bán bình phương) | additional_metrics.json | Chỉ số mô tả mức độ tập trung thị trường, không phải kết luận pháp lý. |
| stock association | Doanh thu ghi nhận trung bình của bài đăng, bao gồm cả bài có 0 lượt bán, theo danh mục/dải giá/cờ còn hàng | stock_status_association.csv | Không phải ước tính thiệt hại doanh thu do hết hàng mang tính nhân quả. |

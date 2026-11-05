# Nguồn Gốc KPI & Quy Tắc Nghiệp Vụ (KPI Lineage)

Phương ngữ SQL: SQLite 3.25+; môi trường kiểm thử thực tế được ghi lại trong manifest. Mỗi tên kết quả tương ứng với một phần truy vấn có tên trong `SQL/analysis.sql`. Các ước lượng thống kê bổ sung được tính toán trong `portfolio/metrics.py` và đối soát chéo tại `portfolio/run.py`.

| Chỉ số | Cách tính / Mẫu số | Tệp kết quả | Cách hiểu đúng |
| --- | --- | --- | --- |
| conversion_rate | SUM(purchased) / COUNT(web sessions) | summary.csv | Mẫu số là phiên truy cập (sessions), không phải người dùng. |
| cart_abandonment_rate | 1 − số phiên đã mua / số phiên thêm vào giỏ | summary.csv | Đã xác thực mua hàng đồng nghĩa với đã thêm vào giỏ. |
| average_order_value | SUM(order_value) / COUNT(order rows) | summary.csv | Tại đây đã xác thực mỗi phiên mua hàng chỉ có đúng một đơn hàng. |
| SKU top-20% share | Doanh thu của ceil(0.2 × distinct SKUs) sản phẩm top đầu / tổng doanh thu đơn hàng | additional_metrics.json | Khi trùng thứ hạng doanh thu, sắp xếp theo mã SKU để đảm bảo tính xác định. |
| discount association | AOV gom nhóm theo thiết bị, danh mục và cờ giảm giá quan sát được | discount_association.csv | Chỉ là mối liên hệ quan sát được, không phải tác động nhân quả của mã giảm giá; không tính chỉ số RFM khách hàng. |

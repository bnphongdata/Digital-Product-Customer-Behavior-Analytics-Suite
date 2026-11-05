# Nguồn Gốc KPI & Quy Tắc Nghiệp Vụ (KPI Lineage)

Phương ngữ SQL: SQLite 3.25+; môi trường kiểm thử thực tế được ghi lại trong manifest. Mỗi tên kết quả tương ứng với một phần truy vấn có tên trong `SQL/analysis.sql`. Các ước lượng thống kê bổ sung được tính toán trong `portfolio/metrics.py` và đối soát chéo tại `portfolio/run.py`.

| Chỉ số | Cách tính / Mẫu số | Tệp kết quả | Cách hiểu đúng |
| --- | --- | --- | --- |
| conversion_rate | SUM(converted) / COUNT(sessions), trong từng nhánh | variant_summary.csv | Giả định các phiên truy cập là độc lập phục vụ suy diễn thống kê. |
| absolute lift | Tỷ lệ chuyển đổi nhánh Variant B − Tỷ lệ nhánh Control | additional_metrics.json | Nhân với 100 để biểu thị theo điểm phần trăm. |
| relative lift | Lift tuyệt đối / Tỷ lệ nhánh Control | additional_metrics.json | Không xác định nếu tỷ lệ chuyển đổi Control bằng 0. |
| difference confidence interval | Khoảng tin cậy Newcombe cho hiệu số hai tỷ lệ sử dụng khoảng Wilson, 95% | additional_metrics.json | Khoảng tin cậy đơn lẻ chưa điều chỉnh cho biến chính. |
| p_value | Kiểm định Z hai phía cho hai tỷ lệ gộp (two-sided pooled two-proportion z-test) | additional_metrics.json | Không phải là xác suất giả thuyết nghiên cứu đúng. |
| srm_p_value_50_50 | Kiểm định độ phù hợp Chi-square (goodness-of-fit) với giả định phân bổ đều 50:50 | additional_metrics.json | Tỷ lệ phân bổ 50:50 là một giả định tường minh. |

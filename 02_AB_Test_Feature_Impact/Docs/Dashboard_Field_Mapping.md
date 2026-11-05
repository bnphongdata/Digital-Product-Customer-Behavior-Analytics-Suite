# Ánh Xạ Kết Quả Xác Thực Vào Biểu Đồ

Sử dụng các **bảng trong thư mục Results** làm nguồn dữ liệu tổng hợp. Các bảng này đã tính toán sẵn mẫu số của chỉ số và phân khúc tương ứng. Không cộng dồn các tỷ lệ phần trăm; hãy tính lại tỷ lệ từ tử số và mẫu số khi gom nhóm nhiều phân khúc.

- `conversion_rate` → `Results/variant_summary.csv`. Giả định các phiên truy cập là độc lập phục vụ suy diễn thống kê.
- `absolute lift` → `Results/additional_metrics.json`. Nhân với 100 để biểu thị theo điểm phần trăm (percentage points).
- `relative lift` → `Results/additional_metrics.json`. Không xác định nếu tỷ lệ chuyển đổi của nhóm Control bằng 0.
- `difference confidence interval` → `Results/additional_metrics.json`. Khoảng tin cậy đơn lẻ chưa điều chỉnh cho biến chính.
- `p_value` → `Results/additional_metrics.json`. Không phải là xác suất giả thuyết đúng.
- `srm_p_value_50_50` → `Results/additional_metrics.json`. Tỷ lệ phân bổ 50:50 là một giả định tường minh.

Tệp báo cáo độc lập `REPORT.html` trực quan hóa các kết quả từ chính các truy vấn SQL này. Các trường và ảnh chụp của dashboard cũ không được chứng thực bởi bảng ánh xạ này. Xem thêm `Dashboard_Reconciliation.md`.

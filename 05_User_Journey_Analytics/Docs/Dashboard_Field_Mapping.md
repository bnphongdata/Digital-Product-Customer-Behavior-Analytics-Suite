# Ánh Xạ Kết Quả Xác Thực Vào Biểu Đồ

Sử dụng các **bảng trong thư mục Results** làm nguồn dữ liệu tổng hợp. Các bảng này đã tính toán sẵn mẫu số của chỉ số và phân khúc tương ứng. Không cộng dồn các tỷ lệ phần trăm; hãy tính lại tỷ lệ từ tử số và mẫu số khi gom nhóm nhiều phân khúc.

- `observed_purchase_rate` → `Results/summary.csv`. Tỷ lệ chạm mốc không xét thứ tự; thời gian theo dõi giữa các người dùng là khác nhau.
- `ordered_funnel` → `Results/ordered_funnel.csv`. Chuẩn đoán phễu theo thứ tự thời gian nghiêm ngặt; cần phân biệt với tỷ lệ tiếp cận từng bước đơn lẻ.
- `returning conversion` → `Results/returning_user_conversion.csv`. Mối liên hệ mang tính mô tả.
- `time to purchase` → `Results/time_to_purchase.csv`. Điều kiện trên tập người dùng đã mua hàng quan sát được; không phải phân tích sống sót (survival analysis).
- `p50 / p90` → `Results/additional_metrics.json`. Chưa hiệu chỉnh cho hiện tượng dữ liệu bị kiểm duyệt phải (right-censoring).

Tệp báo cáo độc lập `REPORT.html` trực quan hóa các kết quả từ chính các truy vấn SQL này. Các trường và ảnh chụp của dashboard cũ không được chứng thực bởi bảng ánh xạ này. Xem thêm `Dashboard_Reconciliation.md`.

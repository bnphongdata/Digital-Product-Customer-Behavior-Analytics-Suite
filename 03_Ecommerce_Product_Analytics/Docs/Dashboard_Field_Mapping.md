# Ánh Xạ Kết Quả Xác Thực Vào Biểu Đồ

Sử dụng các **bảng trong thư mục Results** làm nguồn dữ liệu tổng hợp. Các bảng này đã tính toán sẵn mẫu số của chỉ số và phân khúc tương ứng. Không cộng dồn các tỷ lệ phần trăm; hãy tính lại tỷ lệ từ tử số và mẫu số khi gom nhóm nhiều phân khúc.

- `conversion_rate` → `Results/summary.csv`. Mẫu số là phiên truy cập (sessions), không phải người dùng.
- `cart_abandonment_rate` → `Results/summary.csv`. Đã xác thực mua hàng đồng nghĩa với đã thêm vào giỏ.
- `average_order_value` → `Results/summary.csv`. Tại đây đã xác thực mỗi phiên mua hàng chỉ có đúng một đơn hàng.
- `SKU top-20% share` → `Results/additional_metrics.json`. Khi trùng thứ hạng doanh thu, sắp xếp theo mã SKU để đảm bảo tính xác định.
- `discount association` → `Results/discount_association.csv`. Chỉ là mối tương quan quan sát được, không phải tác động nhân quả của mã giảm giá; không tính chỉ số RFM khách hàng.

Tệp báo cáo độc lập `REPORT.html` trực quan hóa các kết quả từ chính các truy vấn SQL này. Các trường và ảnh chụp của dashboard cũ không được chứng thực bởi bảng ánh xạ này. Xem thêm `Dashboard_Reconciliation.md`.

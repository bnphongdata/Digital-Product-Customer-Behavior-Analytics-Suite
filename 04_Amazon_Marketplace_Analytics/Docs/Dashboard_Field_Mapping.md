# Ánh Xạ Kết Quả Xác Thực Vào Biểu Đồ

Sử dụng các **bảng trong thư mục Results** làm nguồn dữ liệu tổng hợp. Các bảng này đã tính toán sẵn mẫu số của chỉ số và phân khúc tương ứng. Không cộng dồn các tỷ lệ phần trăm; hãy tính lại tỷ lệ từ tử số và mẫu số khi gom nhóm nhiều phân khúc.

- `recorded_revenue` → `Results/summary.csv`. Không được dán nhãn là GMV hay doanh thu hoa hồng sàn.
- `sales_rows` → `Results/summary.csv`. Không phải số lượng đơn hàng vì không có mã đơn hàng (order ID).
- `revenue discrepancy` → `Results/summary.csv`. Dung sai sai lệch trên 1 cent; chưa rõ nguyên nhân dữ liệu nguồn.
- `top-ten share` → `Results/additional_metrics.json`. Thứ hạng rút ra từ các mã người bán (seller ID) được cung cấp.
- `seller HHI` → `Results/additional_metrics.json`. Chỉ số mô tả mức độ tập trung thị trường, không phải kết luận pháp lý chống độc quyền.
- `stock association` → `Results/stock_status_association.csv`. Không phải ước tính thiệt hại doanh thu do hết hàng mang tính nhân quả.

Tệp báo cáo độc lập `REPORT.html` trực quan hóa các kết quả từ chính các truy vấn SQL này. Các trường và ảnh chụp của dashboard cũ không được chứng thực bởi bảng ánh xạ này. Xem thêm `Dashboard_Reconciliation.md`.

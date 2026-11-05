# Ánh Xạ Kết Quả Xác Thực Vào Biểu Đồ

Sử dụng các **bảng trong thư mục Results** làm nguồn dữ liệu tổng hợp. Các bảng này đã tính toán sẵn mẫu số của chỉ số và phân khúc tương ứng. Không cộng dồn các tỷ lệ phần trăm; hãy tính lại tỷ lệ từ tử số và mẫu số khi gom nhóm nhiều phân khúc.

- `snapshot_mrr` → `Results/summary.csv`. Chỉ là ảnh chụp dữ liệu tại một thời điểm; không phải MRR đang hoạt động đã được kiểm chứng.
- `snapshot_arr` → `Results/summary.csv`. Ước tính quy năm, không phải doanh thu ghi nhận chuẩn kế toán.
- `paying_churn_label_rate` → `Results/summary.csv`. Đã loại bỏ các tài khoản miễn phí; nhãn churn không được tái dựng độc lập.
- `ordered onboarding` → `Results/onboarding_funnel.csv`. Chấp nhận các bước trùng ngày; lấy lần thử sớm nhất hợp lệ.
- `power-user association` → `Results/power_user_association.csv`. So sánh trong nhóm người dùng trả phí; chỉ mang tính tương quan khảo sát.

Tệp báo cáo độc lập `REPORT.html` trực quan hóa các kết quả từ chính các truy vấn SQL này. Các trường và ảnh chụp của dashboard cũ không được chứng thực bởi bảng ánh xạ này. Xem thêm `Dashboard_Reconciliation.md`.

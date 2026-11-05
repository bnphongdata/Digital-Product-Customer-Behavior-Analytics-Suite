# Từ Điển Dữ Liệu Nguồn (Data Dictionary)

Tất cả dữ liệu đầu vào đều là các tệp CSV **mô phỏng (synthetic/simulated)**. Các thông tin như mã tiền tệ, seed sinh dữ liệu, chủ sở hữu nguồn và mốc thời gian trích xuất không được cung cấp trong bộ dữ liệu gốc. Quy trình nâng cấp này không tự bịa đặt thêm dữ liệu. Từng byte dữ liệu thô được bảo toàn nguyên vẹn và băm mã kiểm tra (hash) trong `Results/manifest.json`.

## Quy ước kiểm tra hợp đồng dữ liệu (Contract Conventions)

Tất cả các cột được liệt kê đều bắt buộc và không được chứa giá trị null. Các trường số phải là số hữu hạn, không âm; các trường ID và số lượng (units/seats) phải là số dương. Các trường nhị phân (binary) chấp nhận 0/1 hoặc true/false và được chuẩn hóa về 0/1. Định dạng ngày là YYYY-MM-DD. Dữ liệu chuỗi được cắt tỉa khoảng trắng (trimmed). Quy trình kiểm tra sẽ báo lỗi dừng ngay nếu gặp cột lạ, trùng khóa chính hoặc bản ghi mồ côi (orphan references). Các bản ghi sự kiện/fact lặp lại không có ID cố định vẫn được đếm và bảo toàn nguyên trạng.

## ab_sessions

Số dòng: **12.000**. Khóa chính: **session_id**. Nguồn: `Data/raw/ab_sessions_raw.csv`; kết quả: `Data/clean/ab_sessions_clean.csv`.
| Cột | Kiểu dữ liệu | Ý nghĩa |
| --- | --- | --- |
| `session_id` | integer | Mã định danh phiên truy cập duy nhất; không thể thay thế cho mã khách hàng định danh lâu dài. |
| `session_date` | date | Ngày quan sát phiên truy cập (mức ngày). |
| `variant` | text | Nhánh thử nghiệm: Control hoặc Variant B; không có metadata về thuật toán phân bổ. |
| `device` | text | Danh mục thiết bị; tập giá trị danh mục có thể khác nhau giữa các dự án. |
| `source` | text | Kênh nguồn traffic thử nghiệm. |
| `converted` | binary | Cờ nhị phân biểu thị việc chuyển đổi trong phiên. |
| `engagement_score` | number | Điểm tương tác mô phỏng; thang đo không được quy định độc lập. |
| `bounce` | binary | Cờ nhị phân biểu thị phiên thoát trang ngay (bounce). |
| `revenue` | number | Doanh thu ghi nhận theo đơn vị tiền tệ của bộ dữ liệu; không có thuyết minh quy chuẩn kế toán. |

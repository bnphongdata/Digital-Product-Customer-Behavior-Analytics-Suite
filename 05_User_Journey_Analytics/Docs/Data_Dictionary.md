# Từ Điển Dữ Liệu Nguồn (Data Dictionary)

Tất cả dữ liệu đầu vào đều là các tệp CSV **mô phỏng (synthetic/simulated)**. Các thông tin như mã tiền tệ, seed sinh dữ liệu, chủ sở hữu nguồn và mốc thời gian trích xuất không được cung cấp trong bộ dữ liệu gốc. Quy trình nâng cấp này không tự bịa đặt thêm dữ liệu. Từng byte dữ liệu thô được bảo toàn nguyên vẹn và băm mã kiểm tra (hash) trong `Results/manifest.json`.

## Quy ước kiểm tra hợp đồng dữ liệu (Contract Conventions)

Tất cả các cột được liệt kê đều bắt buộc và không được chứa giá trị null. Các trường số phải là số hữu hạn, không âm; các trường ID và số lượng (units/seats) phải là số dương. Các trường nhị phân (binary) chấp nhận 0/1 hoặc true/false và được chuẩn hóa về 0/1. Định dạng ngày là YYYY-MM-DD. Dữ liệu chuỗi được cắt tỉa khoảng trắng (trimmed). Quy trình kiểm tra sẽ báo lỗi dừng ngay nếu gặp cột lạ, trùng khóa chính hoặc bản ghi mồ côi (orphan references). Các bản ghi sự kiện/fact lặp lại không có ID cố định vẫn được đếm và bảo toàn nguyên trạng.

## users

Số dòng: **6.000**. Khóa chính: **user_id**. Nguồn: `Data/raw/users_raw.csv`; kết quả: `Data/clean/users_clean.csv`.
| Cột | Kiểu dữ liệu | Ý nghĩa |
| --- | --- | --- |
| `user_id` | integer | Định danh người dùng nội bộ trong bộ dữ liệu; không chia sẻ chéo giữa các dự án. |
| `first_seen_date` | date | Ngày quan sát đầu tiên được ghi nhận; không nhất thiết là ngày đăng ký tài khoản. |
| `traffic_source` | text | Kênh nguồn traffic người dùng được cung cấp. |
| `device` | text | Danh mục thiết bị; tập giá trị danh mục có thể khác nhau giữa các dự án. |
| `is_returning` | binary | Cờ nhị phân người dùng quay lại; không có định nghĩa khoảng thời gian xem lại (lookback). |

## journey_events

Số dòng: **17.354**. Khóa chính: **không có sẵn**. Nguồn: `Data/raw/journey_events_raw.csv`; kết quả: `Data/clean/journey_events_clean.csv`.
| Cột | Kiểu dữ liệu | Ý nghĩa |
| --- | --- | --- |
| `user_id` | integer | Định danh người dùng nội bộ trong bộ dữ liệu; không chia sẻ chéo giữa các dự án. |
| `event_date` | date | Ngày diễn ra sự kiện (mức ngày); không có timestamp chi tiết hay mã định danh sự kiện. |
| `journey_stage` | text | Tên giai đoạn hành trình; giai đoạn Signup được tách riêng khỏi luồng thương mại tuần tự. |
| `stage_order` | integer | Số thứ tự giai đoạn danh nghĩa; chỉ mang tính mô tả thứ tự lý thuyết, không phản ánh trình tự thời gian sự kiện thực tế. |

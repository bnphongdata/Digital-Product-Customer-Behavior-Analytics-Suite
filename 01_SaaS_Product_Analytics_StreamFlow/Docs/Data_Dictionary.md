# Từ Điển Dữ Liệu Nguồn (Data Dictionary)

Tất cả dữ liệu đầu vào đều là các tệp CSV **mô phỏng (synthetic/simulated)**. Các thông tin như mã tiền tệ, seed sinh dữ liệu, chủ sở hữu nguồn và mốc thời gian trích xuất không được cung cấp trong bộ dữ liệu gốc. Quy trình nâng cấp này không tự bịa đặt thêm dữ liệu. Từng byte dữ liệu thô được bảo toàn nguyên vẹn và băm mã kiểm tra (hash) trong `Results/manifest.json`.

## Quy ước kiểm tra hợp đồng dữ liệu (Contract Conventions)

Tất cả các cột được liệt kê đều bắt buộc và không được chứa giá trị null. Các trường số phải là số hữu hạn, không âm; các trường ID và số lượng (units/seats) phải là số dương. Các trường nhị phân (binary) chấp nhận 0/1 hoặc true/false và được chuẩn hóa về 0/1. Định dạng ngày là YYYY-MM-DD. Dữ liệu chuỗi được cắt tỉa khoảng trắng (trimmed). Quy trình kiểm tra sẽ báo lỗi dừng ngay nếu gặp cột lạ, trùng khóa chính hoặc bản ghi mồ côi (orphan references). Các bản ghi sự kiện/fact lặp lại không có ID cố định vẫn được đếm và bảo toàn nguyên trạng.

## users

Số dòng: **1.500**. Khóa chính: **user_id**. Nguồn: `Data/raw/users_raw.csv`; kết quả: `Data/clean/users_clean.csv`.
| Cột | Kiểu dữ liệu | Ý nghĩa |
| --- | --- | --- |
| `user_id` | integer | Định danh người dùng nội bộ trong bộ dữ liệu; không chia sẻ chéo giữa các dự án. |
| `signup_date` | date | Ngày đăng ký tài khoản được ghi nhận; mốc bắt đầu theo dõi quá trình onboarding và hoạt động. |
| `country` | text | Mã quốc gia theo dữ liệu gốc; không bổ sung dữ liệu địa lý bên ngoài. |
| `acquisition_channel` | text | Kênh thu hút người dùng được ghi nhận trong dữ liệu gốc. |
| `plan_tier` | text | Gói cước dịch vụ: Free, Starter, Pro hoặc Enterprise. |

## subscriptions

Số dòng: **1.500**. Khóa chính: **user_id**. Nguồn: `Data/raw/subscriptions_raw.csv`; kết quả: `Data/clean/subscriptions_clean.csv`.
| Cột | Kiểu dữ liệu | Ý nghĩa |
| --- | --- | --- |
| `user_id` | integer | Định danh người dùng nội bộ trong bộ dữ liệu; không chia sẻ chéo giữa các dự án. |
| `plan_tier` | text | Gói cước dịch vụ: Free, Starter, Pro hoặc Enterprise. |
| `mrr` | number | Ảnh chụp doanh thu định kỳ hàng tháng (MRR) theo đơn vị tiền tệ của bộ dữ liệu. |
| `seats` | integer | Số lượng chỗ (seat) trong gói đăng ký. |
| `completed_step2` | binary | Cờ đánh dấu đã hoàn thành Bước 2 onboarding, được đối soát chéo với nhật ký sự kiện thực tế. |
| `churned_within_90d` | binary | Nhãn nhị phân thể hiện việc rời bỏ trong 90 ngày; không có dữ liệu vòng đời chi tiết và điểm cắt cohort. |
| `first_payment_date` | date | Ngày thanh toán đầu tiên theo dữ liệu gốc, bao gồm cả bản ghi gói Free; không phải bằng chứng độc lập của việc đăng ký trả phí. |

## events

Số dòng: **29.175**. Khóa chính: **không có sẵn**. Nguồn: `Data/raw/events_raw.csv`; kết quả: `Data/clean/events_clean.csv`.
| Cột | Kiểu dữ liệu | Ý nghĩa |
| --- | --- | --- |
| `user_id` | integer | Định danh người dùng nội bộ trong bộ dữ liệu; không chia sẻ chéo giữa các dự án. |
| `event_date` | date | Ngày diễn ra sự kiện (mức ngày); không có timestamp chi tiết hay mã định danh sự kiện. |
| `event_group` | text | Nhóm sự kiện (Onboarding hoặc Product). |
| `event_name` | text | Tên sự kiện, bao gồm các bước onboarding và sự kiện Workflow Run. |

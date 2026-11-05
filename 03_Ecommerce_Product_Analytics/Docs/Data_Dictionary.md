# Từ Điển Dữ Liệu Nguồn (Data Dictionary)

Tất cả dữ liệu đầu vào đều là các tệp CSV **mô phỏng (synthetic/simulated)**. Các thông tin như mã tiền tệ, seed sinh dữ liệu, chủ sở hữu nguồn và mốc thời gian trích xuất không được cung cấp trong bộ dữ liệu gốc. Quy trình nâng cấp này không tự bịa đặt thêm dữ liệu. Từng byte dữ liệu thô được bảo toàn nguyên vẹn và băm mã kiểm tra (hash) trong `Results/manifest.json`.

## Quy ước kiểm tra hợp đồng dữ liệu (Contract Conventions)

Tất cả các cột được liệt kê đều bắt buộc và không được chứa giá trị null. Các trường số phải là số hữu hạn, không âm; các trường ID và số lượng (units/seats) phải là số dương. Các trường nhị phân (binary) chấp nhận 0/1 hoặc true/false và được chuẩn hóa về 0/1. Định dạng ngày là YYYY-MM-DD. Dữ liệu chuỗi được cắt tỉa khoảng trắng (trimmed). Quy trình kiểm tra sẽ báo lỗi dừng ngay nếu gặp cột lạ, trùng khóa chính hoặc bản ghi mồ côi (orphan references). Các bản ghi sự kiện/fact lặp lại không có ID cố định vẫn được đếm và bảo toàn nguyên trạng.

## web_sessions

Số dòng: **25.000**. Khóa chính: **session_id**. Nguồn: `Data/raw/web_sessions_raw.csv`; kết quả: `Data/clean/web_sessions_clean.csv`.
| Cột | Kiểu dữ liệu | Ý nghĩa |
| --- | --- | --- |
| `session_id` | integer | Mã định danh phiên truy cập duy nhất; không thể thay thế cho mã khách hàng định danh lâu dài. |
| `session_date` | date | Ngày quan sát phiên truy cập (mức ngày). |
| `device` | text | Danh mục thiết bị; tập giá trị danh mục có thể khác nhau giữa các dự án. |
| `channel` | text | Kênh thu hút phiên truy cập. |
| `added_to_cart` | binary | Cờ nhị phân biểu thị phiên có thêm sản phẩm vào giỏ hàng. |
| `purchased` | binary | Cờ nhị phân biểu thị phiên có thực hiện giao dịch mua hàng. |

## orders

Số dòng: **3.037**. Khóa chính: **session_id**. Nguồn: `Data/raw/orders_raw.csv`; kết quả: `Data/clean/orders_clean.csv`.
| Cột | Kiểu dữ liệu | Ý nghĩa |
| --- | --- | --- |
| `session_id` | integer | Mã định danh phiên truy cập duy nhất; không thể thay thế cho mã khách hàng định danh lâu dài. |
| `session_date` | date | Ngày quan sát phiên truy cập (mức ngày). |
| `device` | text | Danh mục thiết bị; tập giá trị danh mục có thể khác nhau giữa các dự án. |
| `channel` | text | Kênh thu hút phiên truy cập. |
| `sku` | text | Mã định danh SKU sản phẩm; mỗi dòng đơn hàng được cung cấp tương ứng với một SKU. |
| `category` | text | Danh mục ngành hàng sản phẩm. |
| `discount_applied` | binary | Cờ nhị phân quan sát thấy có giảm giá; không phải can thiệp ngẫu nhiên có kiểm soát. |
| `order_value` | number | Giá trị đơn hàng ghi nhận; không có thông tin chi tiết về hoàn tiền, thuế và phí vận chuyển. |
| `units` | integer | Số lượng đơn vị sản phẩm trong dòng đơn hàng. |

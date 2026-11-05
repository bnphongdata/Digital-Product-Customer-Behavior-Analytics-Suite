# Từ Điển Dữ Liệu Nguồn (Data Dictionary)

Tất cả dữ liệu đầu vào đều là các tệp CSV **mô phỏng (synthetic/simulated)**. Các thông tin như mã tiền tệ, seed sinh dữ liệu, chủ sở hữu nguồn và mốc thời gian trích xuất không được cung cấp trong bộ dữ liệu gốc. Quy trình nâng cấp này không tự bịa đặt thêm dữ liệu. Từng byte dữ liệu thô được bảo toàn nguyên vẹn và băm mã kiểm tra (hash) trong `Results/manifest.json`.

## Quy ước kiểm tra hợp đồng dữ liệu (Contract Conventions)

Tất cả các cột được liệt kê đều bắt buộc và không được chứa giá trị null. Các trường số phải là số hữu hạn, không âm; các trường ID và số lượng (units/seats) phải là số dương. Các trường nhị phân (binary) chấp nhận 0/1 hoặc true/false và được chuẩn hóa về 0/1. Định dạng ngày là YYYY-MM-DD. Dữ liệu chuỗi được cắt tỉa khoảng trắng (trimmed). Quy trình kiểm tra sẽ báo lỗi dừng ngay nếu gặp cột lạ, trùng khóa chính hoặc bản ghi mồ côi (orphan references). Các bản ghi sự kiện/fact lặp lại không có ID cố định vẫn được đếm và bảo toàn nguyên trạng.

## listings

Số dòng: **1.800**. Khóa chính: **listing_id**. Nguồn: `Data/raw/listings_raw.csv`; kết quả: `Data/clean/listings_clean.csv`.
| Cột | Kiểu dữ liệu | Ý nghĩa |
| --- | --- | --- |
| `listing_id` | integer | Mã bài đăng sản phẩm; dùng trường này để kết nối bảng sales với listings. |
| `seller_id` | integer | Mã người bán; một người bán có thể có nhiều bài đăng sản phẩm. |
| `category` | text | Danh mục ngành hàng sản phẩm. |
| `price` | number | Ảnh chụp giá niêm yết/đơn vị sản phẩm theo dữ liệu gốc. |
| `rating` | number | Điểm đánh giá bài đăng sản phẩm theo thang điểm 0–5. |
| `in_stock` | binary | Cờ nhị phân chụp trạng thái còn hàng không ghi ngày; không phải dữ liệu tồn kho lịch sử. |

## sales

Số dòng: **24.000**. Khóa chính: **không có sẵn**. Nguồn: `Data/raw/sales_raw.csv`; kết quả: `Data/clean/sales_clean.csv`.
| Cột | Kiểu dữ liệu | Ý nghĩa |
| --- | --- | --- |
| `sale_date` | date | Ngày phát sinh bán hàng được ghi nhận (mức ngày). |
| `listing_id` | integer | Mã bài đăng sản phẩm; dùng trường này để kết nối bảng sales với listings. |
| `units_sold` | integer | Số lượng đơn vị bán được ghi nhận trên mỗi dòng giao dịch; không có mã đơn hàng/giao dịch. |
| `seller_id` | integer | Mã người bán; một người bán có thể có nhiều bài đăng sản phẩm. |
| `price` | number | Ảnh chụp giá niêm yết/đơn vị sản phẩm theo dữ liệu gốc. |
| `rating` | number | Điểm đánh giá bài đăng sản phẩm theo thang điểm 0–5. |
| `in_stock` | binary | Cờ nhị phân chụp trạng thái còn hàng không ghi ngày; không phải dữ liệu tồn kho lịch sử. |
| `category` | text | Danh mục ngành hàng sản phẩm. |
| `revenue` | number | Doanh thu ghi nhận theo đơn vị tiền tệ của bộ dữ liệu; không có thuyết minh quy chuẩn kế toán. |

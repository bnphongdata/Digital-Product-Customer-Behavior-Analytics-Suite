# Hướng Dẫn Cho Người Đánh Giá & Danh Mục Nguồn Gốc Tài Sản

**Dự án:** data-analyst-portfolio · [README](README.md) · [Giấy phép (License)](LICENSE) · [Trạng thái CI](https://github.com/buinhatphong/digital-product-analytics-portfolio/actions)

## Đánh giá nhanh trong 5 phút

1. Đọc tệp README gốc để nắm rõ mục đích của dự án, các giới hạn dữ liệu và phân biệt rõ phần nào là dữ liệu mô phỏng, phần nào đã được đối soát độc lập.
2. Mở các đường dẫn dự án bên dưới để xem trực tiếp các sản phẩm bàn giao ban đầu. Các liên kết này trỏ đến nhánh mặc định của dự án.
3. Kiểm tra các lần chạy trên GitHub Actions để xem các lần kiểm tra gần nhất và kết luận tương ứng. Một bài kiểm tra đang chờ hoặc thất bại thì không được coi là đã vượt qua.
4. Kiểm tra kỹ dữ liệu đầu vào, công thức tính toán và kết quả đầu ra trước khi trích dẫn các chỉ số hiệu suất hoặc tác động kinh doanh.

### Các điểm truy cập dự án

1. [01_SaaS_Product_Analytics_StreamFlow](<01_SaaS_Product_Analytics_StreamFlow>)
2. [02_AB_Test_Feature_Impact](<02_AB_Test_Feature_Impact>)
3. [03_Ecommerce_Product_Analytics](<03_Ecommerce_Product_Analytics>)
4. [04_Amazon_Marketplace_Analytics](<04_Amazon_Marketplace_Analytics>)
5. [05_User_Journey_Analytics](<05_User_Journey_Analytics>)

## Rà soát nguồn gốc tài sản & Quyền phân phối lại

Các **tệp mẫu được theo dõi** dưới đây cần được rà soát về nguồn gốc và quyền sở hữu. Việc liệt kê tệp ở đây không đồng nghĩa với việc tệp đó là tài liệu của bên thứ ba hay vi phạm bản quyền. Cần xác nhận người tạo hoặc nhà cung cấp, đường dẫn gốc (nếu là nguồn ngoài), các điều khoản áp dụng, quyền chia sẻ/chỉnh sửa và đảm bảo không có dữ liệu cá nhân hay dữ liệu khách hàng thực tế nào bị rò rỉ.

| Tài sản được theo dõi | Tình trạng xác minh nguồn gốc và bản quyền |
| --- | --- |
| `01_SaaS_Product_Analytics_StreamFlow/Dashboard/Product Analytics Dashboard - StreamFlow (Simulated SaaS).twbx` | **Chưa xác minh độc lập** — kiểm tra nguồn gốc và quyền sử dụng |
| `01_SaaS_Product_Analytics_StreamFlow/Data/clean/events_clean.csv` | **Chưa xác minh độc lập** — kiểm tra nguồn gốc và quyền sử dụng |
| `01_SaaS_Product_Analytics_StreamFlow/Data/clean/subscriptions_clean.csv` | **Chưa xác minh độc lập** — kiểm tra nguồn gốc và quyền sử dụng |
| `01_SaaS_Product_Analytics_StreamFlow/Data/clean/users_clean.csv` | **Chưa xác minh độc lập** — kiểm tra nguồn gốc và quyền sử dụng |
| `01_SaaS_Product_Analytics_StreamFlow/Data/raw/events_raw.csv` | **Chưa xác minh độc lập** — kiểm tra nguồn gốc và quyền sử dụng |
| `01_SaaS_Product_Analytics_StreamFlow/Data/raw/subscriptions_raw.csv` | **Chưa xác minh độc lập** — kiểm tra nguồn gốc và quyền sử dụng |
| `01_SaaS_Product_Analytics_StreamFlow/Data/raw/users_raw.csv` | **Chưa xác minh độc lập** — kiểm tra nguồn gốc và quyền sử dụng |
| `01_SaaS_Product_Analytics_StreamFlow/Excel/01_SaaS_Product_Analytics_StreamFlow_Model.xlsx` | **Chưa xác minh độc lập** — kiểm tra nguồn gốc và quyền sử dụng |

### Tiêu chuẩn xác thực

- Đối với tài sản tự tạo (first-party): ghi nhận rõ cách tạo lập và xác nhận xem tài sản đó chứa dữ liệu tự sinh hay dữ liệu mô phỏng.
- Đối với tài sản từ bên ngoài: trích dẫn nguồn, tác giả/nhà cung cấp, phiên bản, giấy phép và quyền phân phối lại/sử dụng thương mại.
- Đối với kết quả từ mô hình: gắn nhãn chính xác và nhất quán là **mô phỏng (simulated)**, **minh họa (illustrative)** hoặc **đo lường thực tế (measured)**.
- Nếu không thể xác định rõ quyền sở hữu hoặc quyền hạn, không được khẳng định rằng giấy phép MIT của repo cấp quyền cho tài liệu đó. Hãy xóa bỏ hoặc thay thế tài liệu khi cần thiết.
- Tuyệt đối không đưa mật khẩu, thông tin xác thực API, dữ liệu riêng tư hay ảnh chụp màn hình nhạy cảm vào tài liệu bằng chứng.

## Phạm vi và giới hạn

Đây là danh mục hỗ trợ điều hướng và **rà soát kiểm tra**, không phải chứng nhận bảo mật hay chứng thư pháp lý cho bất kỳ tài sản nào. Các bước kiểm tra tự động không chứng minh quyền của bên thứ ba hay tính chính xác tuyệt đối của kết quả kinh doanh ngoài thực tế. Vui lòng tham khảo [GitHub Actions](https://github.com/buinhatphong/digital-product-analytics-portfolio/actions) để xem trạng thái kiểm thử trực tiếp mới nhất.

# Nhật Ký Nâng Cấp Dự Án (Upgrade Notes)

## Phạm vi nâng cấp

Tái cấu trúc toàn bộ tầng phân tích dữ liệu cho cả 5 dự án hiện có, giữ nguyên vẹn 10 tệp CSV thô gốc và toàn bộ các tệp dashboard BI, Excel và hình ảnh ban đầu. Bản nâng cấp dựa trên commit chính `5887f7940282859197689b60e41be3e5a8287724`.

## Các thay đổi chính

- Thay thế các script Python mẫu tạm bợ bằng một pipeline thực thi thống nhất, có điểm truy cập riêng cho từng dự án.
- Tổng hợp toàn bộ mã SQL hoạt động vào các tệp SQLite query có đặt tên cụ thể và chạy được ngay. Tệp `advanced_queries.sql` cũ được bổ sung hướng dẫn trỏ tới tệp phân tích chuẩn.
- Bổ sung hợp đồng dữ liệu có định kiểu rõ ràng, kiểm tra ràng buộc quan hệ bảng, làm sạch cẩn trọng và công khai các chẩn đoán chất lượng dữ liệu nguồn.
- Khắc phục các lỗi logic: phân biệt rõ giữa phiên truy cập và định danh khách hàng, kiểm tra tính hợp lệ và thứ tự thời gian của phễu, tính đúng mẫu số của tỷ lệ churn nhóm trả phí, chuẩn hóa nhãn doanh thu sàn và đo lường khoảng tin cậy của thử nghiệm A/B.
- Thay thế các kết luận kinh doanh thiếu căn cứ bằng những phát hiện đo lường cụ thể kèm đề xuất hành động có điều kiện rõ ràng.
- Bổ sung case study chi tiết, báo cáo phân tích HTML offline có biểu đồ trực quan, từ điển dữ liệu (data dictionary), nguồn gốc KPI (KPI lineage), danh mục đối soát dashboard cũ, kế hoạch thực thi truy vấn (query plans) và mã băm SHA-256.
- Bổ sung hệ thống kiểm thử tự động (unit test & integration test) cùng quy trình CI trên GitHub Actions tự động kiểm tra sai lệch số liệu.
- Cập nhật và chuẩn hóa thông tin cá nhân của Bùi Nhất Phong.

## Bằng chứng kiểm thử

Quá trình chạy toàn bộ cục bộ đã xử lý 121.366 dòng dữ liệu và vượt qua 93 bước kiểm tra đối soát. Toàn bộ 48 bài kiểm thử tự động đều đạt kết quả PASS. Tệp manifest lưu trữ chính xác thông tin môi trường, mã băm của tệp nguồn, mã phân tích và tệp kết quả đầu ra.

## Những phát hiện quan trọng từ dữ liệu

- Dữ liệu sự kiện SaaS có 481 dòng trùng lặp hoàn toàn nhưng không có mã định danh sự kiện; các dòng này được giữ nguyên và công khai số lượng.
- Dữ liệu bán hàng trên sàn có 140 dòng trùng lặp hoàn toàn và 9.019 dòng có chênh lệch giữa doanh thu và giá × số lượng; các chênh lệch này được giữ nguyên để điều tra nguồn.
- Dữ liệu hành trình có 3.296 người dùng bị đảo lộn thứ tự ngày giữa các bước kế tiếp. Tỷ lệ tiếp cận bước mua hàng và tỷ lệ hoàn thành phễu tuần tự trả lời hai câu hỏi khác nhau; sự sụt giảm phễu tuần tự không bị quy chụp thành khách hàng bỏ giỏ thanh toán.
- Đóng góp doanh thu của Top 20% SKU thương mại điện tử thực tế là 31,42%, thay thế cho tuyên bố thiếu căn cứ 68% trước đây.
- Thử nghiệm A/B ghi nhận mức tăng chuyển đổi tương đối là 16,33%, tăng tuyệt đối 3,24 điểm phần trăm với khoảng tin cậy 95% từ 1,77 đến 4,71 điểm phần trăm dưới các giả định đã nêu.

## Các giới hạn còn lại

Chưa thực hiện làm mới trực tiếp trên Power BI/Tableau/Excel Desktop bản quyền. Script sinh dữ liệu gốc và nhật ký phân bổ thử nghiệm ban đầu không được cung cấp. Phân tích này không đại diện cho việc triển khai trên hệ thống production hay cam kết kết quả kinh doanh ngoài đời thực.

## Cập nhật xác thực tệp gốc

Rà soát toàn bộ các sổ làm việc gốc, đính chính cả 5 bảng tổng hợp Excel, kiểm chứng công thức bằng Artifact Tool và desktop Calc kèm bằng chứng thay đổi giá trị ô. Xây dựng 3 tệp dữ liệu Tableau Hyper thay thế với 18 bảng được xác thực từng ô. Giải mã mô hình PBIX và cung cấp 19 giá trị baseline tính độc lập bằng truy vấn DAX. Toàn bộ 5 dashboard BI cũ được xác nhận là dùng tập dữ liệu khác với dữ liệu chuẩn hiện tại; sự khác biệt này được ghi nhận minh bạch trong báo cáo kiểm định.

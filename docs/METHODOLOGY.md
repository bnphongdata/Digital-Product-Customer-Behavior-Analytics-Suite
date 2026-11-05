# Phương Pháp Luận, Giới Hạn Dữ Liệu & Các Quyết Định Phân Tích

## Nguồn gốc dữ liệu

Mười tệp CSV dữ liệu gốc đã có sẵn trong repository từ commit ban đầu `5887f7940282859197689b60e41be3e5a8287724`. Đây là các dữ liệu phân tích mô phỏng. Dữ liệu gốc không đi kèm script sinh dữ liệu, seed ngẫu nhiên, nhật ký phân bổ thử nghiệm, mã sự kiện hay mã tiền tệ cụ thể. Toàn bộ tệp dữ liệu thô ban đầu đều được giữ nguyên vẹn từng byte. Giấy phép MIT của repository áp dụng cho mã nguồn được cung cấp; bản cập nhật này không khẳng định quyền sở hữu bên thứ ba hay giấy phép thượng nguồn nào khác.

## Pipeline xử lý & Ranh giới tin cậy

CSV thô → Kiểm tra cấu trúc/kiểu/phạm vi/khóa chính → CSV sạch → Bảng SQLite → Truy vấn SQL có đặt tên → CSV kết quả → Đối soát độc lập bằng pandas → Ước lượng thống kê → Case study & Báo cáo HTML → Tệp mã băm SHA-256 manifest.

Bộ chạy tự động sẽ báo lỗi và dừng ngay nếu gặp giá trị rỗng ở trường bắt buộc, ngày tháng hoặc boolean không hợp lệ, số liệu nằm ngoài quy ước, cấu trúc bảng bị lệch, trùng lặp khóa chính, quan hệ bảng bị gãy hoặc sai lệch số liệu đối soát. Trình chạy sẽ hủy bằng chứng thành công cũ trước khi bắt đầu dự án mới. Nếu một lần chạy thất bại, các tệp kết quả dở dang sẽ không được sử dụng: người dùng cần kiểm tra cả manifest và báo cáo xác thực đạt chuẩn, sau đó chạy lại sau khi sửa lỗi nguồn. Tuyệt đối không dùng báo cáo HTML cũ sau một lần chạy bị lỗi.

Quy trình làm sạch dữ liệu tuân thủ nguyên tắc cẩn trọng: Cho phép chuẩn hóa kiểu dữ liệu và cắt bỏ khoảng trắng thừa. Không tự tạo thêm dữ liệu bẩn giả tạo. Các dòng sự kiện và bán hàng bị lặp lại mà không có mã sự kiện cố định sẽ được giữ nguyên, vì không thể phân biệt rạch ròi giữa hành động hợp lệ lặp lại và lỗi trùng lặp khi nạp dữ liệu. Số lượng dòng trùng lặp tuyệt đối được thống kê công khai. Các điểm bất thường và ngữ cảnh còn thiếu được ghi nhận minh bạch trong tệp `quality.json`.

## Tính tương thích & Hiệu năng SQL

Toàn bộ các truy vấn SQL hoạt động đều hướng tới chuẩn SQLite 3.25+ để tránh phân mảnh cú pháp giữa các hệ thống kho dữ liệu khác nhau. Sử dụng Python 3.12 với các thư viện đã được ghim phiên bản. Bộ chạy sẽ tự động tạo chỉ mục (index) cho khóa chính/khóa ngoại và ghi lại kết quả `EXPLAIN QUERY PLAN` cho từng truy vấn. Điều này giúp kiểm tra kế hoạch thực thi cục bộ, không đại diện cho hiệu năng trên quy mô kho dữ liệu lớn hay môi trường production. Các hàm ngày tháng trong SQLite hoạt động trên chuẩn ISO date. Hàm `NULLIF` giúp các phép chia có mẫu số bằng 0 trả về giá trị không xác định (NULL) thay vì trả về 0.

## Diễn giải thống kê

Phép so sánh chính của thử nghiệm A/B là tỷ lệ chuyển đổi tổng thể ở cấp độ phiên. Báo cáo thể hiện mức tăng tuyệt đối theo điểm phần trăm, mức tăng tương đối theo tỷ lệ, khoảng tin cậy 95% Newcombe-Wilson cho độ chênh lệch và kiểm định z-test gộp hai phía cho hai tỷ lệ. Kiểm định tỷ lệ mẫu (SRM) kiểm tra dựa trên giả định phân bổ 50:50. Phân tích theo phân khúc và các chỉ số cảnh báo chỉ mang tính chất thăm dò, chưa áp dụng hiệu chỉnh đa kiểm định (familywise error rate). Tính độc lập của phiên, tỷ lệ phân bổ dự kiến và việc xem trước kết quả nhiều lần chưa thể xác minh đầy đủ. Giá trị p-value nhỏ không đồng nghĩa với việc tự ý triển khai tính năng ra môi trường thực tế khi chỉ dựa trên dữ liệu mô phỏng.

## Phễu chuyển đổi & Tính tuần tự thời gian

Tỷ lệ tiếp cận giai đoạn (Stage reach) đếm số người dùng có ghi nhận sự kiện, bất kể các bước trước đó ra sao. Trong khi đó, một phễu tuần tự nghiêm ngặt (ordered funnel) đòi hỏi mỗi người dùng phải trải qua đầy đủ các bước trước đó theo đúng trình tự ngày hợp lệ và lấy lần thử sớm nhất thỏa mãn điều kiện. Cho phép các sự kiện diễn ra trong cùng một ngày. Thứ tự giai đoạn trong dữ liệu nguồn không thể tự động sửa lại mốc thời gian sự kiện. Dữ liệu hành trình có hiện tượng đảo ngược thứ tự ngày giữa các bước; việc sụt giảm người dùng trong phễu nghiêm ngặt cần được nhìn nhận như một công cụ chẩn đoán lỗi tracking/dữ liệu mô phỏng, chứ không mặc nhiên coi là khách hàng bỏ giỏ thanh toán. Bước Đăng ký (Signup) được báo cáo độc lập chứ không bắt buộc phải diễn ra sau khi mua hàng.

## Tuyên bố kinh doanh

Không coi lợi ích doanh thu dự phóng là doanh thu thực tế đã đạt được. Không suy diễn tác động nhân quả về tỷ lệ giữ chân, tồn kho hay giảm giá chỉ từ các phân khúc quan sát thuần túy. Bỏ qua phân tích RFM khách hàng vì dữ liệu thiếu mã khách hàng cố định. Các dòng bán hàng trên sàn không phải là đơn hàng hoàn chỉnh, và doanh thu ghi nhận không phải là doanh thu hoa hồng của sàn. Tỷ lệ rời bỏ (churn) là một nhãn được cung cấp sẵn, không phải chỉ số vòng đời được tái dựng độc lập. Những giới hạn này là một phần quan trọng trong câu chuyện phân tích và phỏng vấn chuyên môn.

## Phạm vi kiểm thử xác thực

Các bài kiểm thử tự động bao phủ các điều kiện biên của thống kê, giá trị tham chiếu khoảng tin cậy Wilson, tính đối xứng khi tráo đổi nhóm thử nghiệm, hợp đồng dữ liệu không hợp lệ, chính sách xử lý dòng trùng lặp, quan hệ mồ côi, xử lý thử lại theo thời gian, mẫu số bằng 0, làm tròn top 20% SKU và tính toàn vẹn của tệp nguồn/đầu ra. Toàn bộ lần chạy bổ sung thêm các bước kiểm tra cho từng dự án và đối soát độc lập các chỉ số chính, phễu tuần tự và các chỉ số nâng cao được chọn. Toàn bộ các truy vấn SQL được đặt tên đều được thực thi thực tế. Việc rà soát sổ làm việc gốc, đính chính/tính lại công thức Excel và xác thực nguồn dữ liệu Hyper được ghi nhận chi tiết tại thư mục verification/native.

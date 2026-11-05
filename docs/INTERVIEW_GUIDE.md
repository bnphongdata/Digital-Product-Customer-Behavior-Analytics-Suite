# Cẩm Nang Trao Đổi & Phỏng Vấn Chuyên Môn

## Cách giới thiệu mở đầu ngắn gọn, ấn tượng

“Mình đã xây dựng 5 dự án phân tích dữ liệu chuyên sâu xoay quanh các chủ đề: kích hoạt sản phẩm, thử nghiệm tính năng, phễu thương mại điện tử, chất lượng doanh thu sàn marketplace và hành trình người dùng. Mỗi dự án đều bắt đầu từ dữ liệu mô phỏng, kiểm tra tính toàn vẹn của dữ liệu nguồn, thực thi truy vấn trên SQLite và xuất kết quả. Mình tự động đối soát chéo các chỉ số chính bằng Python, lưu trữ mã băm dữ liệu và bằng chứng kiểm thử tự động. Điểm giá trị nhất trong quá trình làm là mình phát hiện ra nhiều điểm mà các nhận định kinh doanh ban đầu vượt quá phạm vi chứng minh của dữ liệu thực tế.”

## Cách trình bày một dự án trong 5 phút

1. Nêu rõ câu hỏi của các bên liên quan (stakeholders) và quyết định kinh doanh cần hỗ trợ.
2. Trình bày mức độ chi tiết của dữ liệu nguồn (grain), các khóa liên kết (join keys) và khung thời gian quan sát.
3. Mở một câu truy vấn SQL tiêu biểu và giải thích rõ: mẫu số của phép tính, bản số quan hệ khi kết nối bảng (join cardinality) và cách xử lý trường hợp biên (edge cases).
4. Mở tệp kết quả CSV tương ứng và các bước kiểm tra xác thực (validation checks).
5. Đưa ra phát hiện được dữ liệu hỗ trợ, đề xuất hành động tiếp theo và chỉ rõ giới hạn lớn nhất của phân tích.

## Các câu hỏi phỏng vấn thường gặp & Cách trả lời

**Tại sao bạn không xóa bỏ toàn bộ các dòng trùng lặp?**  
Dữ liệu sự kiện SaaS hoặc bán hàng trên sàn không có mã định danh sự kiện cố định (event_id hay transaction_id). Các dòng giống hệt nhau có thể là những lần người dùng lặp lại hành động đó một cách hợp lệ. Mình chọn cách giữ nguyên chúng và thống kê số lượng dòng lặp công khai, trong khi vẫn chặn đứng ngay các dòng bị trùng khóa chính ở các bảng có quy định tính duy nhất.

**Làm thế nào để bạn đảm bảo câu lệnh SQL tính toán chuẩn xác?**  
Toàn bộ truy vấn đều thực thi trực tiếp trên cơ sở dữ liệu SQLite được dựng từ các tệp CSV. Sau đó, mình dùng thư viện pandas trong Python để tính toán lại một cách độc lập từ đầu và so sánh chéo các chỉ số chính, phễu tuần tự và các thước đo nâng cao. Ngoài ra, mình viết sẵn các bài test fixture để kiểm tra các trường hợp đặc biệt như thử lại sự kiện, sự kiện bị đảo lộn thời gian, mẫu số bằng 0 hay quy tắc làm tròn số.

**Bạn đã cải tiến điều gì trong cách dựng phễu người dùng?**  
Việc chỉ đếm số lượng người dùng tại từng bước một cách độc lập không phản ánh đúng một hành trình mua sắm tuần tự hợp lệ. Mình đã bổ sung thêm điều kiện ràng buộc: người dùng phải trải qua bước trước đó rồi mới tính đến bước tiếp theo, đồng thời xét đến các lần thử lại hợp lệ. Những bất cập về mốc thời gian ghi nhận sự kiện được chỉ ra rõ ràng thay vì vội vã kết luận là khách hàng bỏ cuộc.

**Chỉ số mức tăng (lift) trong thử nghiệm A/B được hiểu như thế nào?**  
Mức tăng tuyệt đối (absolute lift) là tỷ lệ chuyển đổi của nhóm thử nghiệm trừ đi nhóm gốc; còn mức tăng tương đối (relative lift) lấy mức chênh lệch đó chia cho tỷ lệ nhóm gốc. Mình luôn báo cáo kèm theo khoảng tin cậy để thể hiện độ biến thiên, đồng thời nêu rõ các giả định về tính độc lập mà dữ liệu ở cấp độ phiên chưa thể khẳng định chắc chắn.

**Tại sao bạn không thực hiện phân tích RFM trong dự án TMĐT?**  
Dữ liệu nguồn không có mã khách hàng cố định (customer_id). Nếu lấy mã phiên truy cập (session_id) để thay thế cho khách hàng thì sẽ bóp méo hoàn toàn tần suất mua hàng và tỷ lệ giữ chân thực tế.

**Bạn xử lý ra sao nếu quy trình làm mới dữ liệu gặp lỗi?**  
Quy trình sẽ dừng ngay lập tức và hủy bỏ các bằng chứng thành công trước đó. Mình sẽ kiểm tra xem lỗi xuất phát từ vi phạm cấu trúc dữ liệu hay lệch đối soát chỉ số, làm việc với nguồn dữ liệu hoặc cập nhật lại quy tắc kinh doanh, sau đó mới chạy lại. Tuyệt đối không sửa ép dữ liệu nguồn chỉ để bài test báo vượt qua.

**Cần bổ sung những gì trước khi đưa hệ thống này vào vận hành thực tế?**  
Cần xác minh nguồn gốc dữ liệu thượng nguồn, thống nhất định nghĩa chỉ số với các bên liên quan, bổ sung mã định danh giao dịch/sự kiện thực tế, xác định khoảng thời gian theo dõi phù hợp, thiết kế phân quyền bảo mật, lên lịch chạy định kỳ và thiết lập cảnh báo giám sát. Đối với các tệp BI cũ, cần đối soát lại trên công cụ Desktop tương ứng.

## Nguyên tắc: Không nói quá về kết quả

Hãy luôn trình bày dự án đúng bản chất: đây là một portfolio phân tích dữ liệu mô phỏng có khả năng tái lập hoàn toàn. Không nhận là nhân viên chính thức của Amazon, không khẳng định đã mang lại doanh thu thực tế cho doanh nghiệp lớn hay tự nhận đã chạy các tác vụ Desktop mà mình chưa thực hiện. Hãy tự tin giải thích mạch lạc tư duy phân tích, hiểu sâu từng dòng code và sẵn sàng chỉnh sửa trực tiếp khi được yêu cầu.

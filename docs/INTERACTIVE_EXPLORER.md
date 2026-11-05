# Trình Khám Phá Dữ Liệu Tương Tác (Analytics Explorer) — Nguồn Gốc & Xác Thực

Mở [trình khám phá độc lập](../demo/analytics-explorer.html) trực tiếp trên trình duyệt của bạn sau khi tải tệp về, hoặc xem qua một trang web tĩnh hỗ trợ HTML. Ứng dụng này hoạt động **hoàn toàn ngoại tuyến (offline)**, không gọi API mạng ra ngoài, không tải thư viện JavaScript bên thứ ba và không đòi hỏi tài khoản Power BI, Tableau hay cloud.

## Trình khám phá này hiển thị những gì?

Bản demo nhúng trực tiếp dữ liệu tổng hợp từ các tệp kết quả sau:
- [Onboarding SaaS](../01_SaaS_Product_Analytics_StreamFlow/Results/onboarding_funnel.csv) — Lượng người dùng tiếp cận qua các bước onboarding theo trình tự thời gian
- [Tổng hợp thử nghiệm A/B](../02_AB_Test_Feature_Impact/Results/variant_summary.csv) — Tỷ lệ chuyển đổi quan sát được ở cấp độ phiên và các chỉ số cảnh báo rủi ro
- [Phễu thương mại điện tử](../03_Ecommerce_Product_Analytics/Results/funnel_by_segment.csv) — Tỷ lệ chuyển đổi và bỏ giỏ hàng theo thiết bị và kênh tiếp thị
- [Ngành hàng sàn marketplace](../04_Amazon_Marketplace_Analytics/Results/category_performance.csv) — Doanh thu ghi nhận và số lượng sản phẩm bán ra theo từng ngành
- [Tiếp cận hành trình người dùng](../05_User_Journey_Analytics/Results/stage_reach.csv) — Lượng người dùng tiếp cận từng bước (*chưa sắp xếp thứ tự*), không phải phễu tuần tự thời gian nghiêm ngặt

Các tệp CSV này được trích xuất từ dữ liệu mô phỏng trong portfolio và được đối soát độc lập giữa Python và SQL. **Trình khám phá này là bản chụp nhanh (snapshot) kết quả trong kho lưu trữ, không phải luồng dữ liệu thời gian thực hay sản phẩm BI gốc. Mọi giá trị biểu đồ không hợp lệ, bị thiếu hoặc không hữu hạn sẽ dừng hiển thị thay vì tự động hiển thị số 0.** Ứng dụng không hiển thị chi tiết từng dòng dữ liệu thô.

## Hướng dẫn sử dụng

1. Chọn một trong 5 dự án phân tích.
2. Chọn chỉ số đo lường (measure) phù hợp của dự án đó.
3. Tìm kiếm theo nhóm hoặc phân khúc, sau đó thay đổi thứ tự sắp xếp và số dòng muốn xem.
4. Nhấp vào liên kết tệp CSV nguồn để đối chiếu trực tiếp số liệu. Các thanh biểu đồ đều bắt đầu từ mốc 0; nhãn số giữ nguyên đơn vị gốc.
5. Đọc kỹ README của dự án, các tệp validation.json, quality.json và các giả định trước khi đưa ra nhận định kinh doanh.

## Quy trình kiểm thử & Bảo trì

Chạy lệnh `python -m unittest discover -s tests -v` từ thư mục gốc dự án. Tệp `tests/test_explorer.py` sẽ nạp chuỗi JSON được nhúng, đối chiếu toàn bộ dữ liệu tổng hợp **từng trường một** với từng tệp CSV, đảm bảo cả 5 báo cáo xác thực đều đạt kết quả PASS và kiểm tra cấu trúc giao diện offline. Nếu có tệp CSV nào thay đổi, hãy cập nhật lại dữ liệu nhúng và chạy lại các bài kiểm thử trước khi bàn giao.

Lệnh `python -m portfolio.run` sẽ làm mới toàn bộ kết quả SQL chuẩn, bằng chứng đối soát, báo cáo HTML và tệp mã băm SHA-256 manifest. Bạn nên chạy lệnh này trước khi chạy unit test nếu có thay đổi mã nguồn hoặc dữ liệu thô. Quy trình CI trên GitHub Actions sẽ tự động chạy cả hai bước này.

## Giới hạn dữ liệu & Thống kê cần lưu ý

- Kết quả dựa trên các tập dữ liệu mô phỏng, không đại diện cho hoạt động kinh doanh hay khách hàng thực tế.
- Phân tích thử nghiệm A/B dựa trên giả định các phiên độc lập và chưa xác thực đầy đủ quy trình phân bổ ngẫu nhiên hay tác động nhân quả ngoài đời thực.
- Doanh thu ghi nhận trên sàn thương mại điện tử không mặc nhiên là GMV, số lượng đơn hàng hay doanh thu hoa hồng của nền tảng.
- Tỷ lệ tiếp cận từng bước hành trình *khác* với phễu tuần tự 6 bước nghiêm ngặt; dữ liệu gốc có các mốc thời gian vi phạm thứ tự trước sau.
- Các sổ làm việc Power BI/Tableau cũ được kiểm tra riêng biệt và có thể sử dụng tập dữ liệu nguồn khác.

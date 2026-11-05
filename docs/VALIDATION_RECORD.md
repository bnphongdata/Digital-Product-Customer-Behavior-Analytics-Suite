# Hồ Sơ Kiểm Tra Xác Thực (Validation Record)

## Phân tích cốt lõi

- Năm quy trình phân tích hoàn chỉnh đã xử lý 121.366 dòng dữ liệu nguồn.
- Đã vượt qua toàn bộ 93 bước kiểm tra về dữ liệu nguồn, quan hệ bảng, thực thi truy vấn và đối soát chéo.
- Toàn bộ các bài kiểm thử tự động đều đạt kết quả PASS, bao gồm việc từ chối cờ PASS giả mạo, chỉ số bị thiếu/trùng lặp và các giá trị không hữu hạn.
- Giữ nguyên vẹn toàn bộ các tệp CSV thô ban đầu và các tệp Power BI/Tableau/hình ảnh gốc.

## Đính chính & Xác thực bảng tính Excel

- Đính chính công thức tính tỷ lệ churn SaaS để chỉ tính trên tài khoản trả phí và chuẩn hóa cờ boolean về dạng số 0/1.
- Mở rộng và định dạng lại cả 5 bảng tổng hợp kèm công thức liên kết với dữ liệu nguồn và định nghĩa rõ ràng.
- Toàn bộ 10 trang tính nguồn trong Excel đều khớp chính xác với các tệp CSV chuẩn.
- Toàn bộ 23 công thức tổng hợp đều khớp với kỳ vọng tính toán độc lập trong Artifact Tool và LibreOffice Calc.
- Cả 5 sổ làm việc đều vượt qua bài kiểm thử thay đổi giá trị ô nguồn (perturbation tests).
- Các bản sao kiểm thử trong Calc đều được xóa cache công thức trước khi mở, chứng minh rằng kết quả đến từ việc tính toán lại thực sự chứ không phải đọc giá trị lưu sẵn trong cache.
- Toàn bộ 5 bảng tổng hợp đã được kết xuất và kiểm tra trực quan.
- Không khẳng định việc thực thi trực tiếp trên ứng dụng Microsoft Excel.

## Xác thực Tableau

- Cả 3 tệp Hyper extract gốc đều được mở thành công qua công cụ của Tableau.
- Đã xây dựng 3 tệp Hyper mới đồng bộ với dữ liệu chuẩn, chứa 18 bảng dữ liệu nguồn/kết quả. Từng bảng đều được đọc lại và so sánh chi tiết từng ô.
- Các tệp extract mới này đóng vai trò là nguồn dữ liệu chuẩn, không phải dựng lại toàn bộ workbook Tableau. Chưa kiểm thử việc làm mới, kết xuất trực quan và tương tác bộ lọc trên Tableau Desktop.

## Xác thực Power BI

- Đã giải mã cả 2 tệp PBIX gốc, bao gồm các bảng dữ liệu nhúng thực tế, DAX measure, mã Power Query, lược đồ quan hệ và danh mục trang báo cáo.
- Đã tạo 19 giá trị baseline đo lường độc lập và các truy vấn kiểm tra trong DAX Query View.
- Chưa thực thi tính toán DAX, làm mới dữ liệu và nghiệm thu trực quan trên ứng dụng Power BI Desktop.

## Phát hiện trọng yếu

Cả 5 dashboard BI gốc ban đầu đều sử dụng tập dữ liệu khác với dữ liệu phân tích chuẩn của dự án. Chúng không được chứng nhận là các giao diện đã được làm mới từ các tệp CSV chuẩn. Báo cáo kiểm định phân biệt rõ sự khác nhau này với khả năng đọc dữ liệu của engine và các phép kiểm tra số học.

Xem thêm `verification/native/SUMMARY.json` để xem số lượng bằng chứng hiện tại và `verification/native/README.md` để nắm rõ quy trình tái lập và các bước tiếp theo.

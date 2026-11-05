# Trạng thái đối soát sổ làm việc (Workbook Reconciliation)

| Tầng kiểm tra (Layer) | Trạng thái | Bằng chứng kiểm tra |
| --- | --- | --- |
| Các chỉ số cốt lõi từ SQL và Python độc lập | Đạt (Passed) | Results/validation.json |
| Sửa công thức Excel & kiểm thử thay đổi ô dữ liệu nguồn | Đạt (Passed) | ../../verification/native/excel_formula_verification.json |
| Tính toán lại trên Desktop Calc | Xem bằng chứng công cụ | ../../verification/native/excel_calc_verification.json |
| Đồng bộ nguồn Power BI / Tableau gốc | Lệch (Mismatch) | ../../verification/native/workbook_audit.json |
| Thay thế nguồn Hyper (các dự án Tableau) | Đạt kiểm tra đọc dữ liệu mức ô | ../../verification/native/tableau_extract_verification.json |
| Các measure DAX của Power BI cũ | Đã cung cấp baseline & câu truy vấn; chưa chạy thực thi | ../../verification/native/ |
| Làm mới trên Power BI / Tableau Desktop & nghiệm thu trực quan | Chưa chạy | Cần cài đặt ứng dụng gốc |

Các dashboard BI cũ thực chất sử dụng nguồn dữ liệu riêng biệt. Việc tự động làm mới (refresh) không thể biến chúng khớp hoàn toàn với phân tích chuẩn vì schema dữ liệu nguồn, tập người dùng và cách định nghĩa chỉ số vốn dĩ khác nhau. Đối với Tableau, hãy tạo lại nguồn dữ liệu trực quan từ tệp `Dashboard/Validated_Analysis.hyper`; đối với Power BI, hãy nhập các bảng chuẩn thực tế và áp dụng các định nghĩa trong tệp `KPI_Lineage.md`.

Các sheet nguồn trong Excel khớp hoàn toàn với các tệp CSV sạch (clean CSV) chuẩn. Toàn bộ kỳ vọng tổng hợp, công thức tính toán, kiểm thử thay đổi dữ liệu và kết quả tính toán lại thực tế đều được lưu lại trong thư mục bằng chứng (`verification/native/`). Lưu ý LibreOffice Calc không phải là Microsoft Excel; các nhãn công cụ xử lý cần được giữ nguyên chính xác.

Đối với Power BI phiên bản cũ, các bài kiểm thử DAX được tạo ra để so sánh các measure hiện có với kỳ vọng rút ra từ chính mô hình nhúng của nó. Việc vượt qua các bài test đó sẽ xác nhận các measure chưa lọc của mô hình đó hoạt động đúng logic nội tại, chứ không đồng nghĩa với việc nó khớp hoàn toàn với các tệp CSV bên ngoài hay mọi biểu đồ đã qua lọc đều đúng tuyệt đối.

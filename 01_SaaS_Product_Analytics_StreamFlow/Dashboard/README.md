# Trạng thái Dashboard BI gốc

Tệp PBIX/TWBX ban đầu trong thư mục này sử dụng tập dữ liệu khác với dữ liệu phân tích CSV chuẩn. Dữ liệu nhúng/extract bên trong đã được rà soát kỹ lưỡng và được lưu giữ như một tài sản cũ có dữ liệu độc lập. Tệp này không được chứng nhận là giao diện đã làm mới từ `Data/clean/`.

Vui lòng xem [Báo cáo xác thực sổ làm việc gốc](../../verification/native/README.md) để biết chính xác tập mẫu dữ liệu, công thức, bằng chứng từ engine gốc và các bước kiểm tra tiếp theo trên Desktop.

Đối với các dự án Tableau, tệp `Validated_Analysis.hyper` là nguồn extract thay thế đã đồng bộ với dữ liệu chuẩn; toàn bộ 18 bảng trên cả 3 dự án đều đã được đối soát từng ô bằng Tableau Hyper API. Đây là nguồn dữ liệu chuẩn, không phải dashboard Tableau dựng sẵn hoàn chỉnh. Bạn hãy dùng từng bảng trong Results làm nguồn tổng hợp độc lập cho từng biểu đồ tương ứng; tránh kết nối bảng Results tổng hợp với bảng dữ liệu chi tiết thô.

Đối với các dự án Power BI, tệp `verification/native/<project>/verify_legacy_measures.dax` dùng để kiểm tra mô hình hiện tại so với các giá trị baseline độc lập tính từ chính dữ liệu nhúng của nó. Việc thực thi tính toán DAX và nghiệm thu trực quan trên Power BI Desktop vẫn cần được thực hiện độc lập.

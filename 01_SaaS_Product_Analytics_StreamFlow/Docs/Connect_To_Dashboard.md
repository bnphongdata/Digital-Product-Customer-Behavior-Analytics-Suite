# Hướng Dẫn Tái Lập & Kết Nối Dữ Liệu

1. Làm theo hướng dẫn ở README gốc để cài đặt môi trường Python với các phiên bản thư viện đã ghim.
2. Chạy lệnh: `python -m portfolio.run --project 01_SaaS_Product_Analytics_StreamFlow`. Nếu có thông báo lỗi, hãy dừng lại để kiểm tra.
3. Mở tệp `REPORT.html` để xem báo cáo phân tích trực quan vừa tạo.
4. Đối với Power BI hoặc Tableau, hãy nhập từng bảng riêng lẻ từ thư mục `Results/*.csv` hoặc `Data/clean/*.csv`. Sử dụng đúng mức độ chi tiết của dữ liệu nguồn; tránh các phép nối bảng nhiều-nhiều (many-to-many) làm nhân bản số liệu.
5. Tạo lại các measure dựa theo tài liệu `KPI_Lineage.md`; không cộng tổng trực tiếp các tỷ lệ phần trăm đã tính sẵn.
6. So sánh các giá trị cốt lõi, mẫu số, bộ lọc và khung thời gian với các tệp trong thư mục `Results/`. Ghi lại bằng chứng trước khi đánh dấu sổ làm việc đã được đối soát.

Cơ sở dữ liệu SQLite cục bộ được lưu tại: `build/01_SaaS_Product_Analytics_StreamFlow/analysis.sqlite`. Thư mục `build/` được cấu hình bỏ qua trên Git; quá trình chạy sẽ tự động tạo lại tệp này.

# Xác Thực Sổ Làm Việc BI Gốc (Native Workbook Verification)

Gói tài liệu và bằng chứng này phân định rạch ròi giữa **rà soát cấu trúc tệp**, **thực thi qua engine dữ liệu**, **tính toán lại công thức**, **làm mới trên ứng dụng Desktop** và **nghiệm thu trực quan**. Việc vượt qua một bước kiểm tra không đồng nghĩa với việc đã vượt qua các bước còn lại.

## Những phát hiện chính từ việc rà soát

| Tài sản BI | Dữ liệu nhúng bên trong | Mối liên hệ với dữ liệu phân tích chuẩn |
| --- | --- | --- |
| Workbook Tableau SaaS | 25.000 sự kiện StreamFlow với các trường app_open, subscribe và billing-delta | Cấu trúc bảng (schema) và tập người dùng khác với dữ liệu chuẩn users/subscriptions/events |
| Workbook Tableau A/B | 12 dòng dữ liệu thử nghiệm đã tổng hợp sẵn | Mức độ chi tiết (grain) và chu kỳ khác với 12.000 dòng phiên chuẩn |
| Workbook Power BI Ecommerce | Mô hình gồm khách hàng, đơn hàng, thanh toán, sản phẩm và phiên | Khác cấu trúc bảng và mức độ chi tiết so với web_sessions/orders chuẩn |
| Workbook Power BI Marketplace | Mô hình đa chiều với 85.000 dòng fact_orders | Khác nguồn dữ liệu so với 24.000 dòng bán hàng chuẩn |
| Workbook Tableau User Journey | 4.066 bản ghi hành trình người dùng trích xuất | Khác cấu trúc bảng và tập người dùng so với users/event-stage chuẩn |

Đây là các trường hợp **lệch nguồn dữ liệu** đã được chứng minh, chứ không đơn thuần là "chưa kịp bấm refresh". Tuyệt đối không lấy ảnh chụp màn hình dashboard cũ để minh họa cho số liệu của tệp CSV chuẩn. Các tệp BI cũ được giữ nguyên để phục vụ thanh tra, không tự ý ghi đè nhằm che giấu sự khác biệt.

## Danh mục bằng chứng bàn giao

- `original_workbook_audit.json`: Biên bản rà soát ban đầu, bao gồm công thức Excel trước khi đính chính và các trường hợp thiếu cache.
- `workbook_audit.json`: Biên bản rà soát cuối cùng về nguồn dữ liệu, bảng và công thức. Việc đọc extract Tableau sử dụng Tableau Hyper API chính hãng; metadata và dữ liệu PBIX được giải mã bằng PBIXRay.
- `excel_formula_verification.json`: Các công thức tổng hợp đã đính chính, giá trị kỳ vọng tính độc lập và bài test thay đổi ô nguồn trong Artifact Tool.
- `excel_calc_verification.json`: Bằng chứng tính toán lại độc lập bằng desktop Calc, bao gồm các tệp đã xóa cache trước khi mở. Đây không phải việc chạy trên Microsoft Excel có bản quyền.
- `tableau_extract_verification.json`: Bằng chứng đọc lại và đối soát từng ô cho toàn bộ 18 bảng trong 3 tệp `Validated_Analysis.hyper` mới.
- Các thư mục Power BI theo từng dự án: DAX trích xuất, Power Query, quan hệ, schema, kỳ vọng measure tính độc lập và truy vấn chạy thử `verify_legacy_measures.dax`. Lưu ý: việc đánh giá DAX trực tiếp trên Power BI Desktop **chưa chạy** tại đây.
- `previews/`: Hình ảnh kết xuất các trang tính tổng hợp Excel đã đính chính.

## Hướng dẫn nghiệm thu trên Power BI Desktop

1. Mở chính xác tệp PBIX gốc được định danh trong tệp baseline bằng mã băm SHA-256.
2. Dùng tính năng DAX Query View để chạy truy vấn `verify_legacy_measures.dax`. Truy vấn này đánh giá các measure của mô hình gốc so với kỳ vọng tính từ chính mô hình nhúng đó, không so sánh với tệp CSV khác nguồn.
3. Xuất bảng kết quả ra tệp CSV và chạy: `python scripts/verify_powerbi_export.py --project 03 --csv path/to/export.csv` (dùng `04` cho Marketplace). Trình xác thực sẽ tự kiểm tra số liệu, từ chối các chỉ số bị thiếu, trùng lặp hoặc mã băm PBIX không khớp.
4. Kiểm tra lược đồ quan hệ, bộ lọc báo cáo và slicer. Ghi lại các kiểm tra trực quan trên từng trang và chụp ảnh màn hình hoặc xuất PDF sau khi làm mới.
5. Nếu muốn trình bày phân tích dữ liệu CSV chuẩn trên Power BI, hãy dựng lại mô hình mới hoàn toàn từ các bảng và định nghĩa chỉ số chuẩn. Các measure cũ không thể thay thế tương đương trực tiếp.

## Hướng dẫn sử dụng nguồn dữ liệu Tableau thay thế

1. Mở tệp `Dashboard/Validated_Analysis.hyper` trong Tableau. Tệp này chứa các bảng dữ liệu thô `Source` và các bảng kết quả `Results` riêng biệt.
2. Dùng từng bảng Results như một nguồn dữ liệu tổng hợp sẵn độc lập cho biểu đồ tương ứng. Tránh kết nối bảng Results tổng hợp với bảng dữ liệu chi tiết vì sẽ làm nhân bản tổng số liệu.
3. Dựng lại các biểu đồ trực quan dựa trên tài liệu `Docs/KPI_Lineage.md`. Việc thay thế nguồn tự động vào workbook cũ là không an toàn vì cột dữ liệu và tập mẫu khác nhau.
4. Đối chiếu tổng số liệu hiển thị dưới cùng điều kiện lọc với các tệp CSV kết quả. Kiểm tra các trường tính toán, tooltip, thứ tự sắp xếp và bộ lọc.
5. Lưu thành tệp TWBX mới và chụp lại giao diện đã làm mới. Việc mở và truy vấn tệp Hyper extract chưa đồng nghĩa với việc đã nghiệm thu trực quan trên Tableau Desktop.

## Cách chạy lại các bước kiểm tra tự động

```bash
python -m pip install -r requirements.txt
python -m pip install -r verification/native/requirements.txt
python scripts/audit_native.py
python scripts/build_tableau_extracts.py
python scripts/powerbi_measure_baselines.py
python -m unittest discover -s tests -v
```

Tính năng đo lường từ xa (telemetry) của Hyper đã được tắt. Tham số `use_tcp_port=auto` là tùy chọn kết nối cục bộ được hỗ trợ. Các script này không tải dữ liệu lên mạng hay yêu cầu quyền truy cập vào các tài khoản đám mây có trong tệp workbook cũ.

## Tài liệu tham khảo công cụ

- [Cài đặt tiến trình Tableau Hyper](https://tableau.github.io/hyper-db/docs/hyper-api/hyper_process/)
- [Hướng dẫn đọc tệp Tableau Hyper](https://tableau.github.io/hyper-db/docs/guides/hyper_file/read/)
- [Thư viện trích xuất mô hình PBIXRay](https://github.com/Hugoberry/pbixray)

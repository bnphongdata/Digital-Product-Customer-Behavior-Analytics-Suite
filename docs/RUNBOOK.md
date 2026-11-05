# Cẩm Nang Tái Lập Dự Án & Xử Lý Sự Cố (Runbook)

## Thiết lập môi trường

Sử dụng Python 3.12. Mở terminal tại thư mục gốc của repository và chạy:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m portfolio.run
python -m unittest discover -s tests -v
```

Trên Windows PowerShell, kích hoạt môi trường ảo bằng lệnh: `.venv\Scripts\Activate.ps1`.

Nếu bạn chỉ muốn chạy một dự án cụ thể, hãy thêm tham số: `--project 02_AB_Test_Feature_Impact`. Nếu chạy ở thư mục khác, dùng cờ `--root /duong/dan/tuyet/doi/toi/repo`. Bạn không cần tài khoản đám mây, quyền truy cập API, máy chủ cơ sở dữ liệu ngoài hay phần mềm trả phí nào để chạy toàn bộ quy trình này.

## Các tệp kết quả đầu ra

- `Data/clean/`: Dữ liệu đã làm sạch và chuẩn hóa, được tạo lại từ các tệp dữ liệu thô ban đầu.
- `Results/*.csv`: Mỗi tệp tương ứng với một truy vấn SQL có đặt tên cụ thể.
- `Results/additional_metrics.json`: Các chỉ số thống kê thử nghiệm hoặc ước lượng bổ sung.
- `Results/quality.json`: Thống kê số lượng dòng, chẩn đoán dòng lặp, các giới hạn dữ liệu nguồn và mã băm.
- `Results/validation.json`: Danh sách các bước kiểm tra thực thi và đối soát thành công.
- `Results/query_plans.json`: Kế hoạch thực thi truy vấn SQLite cục bộ.
- `Results/manifest.json`: Mã băm SHA-256 của dữ liệu nguồn, mã phân tích và kết quả đầu ra cùng phiên bản thư viện.
- `REPORT.html`: Báo cáo phân tích trực quan độc lập, xem offline. Tải về và mở trực tiếp bằng trình duyệt trên máy.
- `build/`: Cơ sở dữ liệu SQLite cục bộ và tệp tóm tắt toàn bộ lần chạy (được cấu hình bỏ qua không commit lên Git).

## Hướng dẫn xử lý sự cố (Troubleshooting)

| Tình huống lỗi | Cách xử lý |
| --- | --- |
| Thiếu thư viện phụ thuộc | Kích hoạt lại môi trường ảo và cài đặt lại các thư viện được ghim trong requirements.txt. |
| Lỗi cấu trúc bảng / giá trị rỗng / sai kiểu | Xác định cột dữ liệu bị lỗi, kiểm tra lại thỏa thuận dữ liệu nguồn và cập nhật quy ước xử lý rõ ràng. |
| Trùng lặp khóa chính / bản ghi mồ côi | Rà soát lại logic trích xuất dữ liệu và mức độ chi tiết của quan hệ bảng. Không tự ý xóa dòng lặp một cách âm thầm. |
| Lệch số liệu giữa SQL và Python | So sánh lại phạm vi dữ liệu, bộ lọc, khung thời gian, phép nối bảng, đơn vị tính và cách xử lý giá trị NULL. |
| Lệch mã băm kết quả (checksum mismatch) | Chạy lại lệnh tạo kết quả từ mã nguồn và dữ liệu hiện tại; kiểm tra xem có tệp nào bị chỉnh sửa ngoài ý muốn không. |
| Lệch số liệu trên Dashboard BI cũ | Tham khảo Docs/Dashboard_Reconciliation.md; kiểm tra dữ liệu nhúng và bộ lọc trước khi trình bày số liệu. |

Nếu quá trình chạy gặp lỗi, bằng chứng thành công của dự án đó sẽ bị hủy để tránh hiểu nhầm. Cần chạy lại thành công hoàn chỉnh trước khi sử dụng số liệu. Bạn có thể kiểm tra tính tiền định (deterministic) bằng cách ghi lại mã băm của các tệp kết quả, chạy lại trong cùng môi trường và so sánh mã băm.

## Trình diễn giao diện trên trình duyệt

Tải tệp [trình khám phá ngoại tuyến](../demo/analytics-explorer.html) về máy và mở bằng trình duyệt. Bạn có thể chọn dự án, chỉ số và phân khúc muốn xem. Toàn bộ dữ liệu tổng hợp nhúng trong demo đều được kiểm tra đối soát với các tệp CSV kết quả bằng `tests/test_explorer.py`. Xem thêm [nguồn gốc dữ liệu và giới hạn](INTERACTIVE_EXPLORER.md).

## Đối soát tính toàn vẹn cục bộ

```bash
python -m unittest discover -s tests -v
python -m portfolio.run
python -m unittest discover -s tests -v
```

Lệnh đầu tiên kiểm tra tính toàn vẹn của mã băm SHA-256 đã lưu trước khi tạo lại; lệnh thứ hai sẽ tái lập toàn bộ kết quả; lệnh thứ ba kiểm tra lại kết quả mới sinh ra. Nếu bạn có thay đổi logic phân tích, hãy kiểm tra kỹ sự khác biệt thay vì bỏ qua các cảnh báo sai lệch.

## Tích hợp liên tục (CI)

Quy trình GitHub Actions tự động dựng lại toàn bộ các dự án, chạy kiểm thử, rà soát sai lệch kết quả số học và lưu trữ bằng chứng. Việc kiểm thử cục bộ thành công là độc lập với CI trên GitHub. Hãy đảm bảo quy trình trên GitHub báo tích xanh thành công trước khi bàn giao kết quả.

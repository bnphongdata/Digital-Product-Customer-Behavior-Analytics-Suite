# 🧪 Thử Nghiệm A/B & Đánh Giá Tác Động Của Tính Năng

### Thử Nghiệm A/B • Tối Ưu Tỷ Lệ Chuyển Đổi • Suy Diễn Thống Kê • Phân Tích Sản Phẩm

**Dự án phân tích dữ liệu end-to-end bằng SQL và Python, đánh giá hiệu quả chuyển đổi qua thử nghiệm A/B, kiểm định ý nghĩa thống kê, hành vi người dùng và hỗ trợ ra quyết định phát hành tính năng dựa trên dữ liệu thực tế.**

![Python](https://img.shields.io/badge/Python-3.12-3776AB)
![SQL](https://img.shields.io/badge/SQL-SQLite-4479A1)
![Thống Kê](https://img.shields.io/badge/Thống_Kê-Kiểm_Định_Giả_Thuyết-blueviolet)
![Khoảng Tin Cậy](https://img.shields.io/badge/Khoảng_Tin_Cậy-95%25-blue)
![Kiểm Tra Chất Lượng](https://img.shields.io/badge/Validation-20%2F20-success)
![Bộ Dữ Liệu](https://img.shields.io/badge/Dữ_Liệu-Mô_Phỏng-orange)

**Người thực hiện:** Bùi Nhất Phong  
**Dự án:** 02 — Thử Nghiệm A/B & Tác Động Tính Năng  
**Portfolio:** [Data Analyst Portfolio](../README.md)  
**LinkedIn:** [Bùi Nhất Phong](https://www.linkedin.com/in/buinhatphong/)

---

## 📌 Tóm Tắt Dự Án (Executive Summary)

Dự án này đánh giá kết quả của một thử nghiệm A/B mô phỏng so sánh giữa trải nghiệm sản phẩm hiện tại (**nhóm Control**) và một trải nghiệm cải tiến thay thế (**nhóm Variant B**).

Mục tiêu cốt lõi là xác định xem Variant B có thực sự mang lại tỷ lệ chuyển đổi phiên (session conversion rate) cao hơn hay không, lượng hóa mức độ bất định xung quanh độ chênh lệch đó thông qua các công cụ thống kê, và chỉ rõ những bằng chứng cần bổ sung trước khi một tổ chức có thể tự tin bấm nút phát hành (rollout) tính năng ra toàn bộ người dùng.

Dựa trên **12.000 dòng dữ liệu phiên truy cập mô phỏng**, kết hợp truy vấn SQL, các phép tính thống kê chuyên sâu bằng Python và quy trình đối soát độc lập, dự án làm sáng tỏ:

- Tỷ lệ chuyển đổi giữa hai nhóm thử nghiệm
- Mức tăng trưởng chuyển đổi tuyệt đối (Absolute Lift) và tương đối (Relative Lift)
- Ý nghĩa thống kê (Statistical Significance) và khoảng tin cậy 95%
- Kiểm tra cân bằng phân bổ mẫu (Sample Ratio Mismatch - SRM)
- Tỷ lệ thoát trang (Bounce Rate) và điểm tương tác của người dùng
- Doanh thu trung bình trên mỗi phiên truy cập (Revenue per Session)
- Phân tích hiệu quả theo thiết bị và kênh nguồn traffic
- Các rủi ro và giới hạn trong việc ra quyết định kinh doanh

### Kết Quả Cốt Lõi

| Chỉ số thử nghiệm | Kết quả xác thực |
|---|---:|
| 👥 Tổng số phiên truy cập | 12.000 |
| 🔵 Tỷ lệ chuyển đổi nhóm Control | 19,84% |
| 🟢 Tỷ lệ chuyển đổi nhóm Variant B | 23,08% |
| 📈 Mức tăng tuyệt đối (Absolute Lift) | +3,24 điểm phần trăm |
| 🚀 Mức tăng tương đối (Relative Lift) | +16,33% |
| 📊 Khoảng tin cậy 95% (Newcombe-Wilson) | +1,77 đến +4,71 điểm phần trăm |
| 🧪 Giá trị p-value (Kiểm định 2 phía) | 0,0000154 |
| ⚖️ Kiểm định tỷ lệ phân bổ mẫu 50:50 (SRM p-value) | 0,8124 (Không lệch) |
| ✅ Bài kiểm thử dữ liệu & logic đã vượt qua | 20/20 passed |

### Phát Hiện Quan Trọng Nhất

Phiên bản Variant B cho thấy **tỷ lệ chuyển đổi tăng 3,24 điểm phần trăm**, tương đương với mức **tăng trưởng tương đối khoảng 16,33%** so với nhóm Control.

Khoảng tin cậy 95% chưa điều chỉnh nằm hoàn toàn phía trên mốc 0 (+1,77 đến +4,71 điểm phần trăm), và kiểm định Z hai tỷ lệ cho ra giá trị p-value cực nhỏ (\(p \approx 0,0000154\)), đạt ý nghĩa thống kê dưới các giả định thử nghiệm chuẩn.

Tuy nhiên, bộ dữ liệu đầu vào chỉ ghi nhận ở mức phiên (session-level), không có mã người dùng định danh duy nhất (`user_id`), không có nhật ký cơ chế phân bổ ngẫu nhiên và thiếu các điều kiện kiểm soát chu kỳ sống thực tế.

**Kết luận của Data Analyst:** Variant B cho kết quả rất khả quan trong tập dữ liệu mô phỏng, nhưng đây là tín hiệu tích cực để tiếp tục thử nghiệm có kiểm soát chứ chưa đủ cơ sở vững chắc để phát hành đại trà ra toàn bộ sản phẩm thực tế.

> **Công bố về dữ liệu:** Case study này sử dụng dữ liệu mô phỏng phục vụ portfolio. Kết quả không đại diện cho một thử nghiệm thực tế của doanh nghiệp hay một hệ thống production ngoài đời thực.

---

## 📚 Mục Lục

1. [Bài Toán Nghiệp Vụ](#-bài-toán-nghiệp-vụ)
2. [Tổng Quan Bộ Dữ Liệu](#-tổng-quan-bộ-dữ-liệu)
3. [Bộ Công Cụ Kỹ Thuật (Tech Stack)](#-bộ-công-cụ-kỹ-thuật-tech-stack)
4. [Quy Trình Phân Tích End-to-End](#-quy-trình-phân-tích-end-to-end)
5. [Thiết Kế Thử Nghiệm & Giả Thuyết Thống Kê](#-thiết-kế-thử-nghiệm--giả-thuyết-thống-kê)
6. [Định Nghĩa KPI & Khung Đo Lường](#-định-nghĩa-kpi--khung-đo-lường)
7. [Phân Tích 1: Hiệu Quả Tỷ Lệ Chuyển Đổi](#-phân-tích-1-hiệu-quả-tỷ-lệ-chuyển-đổi)
8. [Phân Tích 2: Ý Nghĩa Thống Kê & Khoảng Tin Cậy](#-phân-tích-2-ý-nghĩa-thống-kê--khoảng-tin-cậy)
9. [Phân Tích 3: Tỷ Lệ Phân Bổ Mẫu & Kiểm Định SRM](#-phân-tích-3-tỷ-lệ-phân-bổ-mẫu--kiểm-định-srm)
10. [Phân Tích 4: Tương Tác, Doanh Thu & Chỉ Số Bảo Vệ (Guardrails)](#-phân-tích-4-tương-tác-doanh-thu--chỉ-số-bảo-vệ-guardrails)
11. [Phân Tích 5: Phân Khúc Theo Thiết Bị & Nguồn Traffic](#-phân-tích-5-phân-khúc-theo-thiết-bị--nguồn-traffic)
12. [Hiện Thực Hóa Bằng SQL](#-hiện-thực-hóa-bằng-sql)
13. [Phân Tích Thống Kê Bằng Python](#-phân-tích-thống-kê-bằng-python)
14. [Khuyến Nghị Kinh Doanh](#-khuyến-nghị-kinh-doanh)
15. [Chất Lượng Dữ Liệu & Đối Soát](#-chất-lượng-dữ-liệu--đối-soát)
16. [Tài Sản Business Intelligence & Dashboard](#-tài-sản-business-intelligence--dashboard)
17. [Cấu Trúc Thư Mục Dự Án](#-cấu-trúc-thư-mục-dự-án)
18. [Hướng Dẫn Tái Lập Phân Tích](#-hướng-dẫn-tái-lập-phân-tích)
19. [Giới Hạn Phân Tích & Hướng Phát Triển](#-giới-hạn-phân-tích--hướng-phát-triển)
20. [Đúc Kết Từ Dự Án](#-đúc-kết-từ-dự-án)

---

## 🎯 Bài Toán Nghiệp Vụ

### Bối Cảnh Doanh Nghiệp

Các đội ngũ phát triển sản phẩm kỹ thuật số liên tục thử nghiệm những tính năng mới, thay đổi giao diện, tối ưu luồng onboarding để gia tăng hành vi mong muốn và thúc đẩy doanh thu.

Tuy nhiên, việc tung ra một tính năng mới không đồng nghĩa với việc nó chắc chắn mang lại hiệu quả tốt hơn.

Sự cải thiện quan sát được trên bề mặt số liệu có thể chỉ là do biến động ngẫu nhiên (random noise), sự thiên lệch trong tập người dùng tham gia, lỗi thu thập dữ liệu hoặc sai sót trong khâu thiết kế thử nghiệm.

Doanh nghiệp cần một quy trình phân tích thử nghiệm thực sự khoa học và chặt chẽ để phân biệt giữa cải tiến thực chất với những kết luận ảo tưởng.

### Kịch Bản Thử Nghiệm

Một nền tảng kỹ thuật số đang thử nghiệm so sánh 2 phiên bản trải nghiệm:

- **Control (Nhóm đối chứng) — Trải nghiệm hiện tại:** Đóng vai trò là mốc chuẩn (baseline) để so sánh hiệu quả.
- **Variant B (Nhóm thử nghiệm) — Trải nghiệm mới:** Phiên bản cải tiến được kỳ vọng sẽ gia tăng tỷ lệ chuyển đổi của các phiên truy cập.

Dữ liệu nguồn không mô tả chi tiết tính năng cụ thể là gì (ví dụ: đổi màu nút bấm, đổi giao diện giỏ hàng hay đổi chính sách giá), do đó phân tích không tự ý gán ghép một kịch bản giao diện cụ thể.

### Câu Hỏi Nghiệp Vụ Cốt Lõi

**Liệu phiên bản Variant B có thực sự đem lại tỷ lệ chuyển đổi phiên cao hơn nhóm Control hay không, và bằng chứng thống kê ủng hộ kết luận này mạnh đến mức nào?**

### Các Câu Hỏi Bổ Trợ

1. Mức độ chênh lệch tỷ lệ chuyển đổi giữa 2 nhóm là bao nhiêu?
2. Sự khác biệt quan sát được có thực sự khác 0 một cách có ý nghĩa thống kê hay không?
3. Ước tính khoảng tin cậy của mức cải thiện nằm trong biên độ nào?
4. Quy mô mẫu giữa hai nhóm có cân bằng đúng với tỷ lệ phân bổ 50:50 như thiết kế ban đầu không?
5. Các chỉ số phụ như tỷ lệ thoát trang (bounce), điểm tương tác và doanh thu trung bình trên mỗi phiên chuyển động theo chiều hướng nào?
6. Hiệu quả chuyển đổi giữa các nhóm thiết bị và kênh nguồn traffic có đồng nhất không?
7. Những thiếu sót nào trong thiết kế dữ liệu khiến ta chưa thể lập tức cho ra mắt tính năng trên diện rộng?

---

## 🗄️ Tổng Quan Bộ Dữ Liệu

### Tóm Tắt Dữ Liệu

Dự án sử dụng 1 tệp dữ liệu CSV mô phỏng ở mức phiên truy cập, gồm đúng **12.000 bản ghi**.

| Thuộc tính | Mô tả chi tiết |
|---|---|
| Tệp dữ liệu thô | `ab_sessions_raw.csv` |
| Tệp dữ liệu sạch | `ab_sessions_clean.csv` |
| Tổng số dòng | 12.000 dòng |
| Khóa chính khai báo | `session_id` |
| Các nhóm thử nghiệm | Control và Variant B |
| Đơn vị quan sát (Grain) | Phiên truy cập (Session) |
| Độ phân giải ngày | Mức ngày (YYYY-MM-DD) |
| Tính chất dữ liệu | Dữ liệu mô phỏng phục vụ portfolio |

### Cấu Trúc Các Cột Dữ Liệu

| Tên cột | Kiểu dữ liệu | Ý nghĩa nghiệp vụ |
|---|---|---|
| `session_id` | Integer | Mã định danh duy nhất của phiên truy cập |
| `session_date` | Date | Ngày diễn ra phiên truy cập |
| `variant` | Text | Nhánh thử nghiệm: Control hoặc Variant B |
| `device` | Text | Loại thiết bị của người dùng (Desktop, Mobile, Tablet) |
| `source` | Text | Kênh nguồn traffic (Email, Organic, Paid, Referral) |
| `converted` | Binary | Cờ chuyển đổi: 1 là chuyển đổi thành công, 0 là không |
| `engagement_score` | Numeric | Điểm số tương tác mô phỏng của phiên |
| `bounce` | Binary | Cờ thoát trang ngay: 1 là thoát ngay, 0 là có tương tác tiếp |
| `revenue` | Numeric | Doanh thu phát sinh trong phiên truy cập |

### Các Đặc Điểm Quan Trọng Cần Lưu Ý

- **Mức độ chi tiết là Phiên truy cập (Session-level):** Mỗi dòng là một phiên, không phải một khách hàng cụ thể. Một khách hàng có thể ghé thăm nhiều lần và tạo ra nhiều phiên khác nhau.
- **Biến kết quả nhị phân (Binary):** `converted = 1` biểu thị phiên có hoàn thành mục tiêu chuyển đổi.
- **Kênh tiếp thị:** Hỗ trợ phân khúc đa dạng qua các kênh Email, Organic Search, Paid Ads và Referral.
- **Điểm tương tác:** Trường số liên tục mô phỏng mức độ tương tác, nhưng không có thuyết minh về thang đo chi tiết trong dữ liệu gốc.
- **Doanh thu:** Được tính theo đơn vị tiền tệ mô phỏng, không đại diện cho doanh thu kế toán thực tế.
- **Thiếu thông tin phân bổ ngẫu nhiên người dùng:** Bộ dữ liệu không có mã người dùng định danh lâu dài (`user_id`), khiến ta không thể kiểm chứng trực tiếp xem một người dùng có vô tình nhìn thấy cả hai giao diện (cross-exposure) hay không.

Tài liệu chi tiết: [📘 Từ Điển Dữ Liệu](Docs/Data_Dictionary.md) | [📂 Thư Mục Dữ Liệu Thô](Data/raw) | [📂 Thư Mục Dữ Liệu Sạch](Data/clean)

---

## 🛠️ Bộ Công Cụ Kỹ Thuật (Tech Stack)

| Hạng mục | Công nghệ | Ứng dụng thực tế |
|---|---|---|
| Ngôn ngữ lập trình | Python 3.12 | Tính toán thống kê chuyên sâu, kiểm thử tự động, đối soát chéo |
| Ngôn ngữ truy vấn | SQL | Tổng hợp dữ liệu, gom nhóm phân khúc, tính toán tỷ lệ |
| Cơ sở dữ liệu | SQLite | Thực thi truy vấn phân tích quan hệ cục bộ |
| Xử lý dữ liệu | pandas & numpy | Tính toán độc lập để đối chiếu với kết quả SQL |
| Kiểm định thống kê | Two-Proportion Z-Test | Kiểm định ý nghĩa thống kê cho hiệu số hai tỷ lệ chuyển đổi |
| Khoảng tin cậy | Newcombe-Wilson | Ước tính khoảng tin cậy 95% không đối xứng cho hiệu hai tỷ lệ |
| Chẩn đoán phân bổ mẫu | Chi-Square Goodness-of-Fit | Kiểm định phát hiện lệch tỷ lệ mẫu (SRM test) |
| Mô hình bảng tính | Excel | Kiểm tra công thức và tái lập số liệu bằng bảng tính |
| Dữ liệu BI | Tableau Hyper | Xuất tệp trích xuất Hyper chuẩn hóa phục vụ trực quan hóa |
| Đảm bảo chất lượng | Python unittest | Kiểm thử tự động từ schema đến logic thống kê |
| Bảo toàn mã nguồn | SHA-256 | Băm mã toàn vẹn truy vết dữ liệu, mã nguồn và kết quả |
| Quản lý phiên bản | Git & GitHub | Quản lý phiên bản mã nguồn dự án |

---

## 🔄 Quy Trình Phân Tích End-to-End

Dự án tuân thủ quy trình phân tích thử nghiệm khoa học gồm 8 giai đoạn:

### Giai Đoạn 1 — Xác Lập Bài Toán & Tiêu Chí Ra Quyết Định
Làm rõ câu hỏi kinh doanh, xác định nhóm đối chứng/thử nghiệm, biến kết quả chính (primary metric), các chỉ số bảo vệ (guardrail metrics) và bằng chứng cần thu thập.

### Giai Đoạn 2 — Khảo Sát & Kiểm Tra Hợp Đồng Dữ Liệu
Kiểm tra tính toàn vẹn của tệp dữ liệu thô: các cột bắt buộc, tính duy nhất của `session_id`, tính hợp lệ của nhãn nhánh thử nghiệm, giá trị nhị phân của cờ chuyển đổi/thoát trang, và khoảng giá trị của điểm tương tác, doanh thu.

### Giai Đoạn 3 — Làm Sạch & Chuẩn Hóa
Áp dụng các quy tắc chuẩn hóa dữ liệu mà không làm thay đổi bản chất dữ liệu gốc, lưu kết quả vào `Data/clean/ab_sessions_clean.csv`.

### Giai Đoạn 4 — Tổng Hợp Bằng SQL
Thực thi các câu truy vấn SQL để tính toán: quy mô mẫu từng nhóm, số lượt chuyển đổi, tỷ lệ chuyển đổi, tỷ lệ thoát trang, điểm tương tác trung bình, doanh thu trên phiên, và phân bổ theo phân khúc thiết bị/nguồn traffic.

### Giai Đoạn 5 — Suy Diễn Thống Kê Bằng Python
Sử dụng Python để tính toán: mức tăng tuyệt đối, mức tăng tương đối, khoảng tin cậy Newcombe-Wilson 95%, giá trị p-value kiểm định Z hai phía, và kiểm định Chi-Square kiểm tra lệch phân bổ mẫu (SRM).

### Giai Đoạn 6 — Đối Soát Số Liệu Độc Lập
So sánh chéo từng con số giữa kết quả tổng hợp bằng SQL với kết quả tính độc lập bằng Python, bảo đảm sự thống nhất tuyệt đối trước khi công bố.

### Giai Đoạn 7 — Diễn Giải Nghiệp Vụ & Đánh Giá Giới Hạn
Phân tích ý nghĩa kinh doanh của các con số, chỉ rõ những giả định thống kê và những rủi ro nếu vội vã triển khai khi chưa có đầy đủ thông tin về cơ chế phân bổ.

### Giai Đoạn 8 — Xuất Báo Cáo & Lưu Trữ Bằng Chứng
Tự động xuất các tệp CSV kết quả, tệp JSON chỉ số bổ trợ, báo cáo HTML trực quan độc lập và cập nhật mã băm SHA-256 trong manifest.

---

## 🧪 Thiết Kế Thử Nghiệm & Giả Thuyết Thống Kê

### Quy Mô Các Nhóm Thử Nghiệm

| Nhánh thử nghiệm | Mô tả trải nghiệm | Số phiên quan sát | Tỷ trọng |
|---|---|---:|---:|
| Control | Giao diện/trải nghiệm hiện tại | 5.987 | 49,89% |
| Variant B | Giao diện/trải nghiệm cải tiến mới | 6.013 | 50,11% |
| **Tổng cộng** | **Toàn bộ quan sát** | **12.000** | **100%** |

Số lượng phiên giữa hai nhóm rất cân bằng, nhưng chỉ riêng số lượng cân bằng chưa đủ để chứng minh quá trình ngẫu nhiên hóa ngoài đời thực diễn ra hoàn hảo.

### Biến Kết Quả Chính (Primary Metric)

**Tỷ lệ chuyển đổi phiên (Session Conversion Rate):** Tỷ lệ phần trăm số phiên ghi nhận có hành động chuyển đổi thành công trên tổng số phiên của nhóm đó.

### Giả Thuyết Thống Kê

Gọi:
- \(p_C\): Xác suất chuyển đổi thực sự của nhóm Control
- \(p_B\): Xác suất chuyển đổi thực sự của nhóm Variant B

**Giả thuyết Không (Null Hypothesis - \(H_0\)):**
Không có sự khác biệt về xác suất chuyển đổi giữa hai phiên bản:
\[
H_0: p_B - p_C = 0
\]

**Giả thuyết Đối (Alternative Hypothesis - \(H_1\)):**
Có sự khác biệt về xác suất chuyển đổi giữa hai phiên bản (kiểm định hai phía):
\[
H_1: p_B - p_C \neq 0
\]

Phân tích chọn **kiểm định hai phía (two-sided)** thay vì một phía để giữ sự khách quan khoa học, không mặc định trước rằng phiên bản mới chắc chắn sẽ tốt hơn.

### Ngưỡng Ý Nghĩa Thống Kê

Sử dụng mức ý nghĩa quy chuẩn phổ biến trong ngành:
\[
\alpha = 0,05
\]
Tương ứng với mức độ tin cậy không điều chỉnh là 95%.

---

## 📐 Định Nghĩa KPI & Khung Đo Lường

| Chỉ số | Công thức tính | Ý nghĩa nghiệp vụ |
|---|---|---|
| Phiên (Sessions) | Đếm số quan sát trong nhóm | Quy mô mẫu thử nghiệm |
| Lượt chuyển đổi (Conversions) | Tổng số cờ chuyển đổi dương (`SUM(converted)`) | Số phiên thành công ghi nhận được |
| Tỷ lệ chuyển đổi (Conversion Rate) | Lượt chuyển đổi ÷ Tổng số phiên | KPI đánh giá hiệu quả cốt lõi |
| Mức tăng tuyệt đối (Absolute Lift) | Tỷ lệ Variant B − Tỷ lệ Control | Chênh lệch tính theo điểm phần trăm |
| Mức tăng tương đối (Relative Lift) | Mức tăng tuyệt đối ÷ Tỷ lệ Control | Tỷ lệ phần trăm cải thiện so với mốc chuẩn |
| Tỷ lệ thoát trang (Bounce Rate) | Số phiên bounce ÷ Tổng số phiên | Chỉ báo phản ánh trải nghiệm người dùng ban đầu |
| Điểm tương tác trung bình | Trung bình cộng của `engagement_score` | Mức độ gắn kết với sản phẩm |
| Doanh thu trên mỗi phiên | Tổng doanh thu ÷ Tổng số phiên | Chỉ số hiệu quả thương mại trên lượng traffic |
| Khoảng tin cậy (Confidence Interval) | Ước tính khoảng cho \(p_B - p_C\) ở mức 95% | Biên độ bất định của mức chênh lệch |
| Giá trị p-value | Xác suất quan sát thấy độ lệch lớn như vậy nếu \(H_0\) đúng | Bằng chứng bác bỏ giả thuyết không |
| Kiểm định SRM p-value | Kiểm định Chi-Square so với tỷ lệ phân bổ kỳ vọng 50:50 | Phát hiện sự cố phân bổ mẫu bất thường |

Chi tiết quy tắc: [Nguồn Gốc KPI (KPI Lineage)](Docs/KPI_Lineage.md)

---

## 📈 Phân Tích 1: Hiệu Quả Tỷ Lệ Chuyển Đổi

### Câu Hỏi Nghiệp Vụ

Liệu phiên bản Variant B có đem lại tỷ lệ phiên chuyển đổi cao hơn nhóm Control hay không?

### Kết Quả Đối Soát

| Chỉ số | Nhóm Control | Nhóm Variant B |
|---|---:|---:|
| Số phiên truy cập | 5.987 | 6.013 |
| Số phiên chuyển đổi | 1.188 | 1.388 |
| Tỷ lệ chuyển đổi | 19,84% | 23,08% |
| Số phiên không chuyển đổi | 4.799 | 4.625 |

### Phát Hiện 1 — Variant B Đạt Tỷ Lệ Chuyển Đổi Vượt Trội

Nhóm Control đạt tỷ lệ chuyển đổi khoảng **19,84%**, trong khi nhóm Variant B đạt **23,08%**.

Sự khác biệt là dương và rất rõ ràng trong tập dữ liệu phiên được cung cấp.

### Phát Hiện 2 — Lượng Hóa Mức Tăng Tuyệt Đối (Absolute Lift)

Mức tăng tuyệt đối đo lường trực tiếp độ chênh lệch giữa hai tỷ lệ xác suất:
\[
\text{Absolute Lift} = p_B - p_C = 0,230833 - 0,198430 = +0,032403
\]
**Mức tăng tuyệt đối: +3,24 điểm phần trăm (percentage points).**

*Lưu ý quan trọng:* Đây là chênh lệch giữa hai tỷ lệ phần trăm (điểm phần trăm), không phải mức tăng 3,24%.

### Phát Hiện 3 — Lượng Hóa Mức Tăng Tương Đối (Relative Lift)

Mức tăng tương đối so sánh mức tăng tuyệt đối với mốc cơ sở của nhóm Control:
\[
\text{Relative Lift} = \frac{p_B - p_C}{p_C} = \frac{0,032403}{0,198430} \approx +16,33\%
\]
**Mức tăng tương đối: +16,33%.**

### Diễn Giải Nghiệp Vụ

Xét thuần túy trên tập dữ liệu quan sát được, Variant B cho thấy hiệu quả chuyển đổi vượt trội hơn hẳn so với Control, tạo động lực rất lớn để đào sâu phân tích thống kê.

Tuy nhiên, con số này chỉ mô tả những gì đã diễn ra trong tệp dữ liệu, chứ chưa độc lập chứng minh rằng tính năng mới là nguyên nhân trực tiếp thúc đẩy hành vi người dùng ngoài đời thực.

**Bằng chứng truy vấn:** [Tóm tắt nhánh thử nghiệm (variant_summary.csv)](Results/variant_summary.csv)

---

## 📊 Phân Tích 2: Ý Nghĩa Thống Kê & Khoảng Tin Cậy

### Câu Hỏi Nghiệp Vụ

Mức độ bất định thống kê xung quanh độ chênh lệch chuyển đổi này là bao nhiêu?

### Kiểm Định Giả Thuyết

Áp dụng kiểm định Z hai tỷ lệ gộp (two-sided pooled two-proportion z-test) để kiểm tra xem liệu sự chênh lệch có phải do ngẫu nhiên hay không.

### Kết Quả Kiểm Định Thống Kê

| Chỉ số thống kê | Kết quả tính toán |
|---|---:|
| Chênh lệch tuyệt đối | +0,032403 (+3,24 điểm %) |
| Mức tăng tương đối | +16,33% |
| Giá trị p-value (hai phía) | 0,0000154243 (\(\approx 1,54 \times 10^{-5}\)) |
| Mức độ tin cậy | 95% |
| Cận dưới khoảng tin cậy | +1,77 điểm phần trăm (+0,0177) |
| Cận trên khoảng tin cậy | +4,71 điểm phần trăm (+0,0471) |

### Phát Hiện 1 — Giá Trị p-value Rất Nhỏ

Giá trị p-value quan sát được xấp xỉ \(0,0000154\), nhỏ hơn rất nhiều so với ngưỡng quy ước \(\alpha = 0,05\).

**Ý nghĩa thống kê:** Dữ liệu quan sát được mâu thuẫn rất mạnh với giả thuyết không (cho rằng hai nhóm có tỷ lệ chuyển đổi bằng nhau) dưới các giả định của mô hình kiểm định.

Cần lưu ý: p-value không phải là xác suất giả thuyết không đúng, và nó cũng không thể chứng minh việc phân bổ mẫu ngoài đời có bị thiên lệch hay không.

### Phát Hiện 2 — Khoảng Tin Cậy Nằm Hoàn Toàn Phía Dương

Sử dụng phương pháp Newcombe (dựa trên khoảng điểm số Wilson) cho hiệu số hai tỷ lệ độc lập:

**Khoảng tin cậy 95%: từ +1,77 đến +4,71 điểm phần trăm.**

Toàn bộ khoảng tin cậy đều lớn hơn 0 và cận dưới đạt +1,77 điểm phần trăm. Điều này khẳng định rằng dưới mô hình các phép thử độc lập, mức chênh lệch dương là rất đáng tin cậy.

### Phát Hiện 3 — Ý Nghĩa Thống Kê vs. Ý Nghĩa Kinh Doanh

Một kết quả đạt "ý nghĩa thống kê" (statistical significance) chỉ cho biết sự khác biệt khó có thể do ngẫu nhiên gây ra, chứ chưa khẳng định tính năng đó mang lại hiệu quả kinh doanh đáng giá.

Để đưa ra quyết định kinh doanh cuối cùng, ban lãnh đạo còn cần xem xét:
- Mức tăng tối thiểu có ý nghĩa kinh tế (Minimum Detectable Effect / MDE)
- Chi phí phát triển, vận hành và hạ tầng của tính năng mới
- Tác động lên độ ổn định kỹ thuật của sản phẩm
- Tác động đến sự hài lòng lâu dài và tỷ lệ giữ chân khách hàng

**Bằng chứng thống kê:** [Chỉ số thống kê chi tiết (additional_metrics.json)](Results/additional_metrics.json)

---

## ⚖️ Phân Tích 3: Tỷ Lệ Phân Bổ Mẫu & Kiểm Định SRM

### Câu Hỏi Nghiệp Vụ

Tỷ lệ phân chia người dùng giữa hai nhóm có bị lệch bất thường so với thiết kế 50:50 ban đầu hay không?

### Phân Bổ Mẫu Quan Sát Được

| Nhóm | Số phiên thực tế | Tỷ lệ thực tế |
|---|---:|---:|
| Control | 5.987 | 49,89% |
| Variant B | 6.013 | 50,11% |
| **Tổng cộng** | **12.000** | **100%** |

### Số Lượng Kỳ Vọng Theo Thiết Kế 50:50

Với tổng số 12.000 phiên, mỗi nhóm kỳ vọng nhận đúng 6.000 phiên.

### Kiểm Định Chẩn Đoán Lệch Phân Bổ (SRM Test)

Sử dụng kiểm định độ phù hợp Chi-Square (Chi-square goodness-of-fit test) để kiểm tra xem độ chênh lệch 26 phiên (5.987 vs 6.013) có dấu hiệu bất thường hay không:

**Kết quả kiểm định SRM: p-value = 0,8124.**

### Diễn Giải Kết Quả

Giá trị p-value rất lớn (0,8124) cho thấy số lượng mẫu hoàn toàn phù hợp với giả định phân bổ đều 50:50. Không có bất kỳ dấu hiệu nào của hiện tượng lệch phân bổ mẫu (Sample Ratio Mismatch).

Tuy nhiên, cần nhớ rằng: **Kiểm định SRM đạt không đồng nghĩa với việc quá trình ngẫu nhiên hóa ngoài đời thực đã diễn ra đúng chuẩn.** Nếu hệ thống phân bổ bị lỗi khiến một người dùng bị gán vào cả hai nhóm tại các thời điểm khác nhau, kiểm định SRM trên mức phiên cũng không thể phát hiện ra.

---

## 💼 Phân Tích 4: Tương Tác, Doanh Thu & Chỉ Số Bảo Vệ (Guardrails)

Một phân tích A/B toàn diện không bao giờ chỉ nhìn vào một chỉ số chuyển đổi duy nhất mà phải theo dõi các chỉ số trải nghiệm và tài chính đi kèm để tránh tình trạng "tối ưu cục bộ gây hại tổng thể".

### So Sánh Các Chỉ Số Phụ Trợ

| Chỉ số | Nhóm Control | Nhóm Variant B | Chênh lệch quan sát |
|---|---:|---:|---:|
| Tỷ lệ thoát trang (Bounce Rate) | 43,33% | 38,18% | Giảm 5,14 điểm phần trăm |
| Điểm tương tác trung bình | 53,00 | 60,29 | Tăng 7,29 điểm |
| Tổng doanh thu ghi nhận | 49.719,70 | 58.527,50 | Tăng 8.807,80 |
| Doanh thu trung bình trên phiên | 8,30 | 9,73 | Tăng 1,43 đơn vị tiền tệ |

### Phát Hiện 1 — Tỷ Lệ Thoát Trang Giảm Đáng Kể

Nhóm Variant B có tỷ lệ thoát trang thấp hơn khoảng **5,14 điểm phần trăm** so với Control (38,18% so với 43,33%).

Điều này cho thấy giao diện mới không chỉ kích thích chuyển đổi mà dường như còn giúp giữ chân người dùng khám phá sâu hơn trong phiên truy cập.

### Phát Hiện 2 — Điểm Tương Tác Tăng Cao Hơn

Điểm tương tác trung bình của Variant B đạt 60,29 điểm, cao hơn mức 53,00 điểm của Control. Đây là tín hiệu mô tả tích cực, dù thang đo cụ thể không được thuyết minh chi tiết trong dữ liệu nguồn.

### Phát Hiện 3 — Doanh Thu Trên Mỗi Phiên Tăng Trưởng

Doanh thu bình quân mỗi phiên tăng từ 8,30 lên 9,73 đơn vị tiền tệ (tăng khoảng 1,43 đơn vị/phiên).

Đây là tín hiệu thương mại rất đáng khích lệ. Tuy nhiên, phân tích không thực hiện kiểm định nhân quả riêng cho doanh thu vì dữ liệu không cung cấp phân phối chi tiết của giá trị đơn hàng.

### Tổng Hợp Chỉ Số Bảo Vệ (Guardrail Summary)

| Chỉ số | Xu hướng quan sát | Đánh giá nghiệp vụ |
|---|---|---|
| Tỷ lệ chuyển đổi | Tăng mạnh ở Variant B | Chỉ số mục tiêu chính đạt kết quả rất tốt |
| Tỷ lệ thoát trang | Giảm ở Variant B | Chỉ số bảo vệ trải nghiệm chuyển động tích cực |
| Điểm tương tác | Tăng ở Variant B | Tín hiệu tương tác khả quan |
| Doanh thu / Phiên | Tăng ở Variant B | Tín hiệu tài chính tích cực |

**Bằng chứng truy vấn:** [Tóm tắt nhánh thử nghiệm (variant_summary.csv)](Results/variant_summary.csv)

---

## 📱 Phân Tích 5: Phân Khúc Theo Thiết Bị & Nguồn Traffic

### Câu Hỏi Nghiệp Vụ

Liệu mức tăng chuyển đổi của Variant B có đồng đều trên tất cả các loại thiết bị và kênh tiếp thị hay chỉ tập trung ở một vài nhóm đặc thù?

### Kết Quả Một Số Phân Khúc Tiêu Biểu

| Phân khúc khảo sát | Tỷ lệ chuyển đổi Control | Tỷ lệ chuyển đổi Variant B |
|---|---:|---:|
| Máy tính (Desktop) — Kênh Email | 18,54% | 22,00% |
| Máy tính (Desktop) — Kênh Tìm kiếm tự nhiên (Organic) | 21,27% | 24,53% |
| Máy tính (Desktop) — Kênh Quảng cáo trả phí (Paid) | 18,43% | 23,88% |
| Máy tính (Desktop) — Kênh Giới thiệu (Referral) | 20,00% | 24,73% |
| Di động (Mobile) — Kênh Email | 19,67% | 23,36% |

### Phát Hiện 1 — Xu Hướng Tích Cực Xuất Hiện Đồng Đều

Trên tất cả các phân khúc tiêu biểu, Variant B đều ghi nhận tỷ lệ chuyển đổi cao hơn Control.

Điều này cho thấy tính ưu việt của giao diện mới không bị bó hẹp trong một loại màn hình hay một tệp khách hàng cá biệt nào.

### Cảnh Báo Về Mặt Phương Pháp Luận Khi Đào Sâu Phân Khúc

Mặc dù các phân khúc đều cho thấy kết quả khả quan, một chuyên viên phân tích dữ liệu chuyên nghiệp cần hết sức cảnh giác với **vấn đề kiểm định đa biến (multiple testing problem)**. Khi chia nhỏ dữ liệu thành quá nhiều nhóm, xác suất gặp phải sai lầm loại I (False Positive) sẽ tăng vọt nếu không áp dụng các phương pháp hiệu chỉnh (như Bonferroni hay FDR).

Do đó, các kết quả phân khúc ở đây nên được coi là tài liệu gợi ý giả thuyết cho các đợt thử nghiệm tương lai, chứ không nên coi là hiệu ứng đã được chứng minh riêng lẻ cho từng nhóm nhỏ.

**Bằng chứng trích xuất:** [Kết quả phân khúc chi tiết (segment_conversion.csv)](Results/segment_conversion.csv)

---

## 💻 Hiện Thực Hóa Bằng SQL

Tất cả các con số tổng hợp trong dự án đều được xuất phát từ các truy vấn SQL chuẩn, chạy trực tiếp trên cơ sở dữ liệu SQLite:

### Truy Vấn 1 — Tổng Hợp Hiệu Quả Hai Nhánh Thử Nghiệm

```sql
SELECT
    variant,
    COUNT(*) AS sessions,
    SUM(converted) AS conversions,
    AVG(1.0 * converted) AS conversion_rate,
    AVG(1.0 * bounce) AS bounce_rate,
    AVG(engagement_score) AS mean_engagement,
    SUM(revenue) AS revenue,
    AVG(revenue) AS revenue_per_session

FROM ab_sessions_clean

GROUP BY variant

ORDER BY variant;
```

**Kỹ thuật SQL áp dụng:**
- Ép kiểu `1.0 *` khi tính trung bình biến nhị phân để có tỷ lệ chính xác
- Gom nhóm theo nhánh `variant` để so sánh trực tiếp
- Tính toán đồng thời cả biến mục tiêu, biến tương tác và biến doanh thu

### Truy Vấn 2 — Phân Tích Chuyển Đổi Theo Thiết Bị & Kênh Traffic

```sql
SELECT
    device,
    source,
    variant,
    COUNT(*) AS sessions,
    SUM(converted) AS conversions,
    AVG(1.0 * converted) AS conversion_rate

FROM ab_sessions_clean

GROUP BY
    device,
    source,
    variant

ORDER BY
    device,
    source,
    variant;
```

**Kỹ thuật SQL áp dụng:**
- Gom nhóm đa chiều (`GROUP BY device, source, variant`)
- Đo lường quy mô mẫu và tỷ lệ chuyển đổi cho từng lát cắt nghiệp vụ

### Truy Vấn 3 — Theo Dõi Phân Bổ Mẫu Theo Từng Ngày

```sql
SELECT
    session_date,
    variant,
    COUNT(*) AS sessions,
    SUM(converted) AS conversions

FROM ab_sessions_clean

GROUP BY
    session_date,
    variant

ORDER BY
    session_date,
    variant;
```

**Kỹ thuật SQL áp dụng:**
- Theo dõi chuỗi thời gian phân bổ mẫu theo ngày
- Giúp phát hiện sớm các sự cố sụt giảm lưu lượng hoặc phân bổ lệch đột ngột trong quá trình thử nghiệm

**Xem toàn bộ mã nguồn SQL:** [SQL/analysis.sql](SQL/analysis.sql)

---

## 🐍 Phân Tích Thống Kê Bằng Python

Python chịu trách nhiệm thực thi các phép suy diễn thống kê chuẩn xác và đối soát chéo số liệu:

### Các Công Thức Thống Kê Chính

**1. Xác suất chuyển đổi:**
\[
p = \frac{\text{Conversions}}{\text{Sessions}}
\]

**2. Mức tăng tuyệt đối (Absolute Lift):**
\[
\Delta = p_B - p_C
\]

**3. Mức tăng tương đối (Relative Lift):**
\[
L = \frac{p_B - p_C}{p_C}
\]

**4. Tỷ lệ gộp dưới giả thuyết không:**
\[
\hat p = \frac{x_B + x_C}{n_B + n_C}
\]

**5. Giá trị thống kê kiểm định Z hai tỷ lệ:**
\[
z = \frac{p_B - p_C}{\sqrt{\hat p(1 - \hat p)\left(\frac{1}{n_B} + \frac{1}{n_C}\right)}}
\]

### Phương Pháp Khoảng Tin Cậy Newcombe-Wilson

Dự án không sử dụng khoảng tin cậy đối xứng đơn giản (dễ bị lệch khi tỷ lệ gần 0 hoặc 1) mà áp dụng phương pháp Newcombe-Wilson. Phương pháp này kết hợp khoảng tin cậy điểm số Wilson của từng nhóm riêng lẻ để tạo ra khoảng tin cậy không đối xứng có độ chính xác cao cho hiệu số hai tỷ lệ.

### Đối Soát Số Liệu Độc Lập

Mã nguồn Python độc lập đọc dữ liệu từ tệp CSV sạch, tính toán lại toàn bộ các chỉ số và so sánh từng chữ số thập phân với kết quả xuất ra từ câu lệnh SQL. Quy trình này triệt tiêu hoàn toàn nguy cơ sai lệch số liệu báo cáo do lỗi viết code.

---

## 💡 Khuyến Nghị Kinh Doanh

### Bảng Đánh Giá Quyết Định

| Tiêu chí xem xét | Đánh giá thực tế | Kết luận hành động |
|---|---|---|
| Kết quả chuyển đổi chính | Tăng vượt trội (+3,24 điểm %) | Tín hiệu cực kỳ hứa hẹn |
| Bằng chứng thống kê | p-value rất nhỏ (\(1,54 \times 10^{-5}\)) | Bác bỏ giả thuyết không theo mô hình |
| Khoảng tin cậy 95% | Toàn bộ nằm trên mốc dương (+1,77 đến +4,71 điểm %) | Biên độ tăng trưởng đáng tin cậy |
| Cân bằng tỷ lệ mẫu | Kiểm định SRM p-value = 0,8124 | Không phát hiện lệch phân bổ |
| Chỉ số phụ & Bảo vệ | Thoát trang giảm, tương tác và doanh thu tăng | Không có dấu hiệu tổn hại chỉ số phụ |
| Xác thực cơ chế phân bổ | Chưa có log phân bổ người dùng | Cần thu thập bổ sung |
| Độc lập giữa các quan sát | Mức phiên (session), chưa xác thực mức người dùng | Chưa đủ điều kiện chứng minh nhân quả tuyệt đối |
| **Quyết định ra mắt toàn diện** | **Chưa cấp phép phát hành ngay lập tức** | **Triển khai thử nghiệm có kiểm soát tiếp theo** |

### 5 Khuyến Nghị Hành Động Cụ Thể

1. **Khuyến nghị 1 (Ưu tiên cao) — Xác thực đơn vị ngẫu nhiên hóa:** Kiểm tra xem hệ thống phân bổ thử nghiệm hoạt động ở mức người dùng (`user_id`) hay mức phiên (`session_id`). Nếu người dùng quay lại nhiều lần mà bị đổi giao diện liên tục, kết quả sẽ bị nhiễu.
2. **Khuyến nghị 2 (Ưu tiên cao) — Chuẩn hóa định nghĩa chuyển đổi:** Xác nhận rõ sự kiện chuyển đổi được định nghĩa và gắn thẻ đồng nhất ở cả hai nhóm.
3. **Khuyến nghị 3 (Ưu tiên cao) — Thiết lập chỉ số bảo vệ chính thức:** Đưa tỷ lệ thoát trang và doanh thu trên mỗi phiên vào danh sách chỉ số bảo vệ chính thức cho các đợt thử nghiệm sau.
4. **Khuyến nghị 4 (Ưu tiên trung bình) — Đăng ký trước các giả thuyết phân khúc:** Nếu muốn kiểm tra xem tính năng mới có hiệu quả vượt trội trên Mobile hay Desktop, hãy đăng ký trước giả thuyết này trước khi chạy test để tránh thiên lệch nhận thức.
5. **Khuyến nghị 5 (Ưu tiên trung bình) — Triển khai phát hành từng phần (Phased Rollout):** Khi tiến hành thử nghiệm trên môi trường thật, hãy phát hành theo lộ trình tăng dần (10% → 25% → 50% → 100%) kèm theo hệ thống giám sát cảnh báo lỗi kỹ thuật tự động.

### Lộ Trình 30 / 60 / 90 Ngày

- **Ngày 1–30 (Chuẩn bị & Rà soát):** Kiểm toán hệ thống tracking sự kiện, thiết lập mã định danh người dùng ổn định, xác định rõ ngưỡng MDE và chỉ số bảo vệ.
- **Ngày 31–60 (Thực thi thử nghiệm chuẩn):** Chạy thử nghiệm A/B trên môi trường thật với kích thước mẫu được tính toán trước, kiểm soát thời gian chạy đủ chu kỳ kinh doanh (tối thiểu 2 tuần).
- **Ngày 61–90 (Đánh giá & Ra mắt):** Phân tích kết quả cuối cùng, kiểm tra khoảng tin cậy, đánh giá chỉ số bảo vệ và tiến hành phát hành toàn diện nếu các tiêu chuẩn đều đạt.

---

## ✅ Chất Lượng Dữ Liệu & Đối Soát

Bộ kiểm thử tự động của dự án bao gồm 20 bài kiểm tra độc lập, bao quát từ tính hợp lệ của hợp đồng dữ liệu đến sự khớp nối của từng phép tính thống kê.

### Tóm Tắt Kiểm Tra Chất Lượng

| Tiêu chí | Kết quả ghi nhận |
|---|---:|
| Số dòng dữ liệu thô | 12.000 dòng |
| Số dòng dữ liệu sạch | 12.000 dòng |
| Số ô dữ liệu bắt buộc bị thiếu | 0 ô |
| Dòng dữ liệu trùng lặp nguyên bản | 0 dòng |
| Khóa chính khai báo | `session_id` (duy nhất 100%) |
| Số nhánh thử nghiệm | Đúng 2 nhánh (Control và Variant B) |
| Số bài kiểm thử tự động vượt qua | 20/20 passed |

**Lưu ý quan trọng về ngữ nghĩa dữ liệu:**
Báo cáo chất lượng dữ liệu ghi nhận cảnh báo rằng toàn bộ 12.000 dòng dữ liệu phiên đều chịu ảnh hưởng của việc thiếu ngữ cảnh mã người dùng (`user_id`). Điều này không có nghĩa là dữ liệu bị sai định dạng kỹ thuật, mà mang ý nghĩa cảnh báo phương pháp luận: giả định về tính độc lập hoàn toàn giữa các phiên truy cập chưa thể kiểm chứng độc lập nếu thiếu mã định danh người dùng.

**Các tệp kết quả kiểm thử:**
- [validation.json](Results/validation.json) — Biên bản kiểm thử kỹ thuật và đối soát số liệu
- [quality.json](Results/quality.json) — Báo cáo chất lượng và giới hạn ngữ nghĩa dữ liệu
- [manifest.json](Results/manifest.json) — Mã băm cryptographic SHA-256

---

## 📊 Tài Sản Business Intelligence & Dashboard

| Tài sản | Mục đích | Đường dẫn |
|---|---|---|
| Mô hình bảng tính Excel | Sổ làm việc đối soát công thức phân tích | [Excel Workbook](Excel/02_AB_Test_Feature_Impact_Model.xlsx) |
| Dashboard Tableau cũ | Lưu trữ dashboard gốc để tham khảo | [Thư mục Dashboard](Dashboard/) |
| Tệp trích xuất Hyper chuẩn hóa | Dữ liệu nguồn chuẩn hóa phục vụ tạo lại visual | [Validated_Analysis.hyper](Dashboard/Validated_Analysis.hyper) |
| Ảnh chụp Dashboard | Hình ảnh tham khảo giao diện visual cũ | [Thư mục Images](Images/) |
| Báo cáo HTML độc lập | Báo cáo phân tích tương tác ngoại tuyến hoàn chỉnh | [REPORT.html](REPORT.html) |

### Trạng Thái Đối Soát Dashboard Tableau Gốc

Rà soát kỹ thuật cho thấy dashboard Tableau gốc sử dụng **12 dòng dữ liệu tổng hợp**, trong khi phân tích chuẩn mực dựa trên **12.000 bản ghi chi tiết mức phiên**. Do khác biệt về mức độ chi tiết và cấu trúc dữ liệu, ảnh chụp dashboard cũ được lưu giữ làm tư liệu tham khảo chứ không đại diện cho các giá trị KPI chuẩn. Tệp `Validated_Analysis.hyper` đã được tạo sẵn để sẵn sàng cho việc làm mới visual trực tiếp trên Tableau Desktop.

Xem chi tiết: [Biên Bản Đối Soát Dashboard](Docs/Dashboard_Reconciliation.md) | [Ánh Xạ Trường Lên Visual](Docs/Dashboard_Field_Mapping.md) | [Hướng Dẫn Kết Nối](Docs/Connect_To_Dashboard.md)

---

## 📂 Cấu Trúc Thư Mục Dự Án

```text
02_AB_Test_Feature_Impact/
│
├── Data/
│   ├── raw/
│   │   └── ab_sessions_raw.csv           # Dữ liệu CSV thô ban đầu (12.000 dòng)
│   └── clean/
│       └── ab_sessions_clean.csv         # Dữ liệu CSV sạch chuẩn hóa
│
├── SQL/
│   ├── analysis.sql                      # Các truy vấn SQL phân tích chính
│   └── advanced_queries.sql              # Các truy vấn SQL mở rộng
│
├── Python/
│   └── analysis.py                       # Điểm khởi chạy phân tích Python
│
├── Excel/
│   └── 02_AB_Test_Feature_Impact_Model.xlsx # Sổ tính toán đối soát công thức
│
├── Dashboard/
│   ├── README.md                         # Hướng dẫn tái lập dashboard
│   ├── Validated_Analysis.hyper          # Tệp trích xuất Hyper chuẩn hóa
│   └── Experiment _ A-B Test...twbx      # Tệp Tableau nguyên bản
│
├── Images/
│   └── Experiment _ A-B Test...png       # Ảnh chụp dashboard gốc
│
├── Results/
│   ├── variant_summary.csv               # Tóm tắt hiệu quả 2 nhóm thử nghiệm
│   ├── segment_conversion.csv            # Hiệu quả chuyển đổi theo phân khúc
│   ├── daily_assignment.csv              # Phân bổ mẫu và chuyển đổi theo ngày
│   ├── additional_metrics.json           # Các chỉ số thống kê (Lift, CI, p-value, SRM)
│   ├── quality.json                      # Báo cáo chất lượng dữ liệu
│   ├── validation.json                   # Kết quả kiểm thử tự động
│   ├── query_plans.json                  # Kế hoạch thực thi truy vấn SQLite
│   └── manifest.json                     # Mã băm SHA-256 toàn vẹn
│
├── Docs/
│   ├── Data_Dictionary.md                # Từ điển dữ liệu nguồn
│   ├── KPI_Lineage.md                    # Nguồn gốc KPI và công thức tính
│   ├── Dashboard_Reconciliation.md       # Trạng thái đối soát sổ làm việc
│   ├── Dashboard_Field_Mapping.md        # Ánh xạ trường dữ liệu lên visual
│   └── Connect_To_Dashboard.md           # Hướng dẫn kết nối dữ liệu
│
├── REPORT.html                           # Báo cáo phân tích trực quan ngoại tuyến
└── README.md                             # Tài liệu case study chi tiết này
```

---

## ▶️ Hướng Dẫn Tái Lập Phân Tích

Bạn có thể tự mình chạy lại toàn bộ quy trình phân tích thử nghiệm này với các bước sau:

### Yêu Cầu Môi Trường

- Python 3.12 trở lên
- Git
- Quyền cài đặt gói thư viện Python qua `pip`

### Bước 1 — Sao Chép Kho Mã Nguồn

```bash
git clone https://github.com/buinhatphong/digital-product-analytics-portfolio.git
cd digital-product-analytics-portfolio
```

### Bước 2 — Tạo Môi Trường Ảo

```bash
python -m venv .venv
```

Kích hoạt môi trường ảo:
- Trên Windows PowerShell:
  ```powershell
  .venv\Scripts\Activate.ps1
  ```
- Trên macOS / Linux:
  ```bash
  source .venv/bin/activate
  ```

### Bước 3 — Cài Đặt Thư Viện Cần Thiết

```bash
python -m pip install -r requirements.txt
```

### Bước 4 — Thực Thi Phân Tích Dự Án A/B Test

```bash
python -m portfolio.run --project 02_AB_Test_Feature_Impact
```

Lệnh này sẽ tự động:
1. Xác thực hợp đồng dữ liệu của `ab_sessions_raw.csv`
2. Làm sạch và tạo ra `Data/clean/ab_sessions_clean.csv`
3. Nạp dữ liệu vào cơ sở dữ liệu SQLite trong thư mục `build/`
4. Thực thi toàn bộ các câu truy vấn SQL trong `SQL/analysis.sql`
5. Xuất các bảng kết quả CSV ra thư mục `Results/`
6. Tính toán các chỉ số suy diễn thống kê bằng Python (Z-test, Newcombe-Wilson CI, SRM)
7. Tự động sinh báo cáo HTML trực quan `REPORT.html`
8. Băm mã SHA-256 và cập nhật `Results/manifest.json`

### Bước 5 — Chạy Toàn Bộ Kiểm Thử Tự Động

```bash
python -m unittest discover -s tests -v
```

### Bước 6 — Xem Báo Cáo Kết Quả

- Mở trực tiếp tệp `02_AB_Test_Feature_Impact/REPORT.html` trên trình duyệt web để xem báo cáo trực quan.
- Xem các tệp kết quả chi tiết trong thư mục `Results/`.

---

## ⚠️ Giới Hạn Phân Tích & Hướng Phát Triển

### Giới Hạn Hiện Tại

1. **Dữ liệu mô phỏng:** Kết quả phản ánh bộ dữ liệu portfolio, không phải thử nghiệm thực tế của một công ty thật ngoài đời.
2. **Chưa có mã định danh người dùng ổn định:** Thiếu `user_id` khiến ta không thể kiểm chứng tuyệt đối giả định độc lập giữa các phiên.
3. **Giả định phân bổ 50:50:** Kiểm định SRM dựa trên giả định phân chia đều 50:50; cấu hình phân bổ thuật toán thực tế trong hệ thống không được cung cấp.
4. **Chưa kiểm soát quy tắc dừng thử nghiệm (Stopping Rule):** Dữ liệu không ghi nhận liệu bài test có áp dụng quy tắc dừng sớm (early stopping) hay không.
5. **Chưa điều chỉnh cho kiểm định đa biến:** Các kết quả phân khúc thiết bị/nguồn traffic mang tính khám phá, chưa qua hiệu chỉnh kiểm định đa biến.
6. **Đơn vị tiền tệ mô phỏng:** Doanh thu thiếu mã tiền tệ cụ thể và thuyết minh quy chuẩn kế toán.

### Hướng Phát Triển Tương Lai

- Thiết lập cơ chế theo dõi phân bổ và hiển thị ở mức người dùng (`user_id`).
- Tính toán công suất kiểm định (Statistical Power) và kích thước mẫu tối thiểu trước khi chạy test.
- Đăng ký trước các giả thuyết và tiêu chí dừng thử nghiệm (Pre-registration & Sequential Testing).
- Áp dụng mô hình hồi quy logistic hoặc phân cụm người dùng (Clustered Standard Errors) để xử lý việc một người có nhiều phiên.
- Bổ sung theo dõi tác động dài hạn lên tỷ lệ giữ chân khách hàng (Long-term Retention).

---

## 🧠 Đúc Kết Từ Dự Án

### Giá Trị Kỹ Thuật

Dự án thể hiện năng lực chuyên môn vững chắc về:
- Truy vấn, gom nhóm và tính toán tỷ lệ chuyển đổi bằng SQL.
- Ứng dụng suy diễn thống kê bài bản bằng Python: Kiểm định Z hai tỷ lệ, Khoảng tin cậy Newcombe-Wilson, Kiểm định Chi-Square SRM.
- Xây dựng pipeline phân tích tự động, kiểm thử chất lượng dữ liệu và bảo đảm tính tái lập hoàn toàn.
- Đối soát chéo số liệu đa tầng triệt tiêu mọi sai số.

### Giá Trị Nghiệp Vụ

Case study làm nổi bật tư duy thực chiến của một Data Analyst:
- Biết phân biệt rõ ràng giữa ý nghĩa thống kê (statistical significance) và ý nghĩa kinh tế (business significance).
- Phân biệt rạch ròi giữa mức tăng tuyệt đối (điểm phần trăm) và mức tăng tương đối (%).
- Không chỉ chăm chăm vào một chỉ số chuyển đổi mà luôn theo dõi kèm theo các chỉ số bảo vệ (guardrail metrics).
- Dũng cảm chỉ ra các giới hạn của dữ liệu và không đưa ra các quyết định liều lĩnh khi chưa có đủ bằng chứng vững chắc.

---

## 📚 Tài Liệu Hỗ Trợ & Bằng Chứng

| Tài nguyên | Mô tả nội dung |
|---|---|
| [Từ Điển Dữ Liệu](Docs/Data_Dictionary.md) | Chi tiết các trường dữ liệu, kiểu dữ liệu và quy tắc hợp đồng |
| [Nguồn Gốc KPI](Docs/KPI_Lineage.md) | Công thức chỉ số, giả định và bảng ánh xạ kết quả |
| [Mã Nguồn SQL Phân Tích](SQL/analysis.sql) | Các câu lệnh SQL thực thi phân tích thử nghiệm |
| [Tóm Tắt Nhánh Thử Nghiệm](Results/variant_summary.csv) | Bảng KPI chuyển đổi chính của 2 nhóm |
| [Chuyển Đổi Theo Phân Khúc](Results/segment_conversion.csv) | Phân tích chi tiết theo thiết bị và nguồn traffic |
| [Phân Bổ Mẫu Theo Ngày](Results/daily_assignment.csv) | Số lượng phiên và lượt chuyển đổi theo từng ngày |
| [Chỉ Số Thống Kê](Results/additional_metrics.json) | Kết quả tính Lift, khoảng tin cậy CI, p-value và SRM |
| [Báo Cáo Chất Lượng](Results/quality.json) | Đánh giá chất lượng dữ liệu và giới hạn ngữ nghĩa |
| [Báo Cáo Kiểm Thử](Results/validation.json) | Biên bản kiểm thử tự động lúc chạy thực tế |
| [Báo Cáo HTML Độc Lập](REPORT.html) | Báo cáo trực quan hoàn chỉnh xem ngoại tuyến |

---

## 👨‍💻 Về Tác Giả

**Bùi Nhất Phong**

Data Analytics | Business Intelligence | SQL | Python | Phân Tích Sản Phẩm

Tôi tập trung vào việc chuyển đổi các câu hỏi kinh doanh phức tạp thành các bài toán phân tích đo lường được, kiểm soát chặt chẽ chất lượng dữ liệu, đánh giá chính xác hiệu quả và truyền tải những góc nhìn sâu sắc phục vụ ra quyết định.

Các lĩnh vực quan tâm hàng đầu của tôi: Thử nghiệm A/B & Tối ưu hóa chuyển đổi, Phân tích hành vi khách hàng, Business Intelligence, Quản trị chất lượng dữ liệu và Hỗ trợ ra quyết định sản phẩm dựa trên bằng chứng thực tế.

📧 [Email](mailto:buinhatphong.analytics@gmail.com)  
💼 [LinkedIn](https://www.linkedin.com/in/buinhatphong/)  
💻 [GitHub Profile](https://github.com/buinhatphong)

### 🔗 Khám Phá Thêm Dự Án Trong Portfolio

[⬅️ Quay lại Trang Tổng Quan Portfolio](../README.md)

[📈 Dự án trước: Phân Tích Sản Phẩm SaaS](../01_SaaS_Product_Analytics_StreamFlow/README.md)

[🛒 Dự án tiếp theo: Phân Tích Sản Phẩm Thương Mại Điện Tử](../03_Ecommerce_Product_Analytics/README.md)

---

**🧪 Thử Nghiệm A/B & Tác Động Tính Năng | Xây dựng bởi Bùi Nhất Phong**  
*Quyết định dựa trên nền tảng thống kê vững chắc. Phân tích tái lập 100%. Bằng chứng minh bạch.*

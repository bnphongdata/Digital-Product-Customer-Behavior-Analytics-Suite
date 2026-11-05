# 📈 Phân Tích Sản Phẩm SaaS | StreamFlow

### Kích Hoạt Người Dùng • Doanh Thu Gói Đăng Ký • Phễu Onboarding • Phân Tích Rời Bỏ (Churn)

**Dự án phân tích dữ liệu end-to-end bằng SQL và Python, nghiên cứu sâu cách khách hàng SaaS kích hoạt sản phẩm, trải qua phễu onboarding, đóng góp doanh thu định kỳ và các hành vi liên quan đến việc duy trì tài khoản.**

![Python](https://img.shields.io/badge/Python-3.12-3776AB)
![SQL](https://img.shields.io/badge/SQL-SQLite-4479A1)
![Phân Tích Sản Phẩm](https://img.shields.io/badge/Product-Analytics-blueviolet)
![Kiểm Tra Chất Lượng](https://img.shields.io/badge/Validation-19%2F19-success)
![Bộ Dữ Liệu](https://img.shields.io/badge/Dữ_Liệu-Mô_Phỏng-orange)

**Người thực hiện:** Bùi Nhất Phong  
**Dự án:** 01 — Phân Tích Sản Phẩm SaaS  
**Portfolio:** [Data Analyst Portfolio](../README.md)  
**LinkedIn:** [Bùi Nhất Phong](https://www.linkedin.com/in/buinhatphong/)

---

## 📌 Tóm Tắt Dự Án (Executive Summary)

StreamFlow là một case study phân tích sản phẩm dạng phần mềm dịch vụ (SaaS) dựa trên dữ liệu mô phỏng, tập trung nghiên cứu sâu quá trình onboarding của khách hàng, hiệu quả kinh doanh của các gói đăng ký, hành vi tương tác và các chỉ báo liên quan đến việc rời bỏ dịch vụ (churn).

Dự án này minh họa cách một Data Analyst thực chiến sử dụng kết hợp SQL, Python, quy trình kiểm soát chất lượng dữ liệu tự động và tư duy Business Intelligence để biến các bảng dữ liệu SaaS thô thành những chỉ số đo lường tin cậy, từ đó rút ra các đề xuất hành động thực tế cho doanh nghiệp.

Nghiên cứu tập trung giải quyết 4 câu hỏi nghiệp vụ cốt lõi:

1. Người dùng đang rơi rụng nhiều nhất ở bước nào trong quy trình onboarding?
2. Doanh thu định kỳ hàng tháng (MRR) phân bổ thế nào giữa các gói dịch vụ?
3. Nhãn churn trong dữ liệu phản ánh điều gì về tập khách hàng trả phí?
4. Đội ngũ sản phẩm và kinh doanh cần thu thập thêm bằng chứng nào trước khi đưa ra quyết định giữ chân khách hàng?

### Kết Quả Cốt Lõi

| Chỉ số kinh doanh | Kết quả xác thực |
|---|---:|
| 👥 Tổng số người dùng | 1.500 |
| 💳 Khách hàng trả phí | 698 |
| 💰 Doanh thu hàng tháng (Snapshot MRR) | 189.975,00 |
| 📅 Doanh thu quy năm ước tính (Snapshot ARR) | 2.279.700,00 |
| 📉 Tỷ lệ nhãn churn nhóm trả phí | 21,06% |
| 🚧 Tỷ lệ rơi rụng ngay bước onboarding đầu tiên | 62,59% |
| 🏢 Tỷ trọng MRR từ gói Enterprise | 83,80% |
| ✅ Bài kiểm thử dữ liệu & logic đã vượt qua | 19/19 passed |

**Công bố về dữ liệu:** Dự án sử dụng dữ liệu được sinh mô phỏng (synthetic). Đơn vị tiền tệ không được quy định cụ thể và các kết quả phân tích không đại diện cho một doanh nghiệp thật hay một hệ thống production ngoài đời thực.

### Phát Hiện Quan Trọng Nhất

Điểm rơi rụng lớn nhất trong phễu onboarding diễn ra ngay giữa **Bước 1: Account (Tạo tài khoản)** và **Bước 2: Workspace (Thiết lập không gian làm việc)**. Trong số 1.088 người dùng hoàn thành Bước 1, có tới 62,59% không bước tiếp sang giai đoạn kế tiếp theo đúng trình tự thời gian.

Mặt khác, các gói đăng ký Enterprise đóng góp tới **83,80% tổng doanh thu MRR ghi nhận**, cho thấy mức độ tập trung doanh thu cực kỳ lớn vào nhóm khách hàng doanh nghiệp lớn.

Hai con số này chỉ ra hai trọng tâm mà đội ngũ vận hành cần đặc biệt lưu tâm: **trải nghiệm kích hoạt ban đầu của người dùng và rủi ro tập trung nguồn thu**.

---

## 📚 Mục Lục

1. [Bài Toán Nghiệp Vụ](#-bài-toán-nghiệp-vụ)
2. [Tổng Quan Bộ Dữ Liệu](#-tổng-quan-bộ-dữ-liệu)
3. [Bộ Công Cụ Kỹ Thuật (Tech Stack)](#-bộ-công-cụ-kỹ-thuật-tech-stack)
4. [Quy Trình Phân Tích End-to-End](#-quy-trình-phân-tích-end-to-end)
5. [Định Nghĩa KPI & Quy Tắc Nghiệp Vụ](#-định-nghĩa-kpi--quy-tắc-nghiệp-vụ)
6. [Phân Tích 1: Doanh Thu Gói Đăng Ký SaaS](#-phân-tích-1-doanh-thu-gói-đăng-ký-saas)
7. [Phân Tích 2: Phễu Onboarding Người Dùng](#-phân-tích-2-phễu-onboarding-người-dùng)
8. [Phân Tích 3: Rời Bỏ (Churn) & Mức Độ Tương Tác](#-phân-tích-3-rời-bỏ-churn--mức-độ-tương-tác)
9. [Hiện Thực Hóa Bằng SQL](#-hiện-thực-hóa-bằng-sql)
10. [Khuyến Nghị Kinh Doanh](#-khuyến-nghị-kinh-doanh)
11. [Chất Lượng Dữ Liệu & Đối Soát](#-chất-lượng-dữ-liệu--đối-soát)
12. [Tài Sản Business Intelligence & Dashboard](#-tài-sản-business-intelligence--dashboard)
13. [Cấu Trúc Thư Mục Dự Án](#-cấu-trúc-thư-mục-dự-án)
14. [Hướng Dẫn Tái Lập Phân Tích](#-hướng-dẫn-tái-lập-phân-tích)
15. [Giới Hạn Phân Tích & Hướng Phát Triển](#-giới-hạn-phân-tích--hướng-phát-triển)
16. [Đúc Kết Từ Dự Án](#-đúc-kết-từ-dự-án)

---

## 🎯 Bài Toán Nghiệp Vụ

### Bối Cảnh Doanh Nghiệp

Đối với mô hình kinh doanh phần mềm thuê bao (SaaS), việc thu hút khách hàng mới đăng ký (acquisition) chỉ là khởi đầu, hoàn toàn không đảm bảo tăng trưởng bền vững.

Người dùng cần phải hoàn thành onboarding suôn sẻ, cảm nhận được giá trị cốt lõi của sản phẩm (activation) và tiếp tục sử dụng thường xuyên thì nguồn thu định kỳ mới duy trì ổn định.

Do đó, các bộ phận phân tích dữ liệu cần đo lường chuẩn xác:

- Tiến độ người dùng trải qua các bước onboarding
- Hành vi kích hoạt tính năng cốt lõi
- Hiệu quả kinh doanh của từng gói cước
- Doanh thu định kỳ hàng tháng (MRR)
- Các chỉ báo liên quan đến việc rời bỏ (churn)
- Mức độ tương tác với sản phẩm (product engagement)
- Mức độ tập trung doanh thu theo phân khúc
- Độ tin cậy và chất lượng của dữ liệu báo cáo

Nếu định nghĩa chỉ số thiếu chặt chẽ hoặc dữ liệu sự kiện bị nhiễu, doanh nghiệp rất dễ đổ nguồn lực vào những cải tiến sản phẩm không đúng chỗ.

### Mục Tiêu Phân Tích

| Mục tiêu | Câu hỏi phân tích | Ý nghĩa ra quyết định |
|---|---|---|
| Cải thiện kích hoạt | Người dùng rơi rụng ở đâu trong phễu onboarding? | Xác định điểm nghẽn để tối ưu trải nghiệm người dùng (UX) |
| Hiểu rõ doanh thu | Gói cước nào đem về phần lớn MRR? | Đánh giá mức độ rủi ro do tập trung doanh thu |
| Khảo sát Churn | Tỷ lệ nhãn churn ở nhóm trả phí là bao nhiêu? | Thiết lập chỉ báo mô tả cơ sở về khả năng giữ chân |
| Đánh giá tương tác | Hoạt động sản phẩm liên hệ thế nào với nhãn churn? | Xem xét liệu có cơ sở để đi sâu vào phân tích phân khúc hay không |
| Kiểm soát báo cáo | Dữ liệu nguồn và công thức tính toán có khớp nhau không? | Đảm bảo các con số báo cáo có thể kiểm chứng độc lập |

### Mục Tiêu Đầu Ra

Xây dựng một quy trình phân tích hoàn chỉnh, tái lập được 100%, chuyển đổi dữ liệu SaaS thô thành các chỉ số kinh doanh có thể truy vết nguồn gốc và đưa ra những khuyến nghị thực tế dựa trên dữ liệu sẵn có.

---

## 🗄️ Tổng Quan Bộ Dữ Liệu

Dự án sử dụng 3 bảng dữ liệu mô phỏng liên kết chặt chẽ với nhau, gồm tổng cộng **32.175 dòng dữ liệu gốc**.

### Bảng Dữ Liệu Nguồn

| Bảng dữ liệu | Số dòng | Mục đích sử dụng |
|---|---:|---|
| `users_raw.csv` | 1.500 | Thuộc tính tài khoản, ngày đăng ký, gói cước và kênh tiếp thị |
| `subscriptions_raw.csv` | 1.500 | Ảnh chụp gói đăng ký, MRR, số lượng seat và nhãn churn |
| `events_raw.csv` | 29.175 | Các hành động onboarding và tương tác tính năng của người dùng |
| **Tổng cộng** | **32.175** | **3 bảng dữ liệu nguồn phân tích** |

### 1. Bảng Users (Người Dùng)

Chứa thông tin chi tiết ở mức tài khoản, giúp hiểu rõ cơ cấu khách hàng và xác lập mốc thời gian bắt đầu theo dõi onboarding.

**Các trường quan trọng:**

- `user_id` — Mã định danh duy nhất của người dùng
- `signup_date` — Ngày tạo tài khoản
- `country` — Mã quốc gia được ghi nhận
- `acquisition_channel` — Kênh tiếp thị thu hút người dùng
- `plan_tier` — Gói dịch vụ: Free, Starter, Pro hoặc Enterprise

**Mục đích:** Phân khúc khách hàng, xác định thời điểm đăng ký và làm khóa ngoại liên kết.

### 2. Bảng Subscriptions (Gói Đăng Ký)

Cung cấp thông tin đăng ký dịch vụ để tính toán doanh thu snapshot và tỷ lệ gắn nhãn churn.

**Các trường quan trọng:**

- `user_id` — Khóa liên kết với tài khoản người dùng
- `plan_tier` — Gói dịch vụ tương ứng
- `mrr` — Doanh thu định kỳ hàng tháng tại thời điểm chụp dữ liệu
- `seats` — Số lượng vị trí (seats) được cấp phép
- `completed_step2` — Cờ ghi nhận hoàn thành Bước 2 onboarding
- `churned_within_90d` — Nhãn kết quả rời bỏ trong vòng 90 ngày
- `first_payment_date` — Ngày thanh toán đầu tiên được ghi nhận

**Mục đích:** Báo cáo doanh thu, hiệu quả gói cước và so sánh hành vi churn.

### 3. Bảng Events (Nhật Ký Sự Kiện)

Ghi nhận các tương tác thực tế của người dùng với ứng dụng SaaS mô phỏng.

**Các trường quan trọng:**

- `user_id` — Người dùng thực hiện hành động
- `event_date` — Ngày phát sinh sự kiện (mức ngày)
- `event_group` — Nhóm sự kiện: Onboarding hoặc Product
- `event_name` — Tên hành động cụ thể (ví dụ: các bước onboarding hoặc chạy workflow)

**Mục đích:** Xây dựng phễu tuần tự thời gian, khảo sát mức độ tương tác và kiểm tra chất lượng dữ liệu sự kiện.

### Mối Quan Hệ Dữ Liệu

Toàn bộ phân tích liên kết qua trường `user_id`:

**Users (1) → (1) Subscriptions**

**Users (1) → (Nhiều) Events**

Mối quan hệ này được bảo đảm bằng các quy tắc kiểm tra hợp đồng dữ liệu và tính toàn vẹn tham chiếu.

### Tài Liệu Chi Tiết

[📘 Từ Điển Dữ Liệu](Docs/Data_Dictionary.md) | [📂 Dữ Liệu Thô (raw)](Data/raw) | [📂 Dữ Liệu Đã Làm Sạch (clean)](Data/clean)

---

## 🛠️ Bộ Công Cụ Kỹ Thuật (Tech Stack)

| Hạng mục | Công nghệ | Ứng dụng thực tế |
|---|---|---|
| Ngôn ngữ lập trình | Python 3.12 | Xử lý dữ liệu, kiểm thử tự động, đối soát chéo số liệu |
| Truy vấn dữ liệu | SQL | Tính toán KPI và chạy các truy vấn phân tích nghiệp vụ |
| Cơ sở dữ liệu | SQLite | Lưu trữ và thực thi truy vấn quan hệ cục bộ |
| Thư viện phân tích | pandas | Tính toán độc lập để đối chiếu với kết quả SQL |
| Chuẩn hóa dữ liệu | Python | Kiểm tra schema, ép kiểu và chuẩn hóa định dạng |
| Thống kê & Tư duy | Số liệu mô tả | Tỷ lệ, cơ cấu, phân phối và phân tích quan sát |
| Báo cáo kết quả | HTML & CSV | Xuất bảng kết quả và báo cáo tương tác ngoại tuyến |
| Bảng tính Excel | Excel | Kiểm tra công thức và tái lập số liệu bằng sổ làm việc |
| Trực quan hóa dữ liệu | Tableau | Tệp dashboard cũ và tệp trích xuất Hyper chuẩn hóa |
| Đảm bảo chất lượng (QA) | Python unittest | Bộ kiểm thử tự động toàn diện |
| Quản lý phiên bản | Git & GitHub | Quản lý mã nguồn và lịch sử phát triển dự án |
| Tính tái lập | SHA-256 manifests | Truy vết mã băm toàn vẹn cho dữ liệu, mã nguồn và kết quả |

### Kỹ Năng SQL Được Thể Hiện

- Kết nối bảng (JOINS) và tính toàn vẹn quan hệ
- Các hàm tổng hợp (Aggregate functions)
- Tổng hợp có điều kiện (`CASE WHEN` bên trong `SUM`/`COUNT`)
- Bảng tạm dùng chung (Common Table Expressions - CTE)
- Truy vấn con (Subqueries) và truy vấn con tương quan (Correlated subqueries)
- Xử lý sự kiện theo thứ tự thời gian nghiêm ngặt
- Phân nhóm dữ liệu (`GROUP BY`)
- Phép chia an toàn tránh lỗi chia cho 0 (`NULLIF`)
- Lọc dữ liệu theo mốc thời gian
- Xây dựng phễu chuyển đổi đa bước

### Kỹ Năng Python Được Thể Hiện

- Nhập xuất và biến đổi dữ liệu có kiểm soát
- Kiểm tra kiểu dữ liệu và hợp đồng dữ liệu
- Xây dựng mô-đun phân tích tái sử dụng được
- Tự động đối soát kết quả SQL với thuật toán Python
- Kiểm thử tự động chất lượng dữ liệu
- Tự động sinh báo cáo HTML trực quan
- Quản lý tính toàn vẹn của kết quả thông qua mã băm cryptographic

---

## 🔄 Quy Trình Phân Tích End-to-End

Dự án áp dụng quy trình phân tích chặt chẽ gồm 8 bước từ dữ liệu thô đến đề xuất kinh doanh:

### Bước 1 — Xác Định Yêu Cầu Nghiệp Vụ

Làm rõ bài toán kinh doanh, mục tiêu báo cáo, tập người dùng cần khảo sát và quy tắc tính toán từng chỉ số.

**Đầu ra:** Tài liệu phạm vi phân tích và quy tắc tính KPI.

### Bước 2 — Khảo Sát & Đánh Giá Dữ Liệu Thô

Kiểm tra trực tiếp các tệp raw để xác định:

- Mức độ chi tiết (grain) của từng bảng
- Các trường thông tin sẵn có
- Khóa chính và các mối liên kết
- Các cột bắt buộc không được phép null
- Định dạng ngày tháng và các kiểu dữ liệu
- Các trường hợp lặp dòng hoặc thiếu ngữ cảnh

**Đầu ra:** Từ điển dữ liệu nguồn và hợp đồng kiểm tra dữ liệu.

### Bước 3 — Làm Sạch & Chuẩn Hóa Dữ Liệu

Chuẩn hóa các kiểu dữ liệu được hỗ trợ và tạo ra các tệp dữ liệu sạch sẵn sàng cho phân tích.

Các bước kiểm soát bao gồm:

- Đảm bảo không thiếu giá trị ở các cột bắt buộc
- Kiểm tra khoảng giá trị hợp lệ của các trường số (không âm, dương với ID)
- Chuẩn hóa định dạng ngày về YYYY-MM-DD
- Chuẩn hóa trường boolean về 0/1
- Kiểm tra tính duy nhất của khóa chính
- Kiểm tra tính toàn vẹn tham chiếu giữa các bảng
- Ghi nhận và báo cáo các bất thường dữ liệu

Các tệp dữ liệu thô ban đầu được giữ nguyên vẹn 100%.

**Đầu ra:** Các tệp CSV sạch (`Data/clean/`) được tạo lại hoàn toàn tự động.

### Bước 4 — Nạp Dữ Liệu & Phân Tích Bằng SQL

Nạp các bảng dữ liệu sạch vào cơ sở dữ liệu SQLite cục bộ và thực thi các câu truy vấn phân tích nghiệp vụ:

1. Tổng hợp doanh thu gói đăng ký
2. Doanh thu theo từng gói cước
3. Phễu chuyển đổi onboarding theo trình tự thời gian
4. Mối liên hệ giữa hoạt động sản phẩm và nhãn churn

**Đầu ra:** Các bảng kết quả xuất ra thư mục `Results/*.csv`.

### Bước 5 — Đối Soát Độc Lập Bằng Python

Đối chiếu các kết quả cốt lõi tính bằng SQL với kết quả tính toán độc lập bằng Python (sử dụng pandas và logic Python thuần).

Các bài kiểm tra đối soát bao gồm: tổng doanh thu, số lượng người đăng ký trả phí, tỷ lệ churn, số lượng người dùng qua từng bước phễu, và các phép tính hoạt động sản phẩm.

**Đầu ra:** Báo cáo kiểm định `validation.json` và bằng chứng tái lập.

### Bước 6 — Phân Tích & Đọc Hiểu Nghiệp Vụ

Rút ra các quy luật và hiểu biết sâu sắc từ số liệu, phân biệt rạch ròi giữa kết quả quan sát thuần túy với các giả thuyết cần được kiểm chứng thêm.

**Đầu ra:** Các phát hiện, giới hạn phân tích và khuyến nghị cho doanh nghiệp.

### Bước 7 — Báo Cáo & Trực Quan Hóa

Tự động sinh các bảng kết quả CSV và báo cáo HTML trực quan ngoại tuyến (offline).

**Đầu ra:** Các tệp kết quả CSV, báo cáo `REPORT.html` và tệp manifest băm SHA-256.

### Tóm Tắt Luồng Dữ Liệu

**CSV Thô → Kiểm Tra Hợp Đồng → CSV Sạch → Cơ Sở Dữ Liệu SQLite → Truy Vấn SQL Tính KPI → Đối Soát Bằng Python → Tệp Kết Quả & Báo Cáo → Đề Xuất Kinh Doanh**

---

## 📐 Định Nghĩa KPI & Quy Tắc Nghiệp Vụ

Việc định nghĩa chỉ số rõ ràng là yếu tố tiên quyết để đảm bảo tính nhất quán của mọi báo cáo.

| KPI | Định nghĩa | Quy tắc nghiệp vụ then chốt |
|---|---|---|
| Tổng số người dùng | Đếm số bản ghi trong bảng users | Mỗi người dùng có một khóa `user_id` duy nhất |
| Người dùng trả phí | Đếm số dòng đăng ký có MRR > 0 | Loại trừ các tài khoản gói Free |
| Snapshot MRR | Tổng giá trị MRR được cung cấp | Chỉ là ảnh chụp doanh thu tại thời điểm, không phải doanh thu kế toán |
| Snapshot ARR | Snapshot MRR × 12 | Ước tính quy năm, không phải dự báo tài chính |
| Tỷ lệ nhãn churn nhóm trả phí | Khách trả phí có nhãn churn ÷ Tổng khách trả phí | Nhãn quan sát được, không phải chu kỳ sống được tái dựng |
| Tỷ lệ tiếp cận bước Onboarding | Số người dùng hoàn thành đúng trình tự tới bước đó | Bắt buộc phải hoàn thành các bước trước đó trước |
| Tỷ lệ rơi rụng Onboarding | 1 − (Số người bước sau ÷ Số người bước trước) | Tính toán trên tập người dùng đủ điều kiện thời gian |
| Tỷ trọng doanh thu theo gói | MRR của gói ÷ Tổng Snapshot MRR | Tính toán trên toàn bộ bản ghi đăng ký |
| Phân nhóm hoạt động Workflow | Đếm số lượt chạy workflow trong 90 ngày đầu | Chỉ mang tính mô tả tương quan |

### Các Phân Biệt Khái Niệm Quan Trọng

**MRR Snapshot vs. Doanh Thu Ghi Nhận Kế Toán**

Trường `mrr` trong bộ dữ liệu thể hiện ảnh chụp tại một thời điểm của gói dịch vụ. Con số này không chứng thực việc tiền đã thực thu về tài khoản hay doanh thu được ghi nhận theo chuẩn kế toán định kỳ.

**Nhãn Churn vs. Hành Vi Rời Bỏ Thực Tế**

Bộ dữ liệu chứa một cờ nhị phân biểu thị việc churn nhưng thiếu lịch sử hủy gói và chu kỳ thanh toán hoàn chỉnh để tái lập phân tích cohort retention chuẩn mực.

**Chạm Sự Kiện vs. Hoàn Thành Phễu Tuần Tự**

Việc một người dùng ghi nhận có sự kiện ở một bước không có nghĩa là họ đã hoàn thành hợp lệ các bước trước đó. Phễu tuần tự đòi hỏi các bước phải diễn ra theo đúng thứ tự ngày tháng không giảm sau ngày đăng ký.

Xem chi tiết: [Nguồn Gốc KPI (KPI Lineage)](Docs/KPI_Lineage.md)

---

## 💰 Phân Tích 1: Doanh Thu Gói Đăng Ký SaaS

### Câu Hỏi Nghiệp Vụ

Gói dịch vụ nào đóng góp nhiều doanh thu định kỳ hàng tháng nhất, và mức độ tập trung doanh thu ra sao?

### Hiệu Quả Doanh Thu Theo Gói

| Gói dịch vụ | Số người dùng | Snapshot MRR | Tỷ trọng MRR |
|---|---:|---:|---:|
| 🏢 Enterprise | 92 | 159.201 | 83,80% |
| 💼 Pro | 264 | 20.856 | 10,98% |
| 🌱 Starter | 342 | 9.918 | 5,22% |
| 🆓 Free | 802 | 0 | 0,00% |
| **Tổng cộng** | **1.500** | **189.975** | **100%** |

### Phát Hiện 1 — Gói Enterprise Chiếm Phần Lớn Doanh Thu

Khách hàng Enterprise chỉ chiếm một phần nhỏ trong tổng số người dùng (92 trên 1.500 người, khoảng 6,13%), nhưng lại mang lại tới **83,80% tổng doanh thu hàng tháng**.

**Đánh giá:** Nguồn thu của sản phẩm phụ thuộc rất lớn vào một nhóm nhỏ khách hàng doanh nghiệp lớn.

Điều này biến việc duy trì hợp đồng và chăm sóc khách hàng Enterprise thành ưu tiên sống còn của bộ phận Customer Success.

Tuy nhiên, chỉ dựa vào ảnh chụp gói cước thì chưa thể đánh giá toàn diện rủi ro doanh thu nếu thiếu thông tin về thời hạn hợp đồng và lịch sử gia hạn.

### Phát Hiện 2 — Tài Khoản Miễn Phí Chiếm Đa Số Người Dùng

Gói Free có 802 người dùng, tương đương 53,47% tổng số tài khoản trong hệ thống.

Đây là một tệp người dùng không trả phí rất lớn.

**Hướng khảo sát tiếp theo:** Đội ngũ sản phẩm cần tìm hiểu xem người dùng gói Free có gặp rào cản kích hoạt nào khiến họ không muốn hoặc không thể nâng cấp lên gói trả phí hay không.

Dữ liệu hiện tại chưa đủ để vẽ lại hành trình chuyển đổi từ Free sang Paid hoặc chỉ ra lý do cụ thể người dùng không chi tiền.

### Phát Hiện 3 — Hai Gói Starter & Pro Đóng Góp Khiêm Tốn

Starter và Pro cộng lại chỉ đóng góp khoảng 16,20% tổng MRR.

Để mở rộng doanh thu từ phân khúc khách hàng cá nhân và doanh nghiệp vừa và nhỏ (SMB), công ty cần thu thập thêm dữ liệu về tần suất dùng tính năng, mức độ hài lòng về giá và tỷ lệ nâng/hạ cấp gói.

### Khuyến Nghị Kinh Doanh

1. Ưu tiên phân tích chuyên sâu về nhóm khách hàng Enterprise, kiểm tra hợp đồng và lịch sử gia hạn để dự phòng rủi ro churn nguồn thu lớn.
2. Thiết kế khảo sát hoặc phỏng vấn nhóm người dùng Free và Starter để tìm ra rào cản ngăn họ nâng cấp tính năng.

**Bằng chứng truy vấn SQL:** [Doanh thu theo gói (revenue_by_tier.csv)](Results/revenue_by_tier.csv)

---

## 🚀 Phân Tích 2: Phễu Onboarding Người Dùng

### Câu Hỏi Nghiệp Vụ

Người dùng đang gặp khó khăn và bỏ cuộc ở những bước nào trong quá trình làm quen với sản phẩm?

### Các Bước Trong Quy Trình Onboarding

Theo dữ liệu sự kiện, quy trình onboarding tiêu chuẩn gồm 5 bước tuần tự:

**Tạo tài khoản (Account) → Thiết lập không gian làm việc (Workspace) → Kết nối tích hợp (Integration) → Chạy luồng công việc đầu tiên (First Workflow) → Mời đồng nghiệp (Invite Team)**

Truy vấn SQL tiến hành đánh giá xem có bao nhiêu người dùng hoàn thành lần lượt từng bước này theo đúng thứ tự ngày hợp lệ.

### Kết Quả Phễu Tuần Tự Được Xác Thực

| Giai đoạn | Số người dùng | Tỷ lệ giữ chân so với bước trước |
|---|---:|---:|
| Bước 1: Account (Tạo tài khoản) | 1.088 | Mốc chuẩn (Baseline) |
| Bước 2: Workspace (Không gian làm việc) | 407 | 37,41% |
| Bước 3: Integration (Kết nối tích hợp) | 123 | 30,22% |
| Bước 4: First Workflow (Chạy luồng đầu) | 34 | 27,64% |
| Bước 5: Invite Team (Mời đồng nghiệp) | 9 | 26,47% |

### Phân Tích Tỷ Lệ Rơi Rụng Giữa Các Bước

| Bước chuyển đổi | Số người bỏ cuộc | Tỷ lệ rơi rụng (Drop-Off) |
|---|---:|---:|
| Account → Workspace | 681 | 62,59% |
| Workspace → Integration | 284 | 69,78% |
| Integration → First Workflow | 89 | 72,36% |
| First Workflow → Invite Team | 25 | 73,53% |

### Phát Hiện 1 — Điểm Rơi Rụng Nghiêm Trọng Ngay Bước Thiết Lập Đầu Tiên

Trong số 1.088 người dùng đã kích hoạt Bước 1 (Account), chỉ có 407 người hoàn thành hợp lệ Bước 2 (Workspace).

**Có tới 62,59% người dùng biến mất ngay sau khi đăng ký.**

Con số này báo động rằng trải nghiệm thiết lập workspace ban đầu đang có vấn đề lớn.

Các giả thuyết có thể đặt ra: hướng dẫn thiết lập quá phức tạp, phát sinh lỗi kỹ thuật khi tạo workspace, hoặc người dùng chưa thấy ngay được giá trị sau khi tạo tài khoản.

### Phát Hiện 2 — Tỷ Lệ Rơi Rụng Tiếp Tục Cao Ở Các Bước Kế Tiếp

Chỉ có 123 người hoàn thành bước Integration sau khi đã qua hai bước trước.

Đến bước First Workflow chỉ còn 34 người, và bước Invite Team chỉ còn đúng 9 người.

Điều này cho thấy tỷ lệ hoàn thành trọn vẹn toàn bộ luồng onboarding chuẩn là cực kỳ thấp. Tuy nhiên, cũng cần lưu ý rằng không phải khách hàng nào cũng cần tính năng mời đồng nghiệp (ví dụ người dùng cá nhân).

### Phát Hiện 3 — Tỷ Lệ Hoàn Thành Trọn Phễu Chỉ Đạt 0,83%

Chỉ có 9 trên tổng số 1.088 người bắt đầu Bước 1 đi được đến bước cuối cùng, tương đương khoảng **0,83%**.

Đây là con số thống kê mô tả phễu tuần tự nghiêm ngặt. Ta không nên vội vã kết luận rằng 99,17% người dùng còn lại không nhận được giá trị gì từ sản phẩm, bởi có thể họ đã nhận được giá trị cốt lõi mà không cần phải mời thêm người vào nhóm.

### Kế Hoạch Điều Tra Trọng Tâm

- **Ưu tiên 1 — Tối ưu bước chuyển Account sang Workspace:** Kiểm tra lại tracking sự kiện, rà soát giao diện hướng dẫn người dùng mới và thu thập phản hồi định tính để tháo gỡ điểm nghẽn.
- **Ưu tiên 2 — Giảm rào cản bước Integration:** Đánh giá xem tài liệu hướng dẫn kết nối API/tích hợp có dễ hiểu không, hay yêu cầu kỹ thuật quá cao đối với người dùng phổ thông.
- **Ưu tiên 3 — Hỗ trợ tạo First Workflow:** Cung cấp sẵn các mẫu template workflow mẫu để người dùng chỉ cần 1 click là chạy thử thành công.
- **Ưu tiên 4 — Xem lại định nghĩa phễu:** Đánh giá lại xem bước "Invite Team" có thực sự là bước bắt buộc cho mọi đối tượng khách hàng hay chỉ là tính năng nâng cao dành riêng cho gói doanh nghiệp.

**Bằng chứng truy vấn SQL:** [Kết quả phễu Onboarding (onboarding_funnel.csv)](Results/onboarding_funnel.csv)

---

## 📉 Phân Tích 3: Rời Bỏ (Churn) & Mức Độ Tương Tác

### Câu Hỏi Nghiệp Vụ

Nhãn churn ghi nhận được phản ánh điều gì về nhóm khách hàng trả phí, và hoạt động chạy workflow thực tế có mối liên hệ như thế nào với việc rời bỏ?

### Số Liệu Churn Quan Sát Được

| Chỉ số | Kết quả |
|---|---:|
| Số người dùng trả phí | 698 |
| Tỷ lệ gắn nhãn churn ở nhóm trả phí | 21,06% |
| Cột chỉ báo churn | `churned_within_90d` |
| Tập dữ liệu khảo sát | Các thuê bao có MRR > 0 |

### Phát Hiện 1 — Tỷ Lệ Gắn Nhãn Churn Ở Khách Trả Phí Là 21,06%

Khoảng 21,06% khách hàng đang trả tiền được gắn nhãn churn trong bộ dữ liệu snapshot.

Đây là một con số mô tả thực trạng tĩnh. Cần nhấn mạnh rằng con số này chưa phải là tỷ lệ churn tính theo cohort chu kỳ sống chuẩn của SaaS, vì dữ liệu không cung cấp mốc thời gian hủy gói cụ thể, chu kỳ thanh toán hay lịch sử gia hạn.

### Phát Hiện 2 — Hạn Chế Khi Khảo Sát Nhóm Power User

Phân tích ban đầu đặt ra tiêu chí: người dùng có từ 20 lượt chạy workflow trở lên trong vòng 90 ngày đầu sau đăng ký được coi là "Power User".

Tuy nhiên, khi trích xuất kết quả:

| Phân nhóm tương tác | Số khách trả phí | Tỷ lệ nhãn Churn |
|---|---:|---:|
| Dưới 20 lượt chạy Workflow | 698 | 21,06% |
| Từ 20 lượt chạy trở lên | 0 | — |

Trong khung thời gian 90 ngày được khảo sát, **toàn bộ 698 khách hàng trả phí đều có dưới 20 lượt chạy workflow**. Không có khách hàng nào đạt ngưỡng 20 lượt.

**Ý nghĩa phân tích:** Số liệu thực tế không hỗ trợ việc so sánh tỷ lệ churn giữa nhóm "hoạt động cao" và "hoạt động thấp" với ngưỡng 20 lượt như giả định ban đầu.

Một Data Analyst trung thực sẽ không bao giờ tự bịa ra kết luận kiểu "người dùng tích cực có tỷ lệ rời bỏ thấp hơn", khi mà dữ liệu thực tế hoàn toàn không có nhóm người dùng tích cực đạt ngưỡng đó.

### Khuyến Nghị Hành Động

- Thu thập thêm dữ liệu chi tiết về chu kỳ sống của khách hàng (ngày bắt đầu gói, ngày hủy gói, lý do hủy).
- Đánh giá lại phân phối thực tế của số lượt chạy workflow để chọn ngưỡng phân nhóm phù hợp hơn (ví dụ: nhóm 1-5 lượt, 6-10 lượt).
- Triển khai phân tích cohort giữ chân theo tháng đăng ký thay vì chỉ nhìn vào một ảnh chụp tĩnh.

**Bằng chứng truy vấn SQL:** [Mối liên hệ Power User (power_user_association.csv)](Results/power_user_association.csv)

---

## 💻 Hiện Thực Hóa Bằng SQL

Toàn bộ các phân tích trong dự án đều được thực thi trực tiếp bằng các truy vấn SQLite chuẩn, bảo đảm tính minh bạch và có thể chạy lại bất cứ lúc nào.

### Ví Dụ 1 — Tổng Hợp Doanh Thu & Chỉ Báo Churn

Câu truy vấn tính toán các chỉ số kinh doanh tổng quan từ bảng thuê bao đã làm sạch:

```sql
SELECT
    COUNT(*) AS users,
    SUM(mrr > 0) AS paying_users,
    SUM(mrr) AS snapshot_mrr,
    SUM(mrr) * 12 AS snapshot_arr,

    -- Tính tỷ lệ churn riêng cho nhóm khách hàng trả phí (loại trừ tài khoản Free)
    1.0 * SUM(
        CASE
            WHEN mrr > 0
            THEN churned_within_90d
            ELSE 0
        END
    ) / NULLIF(SUM(mrr > 0), 0)
      AS paying_churn_label_rate

FROM subscriptions_clean;
```

**Kỹ thuật SQL áp dụng:**
- Hàm tổng hợp kết hợp biểu thức logic (`SUM(mrr > 0)`)
- Cấu trúc `CASE WHEN` lọc đúng đối tượng nghiệp vụ
- Ép kiểu số thực `1.0 *` để tránh lỗi chia nguyên
- Hàm `NULLIF` triệt tiêu nguy cơ lỗi chia cho 0

### Ví Dụ 2 — Phân Bổ Doanh Thu Theo Gói Cước

```sql
SELECT
    plan_tier,
    COUNT(*) AS users,
    SUM(mrr) AS snapshot_mrr,

    -- Tính tỷ trọng doanh thu của từng gói so với tổng doanh thu toàn bộ hệ thống
    1.0 * SUM(mrr)
        / NULLIF(
            (SELECT SUM(mrr)
             FROM subscriptions_clean),
            0
        ) AS mrr_share

FROM subscriptions_clean

GROUP BY plan_tier

ORDER BY snapshot_mrr DESC;
```

**Kỹ thuật SQL áp dụng:**
- Gom nhóm phân khúc bằng `GROUP BY`
- Truy vấn con vô hướng (Scalar subquery) để lấy mẫu số tổng thể
- Sắp xếp kết quả giảm dần theo doanh thu

### Ví Dụ 3 — Phễu Onboarding Tuần Tự Theo Thời Gian

Để đảm bảo người dùng chỉ được tính là hoàn thành một bước nếu họ đã trải qua các bước trước đó và ngày diễn ra sự kiện không nhỏ hơn ngày bước trước:

```sql
WITH s0 AS (
    -- Bước khởi đầu: Ngày đăng ký tài khoản
    SELECT
        user_id,
        signup_date AS reached
    FROM users_clean
),

s1 AS (
    -- Bước 1: Hoàn thành tạo tài khoản sau hoặc đúng ngày đăng ký
    SELECT
        p.user_id,
        (
            SELECT MIN(e.event_date)
            FROM events_clean e
            WHERE e.user_id = p.user_id
              AND e.event_name = 'Step 1: Account'
              AND e.event_date >= p.reached
        ) AS reached
    FROM s0 p
    WHERE p.reached IS NOT NULL
),

s2 AS (
    -- Bước 2: Thiết lập không gian làm việc sau hoặc đúng ngày hoàn thành Bước 1
    SELECT
        p.user_id,
        (
            SELECT MIN(e.event_date)
            FROM events_clean e
            WHERE e.user_id = p.user_id
              AND e.event_name = 'Step 2: Workspace'
              AND e.event_date >= p.reached
        ) AS reached
    FROM s1 p
    WHERE p.reached IS NOT NULL
)

SELECT
    COUNT(reached) AS workspace_users
FROM s2;
```

**Kỹ thuật SQL áp dụng:**
- Chuỗi CTE kế tiếp nhau mô hình hóa luồng người dùng
- Truy vấn con tương quan tìm mốc thời gian sớm nhất (`MIN(event_date)`)
- So sánh điều kiện ngày `>= reached` ngăn chặn việc nhảy cóc bước hoặc đảo ngược thứ tự thời gian

**Xem toàn bộ mã nguồn SQL:** [SQL/analysis.sql](SQL/analysis.sql)

---

## 💡 Khuyến Nghị Kinh Doanh

Dưới đây là các đề xuất hành động thực tiễn được ưu tiên dựa trên mức độ tác động và bằng chứng dữ liệu:

| Mức ưu tiên | Đề xuất hành động | Bằng chứng dữ liệu hỗ trợ | Phương án kiểm chứng |
|---|---|---|---|
| 🔴 Rất cao | Tối ưu trải nghiệm thiết lập Workspace | 62,59% người dùng rơi rụng ở bước chuyển đổi đầu | Phỏng vấn người dùng và chạy thử nghiệm A/B luồng onboarding mới |
| 🔴 Rất cao | Đánh giá rủi ro tập trung nguồn thu Enterprise | 83,80% MRR đến từ gói Enterprise | Rà soát điều khoản hợp đồng và lịch sử gia hạn từng tài khoản lớn |
| 🟡 Trung bình | Đơn giản hóa bước kết nối Integration | Tỷ lệ chuyển tiếp tới Integration rất thấp | Phân tích nhật ký lỗi kỹ thuật và tài liệu hóa API |
| 🟡 Trung bình | Đặt lại ngưỡng đo lường tương tác | 0 khách trả phí đạt ngưỡng 20 lượt chạy workflow | Khảo sát phân vị thực tế của tần suất sử dụng tính năng |
| 🟡 Trung bình | Chuẩn hóa cơ chế theo dõi Churn | Tỷ lệ churn nhãn là 21,06% | Bổ sung bảng theo dõi vòng đời thuê bao chi tiết |

### Lộ Trình Hành Động 30 / 60 / 90 Ngày

**Tháng thứ 1 (Ngày 1–30) — Chẩn Đoán & Khảo Sát**
- Rà soát lại việc gắn thẻ sự kiện (tracking instrumentation) của Bước 1 và Bước 2.
- Thực hiện 10-15 cuộc phỏng vấn sâu với người dùng mới về trải nghiệm tạo workspace.
- Rà soát thời hạn hợp đồng của toàn bộ 92 khách hàng Enterprise.

**Tháng thứ 2 (Ngày 31–60) — Thiết Kế Thử Nghiệm**
- Thiết kế luồng onboarding rút gọn (checklist trực quan, mẫu workspace có sẵn).
- Xác lập chỉ số đo lường chính (tỷ lệ chuyển đổi Bước 1 sang Bước 2) và chỉ số bảo vệ (guardrail metrics).
- Triển khai thử nghiệm A/B ngẫu nhiên có kiểm soát.

**Tháng thứ 3 (Ngày 61–90) — Đánh Giá & Mở Rộng**
- Đánh giá kết quả thử nghiệm A/B, tính toán khoảng tin cậy và giá trị p-value.
- Nếu phiên bản mới cải thiện có ý nghĩa thống kê, tiến hành phát hành toàn diện.
- Lên kế hoạch tiếp theo cho bước tối ưu luồng Integration.

---

## ✅ Chất Lượng Dữ Liệu & Đối Soát

### Tầm Quan Trọng Của Việc Kiểm Tra Dữ Liệu

Mọi quyết định kinh doanh chuẩn xác đều phải bắt đầu từ dữ liệu chuẩn xác. Nếu dữ liệu đầu vào bị lỗi hoặc câu truy vấn bị sai logic, các kết luận rút ra sẽ gây thiệt hại nặng nề cho doanh nghiệp.

Dự án này tích hợp sẵn bộ kiểm thử chất lượng tự động kiểm tra từ schema, tính toàn vẹn tham chiếu, tính đúng đắn của logic tính toán đến việc đối soát chéo độc lập.

### Tóm Tắt Kết Quả Kiểm Tra Chất Lượng

| Tiêu chí kiểm tra | Bằng chứng ghi nhận |
|---|---:|
| Bản ghi người dùng (Users) | 1.500 bản ghi, khóa chính không trùng lặp |
| Bản ghi thuê bao (Subscriptions) | 1.500 bản ghi, khóa ngoại khớp 100% |
| Bản ghi sự kiện (Events) | 29.175 bản ghi |
| Số ô dữ liệu bắt buộc bị thiếu | 0 ô |
| Dòng sự kiện trùng lặp nguyên bản | 481 dòng (được đếm và giữ nguyên) |
| Tài khoản Free có cờ churn dương | 218 tài khoản (loại trừ khỏi mẫu số churn trả phí) |
| Sự kiện xảy ra trước ngày đăng ký | 0 trường hợp |
| Mâu thuẫn giữa cờ Step 2 và dữ liệu sự kiện | 0 trường hợp |
| Số bài kiểm thử tự động vượt qua | 19/19 passed |

### Quyết Định Xử Lý Dữ Liệu Quan Trọng

1. **Giữ nguyên 481 dòng sự kiện lặp:** Vì dữ liệu sự kiện không có mã ID riêng biệt cho từng hành động và chỉ ghi nhận ở mức ngày, không thể khẳng định chắc chắn 481 dòng này là lỗi nhân bản do hệ thống hay là người dùng thực sự thực hiện hành động đó nhiều lần trong ngày. Phân tích chọn phương án minh bạch: giữ nguyên và công bố rõ ràng trong báo cáo.
2. **Tách riêng tài khoản Free khỏi chỉ số Churn trả phí:** Có 218 tài khoản Free mang cờ churn dương. Tuy nhiên, chỉ số KPI theo yêu cầu nghiệp vụ là tỷ lệ rời bỏ của khách hàng trả phí, do đó mẫu số và tử số chỉ tính trên các tài khoản có `mrr > 0`.
3. **Bảo đảm tính toàn vẹn tham chiếu:** Mọi `user_id` trong bảng subscriptions và events đều tồn tại hợp lệ trong bảng users.
4. **Đối soát chéo độc lập:** Toàn bộ các chỉ số tính bằng SQL đều được viết lại bằng thuật toán Python độc lập để so sánh từng con số, đảm bảo không có sai sót do khác biệt phương ngữ hay logic lập trình.

**Các tệp kết quả kiểm thử:**
- [validation.json](Results/validation.json) — Biên bản kiểm tra kỹ thuật và đối soát số liệu
- [quality.json](Results/quality.json) — Báo cáo các phát hiện bất thường trong dữ liệu
- [manifest.json](Results/manifest.json) — Bảng mã băm SHA-256 bảo đảm tính toàn vẹn tuyệt đối

---

## 📊 Tài Sản Business Intelligence & Dashboard

Dự án cung cấp đầy đủ các tài sản từ bảng tính Excel, trích xuất dữ liệu Tableau đến báo cáo HTML ngoại tuyến:

| Tài sản | Vị trí | Mục đích sử dụng |
|---|---|---|
| Mô hình bảng tính Excel | [Excel Workbook](Excel/01_SaaS_Product_Analytics_StreamFlow_Model.xlsx) | Sổ làm việc kiểm tra công thức và tính toán tóm tắt |
| Dashboard Tableau cũ | [Thư mục Dashboard](Dashboard/) | Lưu trữ file dashboard nguyên bản |
| Dữ liệu trích xuất Tableau | [Validated_Analysis.hyper](Dashboard/Validated_Analysis.hyper) | File Hyper chuẩn hóa nguồn phục vụ việc tạo lại visual |
| Ảnh chụp Dashboard | [Thư mục Images](Images/) | Ảnh chụp giao diện dashboard gốc |
| Báo cáo HTML độc lập | [REPORT.html](REPORT.html) | Báo cáo trực quan độc lập tự động tạo từ SQL & Python |

### Trạng Thái Đối Soát Dashboard Gốc

Qua rà soát kỹ thuật, tệp Tableau nguyên bản sử dụng một tập dữ liệu khác biệt về schema và số lượng sự kiện so với 3 tệp CSV chuẩn của dự án. Vì vậy:

- Dashboard cũ được giữ lại như một tài sản tham khảo lịch sử.
- Ảnh chụp của nó không được coi là bằng chứng cho các giá trị KPI chuẩn.
- Đã tạo sẵn tệp trích xuất `Validated_Analysis.hyper` chứa chính xác dữ liệu sạch và kết quả đã được xác thực để sẵn sàng kết nối lại trong Tableau Desktop.

Xem thêm: [Biên Bản Đối Soát Dashboard](Docs/Dashboard_Reconciliation.md) | [Ánh Xạ Trường Dữ Liệu](Docs/Dashboard_Field_Mapping.md) | [Hướng Dẫn Kết Nối](Docs/Connect_To_Dashboard.md)

---

## 📂 Cấu Trúc Thư Mục Dự Án

```text
01_SaaS_Product_Analytics_StreamFlow/
│
├── Data/
│   ├── raw/                              # Dữ liệu CSV thô ban đầu (bảo toàn nguyên vẹn)
│   └── clean/                            # Dữ liệu CSV sạch đã qua chuẩn hóa kiểu và hợp đồng
│
├── SQL/
│   ├── analysis.sql                      # Các truy vấn phân tích chính
│   └── advanced_queries.sql              # Các truy vấn nâng cao chuyên sâu
│
├── Python/
│   └── analysis.py                       # Điểm kích hoạt xử lý Python của dự án
│
├── Excel/
│   └── 01_SaaS_Product_Analytics_StreamFlow_Model.xlsx  # Sổ tính toán đối soát công thức
│
├── Dashboard/
│   ├── README.md                         # Hướng dẫn tái lập dashboard
│   ├── Validated_Analysis.hyper          # Tệp trích xuất Hyper chuẩn hóa cho Tableau
│   └── Product Analytics Dashboard...twbx
│
├── Images/
│   └── Product Analytics Dashboard...png
│
├── Results/
│   ├── summary.csv                       # Tổng hợp doanh thu và churn
│   ├── revenue_by_tier.csv               # Doanh thu theo gói cước
│   ├── onboarding_funnel.csv             # Kết quả phễu tuần tự
│   ├── power_user_association.csv        # Khảo sát hoạt động workflow
│   ├── additional_metrics.json           # Các chỉ số bổ trợ
│   ├── quality.json                      # Nhật ký kiểm tra chất lượng dữ liệu
│   ├── validation.json                   # Kết quả kiểm thử tự động
│   ├── query_plans.json                  # Kế hoạch thực thi truy vấn SQLite
│   └── manifest.json                     # Mã băm SHA-256 toàn vẹn
│
├── Docs/
│   ├── Data_Dictionary.md                # Từ điển dữ liệu nguồn
│   ├── KPI_Lineage.md                    # Nguồn gốc và công thức KPI
│   ├── Dashboard_Reconciliation.md       # Trạng thái đối soát dashboard
│   ├── Dashboard_Field_Mapping.md        # Ánh xạ trường dữ liệu lên visual
│   └── Connect_To_Dashboard.md           # Hướng dẫn kết nối lại dashboard
│
├── REPORT.html                           # Báo cáo phân tích trực quan độc lập
└── README.md                             # Tài liệu case study chi tiết này
```

---

## ▶️ Hướng Dẫn Tái Lập Phân Tích

Bạn có thể tự mình chạy lại toàn bộ quy trình phân tích này trên máy tính cá nhân chỉ với vài bước đơn giản mà không cần cài đặt máy chủ cơ sở dữ liệu phức tạp:

### Yêu Cầu Môi Trường

- Python phiên bản 3.12 trở lên
- Git
- Quyền cài đặt các gói Python thông qua `pip`

### Bước 1 — Sao Chép Kho Mã Nguồn (Clone Repo)

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

### Bước 4 — Thực Thi Phân Tích Dự Án SaaS

```bash
python -m portfolio.run --project 01_SaaS_Product_Analytics_StreamFlow
```

Lệnh này sẽ tự động:
1. Đọc và kiểm tra hợp đồng dữ liệu thô
2. Làm sạch và xuất ra `Data/clean/*.csv`
3. Tạo cơ sở dữ liệu SQLite cục bộ trong thư mục `build/`
4. Thực thi các câu lệnh SQL trong `SQL/analysis.sql`
5. Xuất các bảng kết quả ra thư mục `Results/`
6. Chạy thuật toán đối soát Python độc lập
7. Sinh báo cáo trực quan `REPORT.html`
8. Băm mã SHA-256 và cập nhật `Results/manifest.json`

### Bước 5 — Chạy Toàn Bộ Kiểm Thử Tự Động

```bash
python -m unittest discover -s tests -v
```

### Bước 6 — Xem Báo Cáo Kết Quả

- Mở trực tiếp tệp `01_SaaS_Product_Analytics_StreamFlow/REPORT.html` trên trình duyệt web bất kỳ để tương tác với báo cáo trực quan hoàn chỉnh.
- Kiểm tra các bảng kết quả chi tiết trong thư mục `Results/`.

---

## ⚠️ Giới Hạn Phân Tích & Hướng Phát Triển

### Giới Hạn Của Dữ Liệu Hiện Tại

1. **Dữ liệu mô phỏng (Synthetic Data):** Dữ liệu được sinh bằng thuật toán nhằm mục đích minh họa kỹ năng phân tích, không đại diện cho hành vi tiêu dùng thực tế của một doanh nghiệp đang vận hành ngoài đời.
2. **Doanh thu ảnh chụp (Snapshot Revenue):** Giá trị MRR và ARR phản ánh trạng thái tĩnh tại thời điểm trích xuất, chưa phải doanh thu thực tế được kiểm toán.
3. **Thiếu thông tin vòng đời trọn vẹn:** Chưa có bảng nhật ký thuê bao chi tiết theo từng tháng để vẽ biểu đồ cohort retention thực thụ.
4. **Độ phân giải thời gian ở mức ngày:** Các sự kiện chỉ được ghi nhận theo ngày (không có giờ, phút, giây), khiến việc phân tích hành vi trong cùng một ngày gặp giới hạn nhất định.
5. **Ngưỡng tương tác chưa tối ưu:** Toàn bộ khách hàng trả phí đều có dưới 20 lượt chạy workflow trong 90 ngày đầu, khiến việc so sánh nhóm cực kỳ tích cực (power user) chưa thực hiện được.

### Hướng Phát Triển Trong Tương Lai

- Xây dựng mô hình phân tích giữ chân dạng Cohort (Cohort Retention Matrix) khi có dữ liệu nhật ký gia hạn theo thời gian thực.
- Tính toán thời gian tới khi kích hoạt (Time to Activation - TTA) chính xác đến từng phút/giờ.
- Theo dõi tỷ lệ chuyển đổi từ tài khoản dùng thử/miễn phí sang trả phí (Free-to-Paid Conversion Funnel).
- Phân tích chi tiết hành vi nâng cấp (upgrade) và hạ cấp (downgrade) gói cước.
- Xây dựng dashboard Tableau kết nối trực tiếp với nguồn `Validated_Analysis.hyper` và nghiệm thu trực quan đầy đủ.

---

## 🧠 Đúc Kết Từ Dự Án

### Giá Trị Kỹ Thuật

Dự án này là minh chứng cụ thể cho năng lực:
- Truy vấn, biến đổi và phân tích dữ liệu quan hệ bằng SQL từ cơ bản đến nâng cao.
- Xây dựng pipeline kiểm tra chất lượng dữ liệu tự động bằng Python.
- Xử lý bài toán phễu chuyển đổi tuần tự theo thời gian nghiêm ngặt.
- Tính toán chính xác các chỉ số tài chính SaaS cốt lõi (MRR, ARR, Churn).
- Đối soát chéo đa tầng đảm bảo không có bất kỳ sai số nào trong báo cáo.

### Giá Trị Nghiệp Vụ

Quan trọng hơn cả kỹ thuật viết code, dự án thể hiện tư duy kinh doanh của một Data Analyst:
- Biết chuyển hóa các bài toán kinh doanh thành câu hỏi phân tích cụ thể.
- Biết hoài nghi lành mạnh trước dữ liệu: không vội vàng kết luận nguyên nhân kết quả khi dữ liệu chỉ mang tính quan sát.
- Nhận biết rõ giới hạn của bộ dữ liệu và minh bạch công bố những điều dữ liệu *không* thể trả lời.
- Đưa ra các đề xuất hành động thực tế, có thể đo lường và kiểm chứng được.

---

## 📚 Tài Liệu Hỗ Trợ

| Tài liệu | Nội dung |
|---|---|
| [Từ Điển Dữ Liệu](Docs/Data_Dictionary.md) | Giải thích các trường, kiểu dữ liệu, khóa và quy tắc kiểm thử |
| [Nguồn Gốc KPI](Docs/KPI_Lineage.md) | Công thức tính, mẫu số và mối liên kết bảng của từng chỉ số |
| [Biên Bản Đối Soát Dashboard](Docs/Dashboard_Reconciliation.md) | Trạng thái đồng bộ của các tài sản BI nguyên bản |
| [Ánh Xạ Trường Lên Visual](Docs/Dashboard_Field_Mapping.md) | Danh sách trường dữ liệu phục vụ tích hợp dashboard |
| [Hướng Dẫn Kết Nối Dashboard](Docs/Connect_To_Dashboard.md) | Các bước kết nối sổ làm việc BI với nguồn dữ liệu chuẩn |
| [Mã Nguồn SQL Phân Tích](SQL/analysis.sql) | Toàn bộ câu lệnh SQL thực thi phân tích |
| [Báo Cáo HTML Độc Lập](REPORT.html) | Báo cáo trực quan hoàn chỉnh xem ngoại tuyến |

---

## 👨‍💻 Về Tác Giả

**Bùi Nhất Phong**  
Data Analytics | Business Intelligence | SQL | Python | Phân Tích Nghiệp Vụ

Tôi đam mê việc sử dụng dữ liệu để giải quyết các bài toán kinh doanh thực tế, nâng cao độ tin cậy của hệ thống báo cáo và truyền tải những góc nhìn sâu sắc đến người ra quyết định.

Các lĩnh vực thế mạnh của tôi bao gồm: Phân tích sản phẩm kỹ thuật số, Phân tích hành vi khách hàng, Business Intelligence, Tối ưu hóa vận hành và Hỗ trợ ra quyết định dựa trên dữ liệu.

📧 [Email](mailto:buinhatphong.analytics@gmail.com)  
💼 [LinkedIn](https://www.linkedin.com/in/buinhatphong/)  
💻 [GitHub Profile](https://github.com/buinhatphong)

### 🔗 Khám Phá Thêm Các Dự Án Khác

[⬅️ Quay lại Trang Tổng Quan Portfolio](../README.md)

---

**📈 StreamFlow SaaS Product Analytics | Xây dựng bởi Bùi Nhất Phong**  
*Góc nhìn sâu sắc từ SQL. Số liệu kiểm chứng bằng Python. Quyết định phân tích minh bạch và chuẩn xác.*

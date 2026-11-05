# 🔍 Phân Tích Hành Trình Khách Hàng | Hành Vi, Phễu Chuyển Đổi & Theo Dõi Sự Kiện

### SQL • Python • Phân Tích Khách Hàng • Phân Tích Phễu • Phân Khúc Hành Vi • Chất Lượng Dữ Liệu

**Một case study phân tích hành trình khách hàng (User Journey) end-to-end, nghiên cứu sâu về hành vi người dùng, hoạt động mua hàng, phễu tuần tự theo thời gian, tỷ lệ chuyển đổi của khách hàng quay lại (returning users) và độ tin cậy của hệ thống gắn thẻ sự kiện (tracking instrumentation) bằng SQL và Python.**

![Python](https://img.shields.io/badge/Python-3.12-3776AB)
![SQL](https://img.shields.io/badge/SQL-SQLite-4479A1)
![Tableau](https://img.shields.io/badge/Tableau-Tài_Sản_Gốc-E97627)
![Phân Tích Khách Hàng](https://img.shields.io/badge/Customer-Journey_Analytics-blueviolet)
![Kiểm Tra Chất Lượng](https://img.shields.io/badge/Validation-15%2F15-success)
![Bộ Dữ Liệu](https://img.shields.io/badge/Dữ_Liệu-Mô_Phỏng-orange)

**Người thực hiện:** Bùi Nhất Phong  
**Dự án:** 05 — Phân Tích Hành Trình Khách Hàng  
**Portfolio:** [Data Analyst Portfolio](../README.md)  
**LinkedIn:** [Bùi Nhất Phong](https://www.linkedin.com/in/buinhatphong/)

---

## 📌 Tóm Tắt Dự Án (Executive Summary)

Dự án này phân tích hành vi của người dùng trải nghiệm trên một nền tảng thương mại điện tử mô phỏng, bắt đầu từ lúc đặt chân vào trang đích (Landing) cho đến khi hoàn tất đơn hàng (Purchase).

Dựa trên **6.000 hồ sơ người dùng và 17.354 sự kiện hành trình được ghi nhận**, dự án kết hợp truy vấn SQL, phân tích Python, kiểm định chuỗi thời gian sự kiện, phân khúc hành vi và xây dựng báo cáo đối soát nhằm làm sáng tỏ hành vi khách hàng và chỉ ra các điểm giới hạn của phương pháp đo lường phễu.

Trọng tâm cốt lõi của nghiên cứu là phân biệt rạch ròi giữa: **Tỷ lệ tiếp cận sự kiện đơn lẻ (Event Reach)** và **Tỷ lệ hoàn thành phễu theo đúng trình tự thời gian (Chronological Funnel Completion)**.

Dự án trả lời 5 câu hỏi nghiệp vụ quan trọng:

1. Có bao nhiêu người dùng thực sự phát sinh sự kiện mua hàng?
2. Có bao nhiêu người hoàn thành trọn vẹn phễu mua hàng theo đúng thứ tự ngày hợp lệ?
3. Tỷ lệ mua hàng khác biệt thế nào giữa khách hàng mới và khách hàng quay lại (returning users)?
4. Người dùng mất trung bình bao nhiêu ngày từ lần đầu ghé thăm đến khi chốt đơn?
5. Những vấn đề chất lượng dữ liệu nào đang cản trở việc đánh giá chính xác tỷ lệ khách hàng bỏ cuộc?

### Kết Quả Cốt Lõi

| Chỉ số kinh doanh | Kết quả xác thực |
|---|---:|
| 👥 Tổng số người dùng quan sát | 6.000 |
| 📋 Tổng số sự kiện hành trình ghi nhận | 17.354 |
| 💳 Số người dùng có sự kiện Mua hàng (Purchase) | 627 |
| 📈 Tỷ lệ mua hàng quan sát được (Observed Purchase Rate) | 10,45% |
| 🔁 Tỷ lệ mua hàng của nhóm khách quay lại (Returning Users) | 16,20% |
| 🆕 Tỷ lệ mua hàng của nhóm khách không quay lại | 8,26% |
| ⏱️ Số ngày chuyển đổi trung vị (Median Days to Purchase) | 7 ngày |
| 📅 Phân vị 90 (P90) số ngày chuyển đổi | 12 ngày |
| ⚠️ Số người dùng bị lỗi đảo ngược ngày giữa các bước liên tiếp | 3.296 người (54,93%) |
| 🔎 Số hành trình hoàn tất 6 bước tuần tự nghiêm ngặt | **0 người** |
| ✅ Bài kiểm thử dữ liệu & logic đã vượt qua | 15/15 passed |

**Công bố về dữ liệu:** Dự án sử dụng dữ liệu mô phỏng phục vụ portfolio. Kết quả không đại diện cho hành vi tiêu dùng thật hay hệ thống production của một doanh nghiệp ngoài đời thực.

### Các Phát Hiện Quan Trọng

**1. Ghi nhận 627 người dùng thực tế đã mua hàng:**  
Trong tổng số 6.000 người dùng, có 627 người xuất hiện sự kiện `Purchase`, tương ứng với **tỷ lệ mua hàng quan sát được là 10,45%**.

**2. Khách hàng quay lại có tỷ lệ mua hàng cao vượt trội:**  
Nhóm khách hàng quay lại (returning users) đạt tỷ lệ mua hàng **16,20%**, cao gần gấp đôi so với mức **8,26%** của nhóm khách hàng không quay lại (chênh lệch 7,94 điểm phần trăm). Đây là mối liên hệ quan sát có giá trị lớn cho các chiến dịch remarketing.

**3. Nghịch lý giữa số người mua thực tế và phễu tuần tự thời gian:**  
Mặc dù có tới 627 người mua hàng thực tế, nhưng khi áp dụng mô hình phễu tuần tự nghiêm ngặt (ngày bước sau phải lớn hơn hoặc bằng ngày bước trước), kết quả lại cho ra **0 người hoàn thành trọn vẹn 6 bước**.

**4. Dữ liệu sự kiện bị lỗi đảo ngược thời gian nghiêm trọng:**  
Có tới **3.296 người dùng (54,93%)** gặp hiện tượng bước sau lại có ngày ghi nhận diễn ra *trước* bước trước (adjacent-stage date inversion). Nguyên nhân xuất phát từ việc dữ liệu chỉ ghi nhận ở mức ngày (không có giờ, phút, giây) và hệ thống tracking có thể bị trễ khi gửi log sự kiện.

### Kết Luận Kinh Doanh

Khuyến nghị quan trọng nhất của dự án là: **Đội ngũ sản phẩm phải rà soát lại hệ thống gắn thẻ sự kiện (tracking instrumentation) và độ phân giải mốc thời gian trước khi kết luận khách hàng đang gặp lỗi thanh toán**.  
Case study này là bài học đắt giá cho thấy: code SQL có thể chạy đúng 100% logic, nhưng nếu dữ liệu đầu vào bị lỗi thứ tự thời gian thì kết luận kinh doanh rút ra sẽ hoàn toàn sai lệch!

---

## 📚 Mục Lục

1. [Bài Toán Nghiệp Vụ](#-bài-toán-nghiệp-vụ)
2. [Tổng Quan Bộ Dữ Liệu](#-tổng-quan-bộ-dữ-liệu)
3. [Bộ Công Cụ Kỹ Thuật (Tech Stack)](#-bộ-công-cụ-kỹ-thuật-tech-stack)
4. [Quy Trình Phân Tích End-to-End](#-quy-trình-phân-tích-end-to-end)
5. [Định Nghĩa KPI & Quy Tắc Nghiệp Vụ](#-định-nghĩa-kpi--quy-tắc-nghiệp-vụ)
6. [Phân Tích 1: Tổng Quan Hoạt Động Mua Hàng](#-phân-tích-1-tổng-quan-hoạt-động-mua-hàng)
7. [Phân Tích 2: Tỷ Lệ Tiếp Cận Từng Bước Hành Trình (Stage Reach)](#-phân-tích-2-tỷ-lệ-tiếp-cận-từng-bước-hành-trình-stage-reach)
8. [Phân Tích 3: Phễu Tuần Tự Theo Thời Gian (Ordered Funnel)](#-phân-tích-3-phễu-tuần-tự-theo-thời-gian-ordered-funnel)
9. [Phân Tích 4: Chuyển Đổi Nhóm Khách Hàng Quay Lại (Returning Users)](#-phân-tích-4-chuyển-đổi-nhóm-khách-hàng-quay-lại-returning-users)
10. [Phân Tích 5: Thời Gian Từ Lúc Ghé Thăm Đến Khi Chốt Đơn](#-phân-tích-5-thời-gian-từ-lúc-ghé-thăm-đến-khi-chốt-đơn)
11. [Phân Tích 6: Chất Lượng Dữ Liệu & Sai Lệch Thứ Tự Thời Gian](#-phân-tích-6-chất-lượng-dữ-liệu--sai-lệch-thứ-tự-thời-gian)
12. [Hiện Thực Hóa Bằng SQL](#-hiện-thực-hóa-bằng-sql)
13. [Phân Tích Bằng Python & Đối Soát Số Liệu](#-phân-tích-bằng-python--đối-soát-số-liệu)
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

Các doanh nghiệp số cần theo dõi sát sao cách người dùng tương tác trên website: từ lúc vào trang chủ, tìm kiếm danh mục, xem chi tiết sản phẩm, bỏ vào giỏ hàng, điền thông tin thanh toán cho đến khi bấm mua hàng.

Phân tích hành trình khách hàng (User Journey Analytics) giúp doanh nghiệp trả lời:
- Người dùng tìm thấy sản phẩm như thế nào?
- Hành vi lướt xem hàng và tương tác với trang sản phẩm ra sao?
- Tỷ lệ rơi rụng ở từng bước trong phễu mua sắm là bao nhiêu?
- Khách hàng quay lại (returning users) có hành vi mua sắm khác gì so với khách mới?
- Khách hàng mất bao lâu để đưa ra quyết định mua hàng?

Tuy nhiên, việc đo lường hành trình khách hàng đòi hỏi dữ liệu sự kiện phải chuẩn xác về cả danh tính lẫn mốc thời gian. Nếu hệ thống tracking bị lỗi thứ tự thời gian, phễu chuyển đổi sẽ hiển thị tỷ lệ rơi rụng ảo, khiến doanh nghiệp chẩn đoán sai hoàn toàn điểm nghẽn của sản phẩm.

### Câu Hỏi Nghiệp Vụ Cốt Lõi

**Hành vi mua hàng thực tế của khách hàng so với mô hình phễu tuần tự thời gian nghiêm ngặt có gì mâu thuẫn, và những điểm mâu thuẫn đó phản ánh điều gì về chất lượng của hệ thống đo lường hành trình người dùng?**

---

## 🗄️ Tổng Quan Bộ Dữ Liệu

Dự án sử dụng 2 bảng dữ liệu mô phỏng gồm tổng cộng **23.354 bản ghi**.

### Bảng Dữ Liệu Nguồn

| Bảng dữ liệu | Số bản ghi | Mục đích sử dụng |
|---|---:|---|
| `users_raw.csv` | 6.000 | Thuộc tính tài khoản, ngày quan sát đầu tiên, thiết bị và cờ khách quay lại |
| `journey_events_raw.csv` | 17.354 | Nhật ký các sự kiện hành trình và ngày diễn ra sự kiện |
| **Tổng cộng** | **23.354** | **2 bảng dữ liệu liên kết** |

### 1. Bảng Users (Người Dùng)

Mỗi dòng đại diện cho một người dùng độc lập.

| Cột | Kiểu dữ liệu | Ý nghĩa nghiệp vụ |
|---|---|---|
| `user_id` | Integer | Mã định danh duy nhất của người dùng trong tập dữ liệu |
| `first_seen_date` | Date | Ngày quan sát đầu tiên được ghi nhận |
| `traffic_source` | Text | Kênh nguồn mang lại người dùng (Direct, Organic, Paid, Referral, Social) |
| `device` | Text | Thiết bị sử dụng (Desktop, Mobile, Tablet) |
| `is_returning` | Binary | Cờ nhị phân: 1 nếu là khách hàng quay lại, 0 nếu là khách mới |

### 2. Bảng Journey Events (Sự Kiện Hành Trình)

Ghi nhận các hành động người dùng thực hiện trên nền tảng.

| Cột | Kiểu dữ liệu | Ý nghĩa nghiệp vụ |
|---|---|---|
| `user_id` | Integer | Mã người dùng thực hiện hành động |
| `event_date` | Date | Ngày diễn ra sự kiện (mức ngày YYYY-MM-DD) |
| `journey_stage` | Text | Tên giai đoạn hành trình |
| `stage_order` | Integer | Số thứ tự danh nghĩa của giai đoạn |

### 7 Giai Đoạn Hành Trình Trong Dữ Liệu

Dữ liệu nguồn ghi nhận 7 nhãn sự kiện:
1. `Landing` (Trang đích)
2. `Browse` (Lướt xem danh mục)
3. `Product View` (Xem chi tiết sản phẩm)
4. `Add to Cart` (Thêm hàng vào giỏ)
5. `Checkout` (Bắt đầu thanh toán)
6. `Purchase` (Mua hàng thành công)
7. `Signup` (Đăng ký tài khoản)

### Quy Tắc Nghiệp Vụ Về Luồng Mua Hàng Chuẩn

Phễu thương mại điện tử cốt lõi sử dụng 6 giai đoạn:

**Landing → Browse → Product View → Add to Cart → Checkout → Purchase**

Sự kiện **Signup (Đăng ký tài khoản)** được tách riêng để phân tích độc lập. Dữ liệu thực tế cho thấy rất nhiều khách hàng mua hàng xong mới đăng ký tài khoản (hoặc mua dạng khách vãng lai), do đó việc ép buộc Signup phải là bước cuối cùng của phễu thương mại là một quy tắc phi thực tế và thiếu cơ sở.

### Ranh Giới & Giới Hạn Của Grain Dữ Liệu

- **Độ phân giải thời gian ở mức ngày:** Các sự kiện chỉ có ngày (YYYY-MM-DD), không có giờ phút giây. Nếu người dùng thực hiện nhiều bước trong cùng 1 ngày, ta không thể biết chắc chắn bước nào diễn ra trước bằng mắt thường.
- **Không có mã phiên (session_id):** Không thể xác định các bước diễn ra trong cùng một phiên hay trải dài qua nhiều ngày ghé thăm khác nhau.
- **Không có mã sự kiện duy nhất (event_id):** Không hỗ trợ kiểm tra tính duy nhất ở mức từng cú nhấp chuột.

Tài liệu chi tiết: [📘 Từ Điển Dữ Liệu](Docs/Data_Dictionary.md) | [📂 Dữ Liệu Thô](Data/raw) | [📂 Dữ Liệu Đã Làm Sạch](Data/clean)

---

## 🛠️ Bộ Công Cụ Kỹ Thuật (Tech Stack)

| Hạng mục | Công nghệ | Ứng dụng thực tế |
|---|---|---|
| Ngôn ngữ lập trình | Python 3.12 | Chuẩn hóa dữ liệu, kiểm thử tự động, phân vị thống kê |
| Ngôn ngữ truy vấn | SQL | Phân tích phễu tuần tự CTE, tính toán số ngày bằng hàm ngày tháng |
| Cơ sở dữ liệu | SQLite | Thực thi truy vấn phân tích quan hệ cục bộ |
| Xử lý dữ liệu | pandas | Đối soát chéo độc lập giữa Python và SQL |
| Trực quan hóa dữ liệu | Tableau | Tệp dashboard `.twbx` nguyên bản và tệp trích xuất Hyper chuẩn hóa |
| Bảng tính Excel | Excel | Sổ tính toán đối soát công thức và mô hình tóm tắt |
| Thống kê mô tả | Quantiles | Tính toán phân vị trung vị (P50) và P90 của thời gian chốt đơn |
| Báo cáo kết quả | HTML & CSV | Xuất bảng kết quả và báo cáo tương tác ngoại tuyến |
| Đảm bảo chất lượng | Python unittest | Bộ kiểm thử tự động toàn diện (15 bài test) |
| Bảo toàn dữ liệu | SHA-256 | Băm mã cryptographic bảo đảm tính toàn vẹn 100% |

---

## 🔄 Quy Trình Phân Tích End-to-End

1. **Xác định câu hỏi kinh doanh:** Phân biệt rõ sự khác nhau giữa tỷ lệ tiếp cận sự kiện (reach) và phễu tuần tự (ordered funnel).
2. **Khảo sát dữ liệu thô:** Kiểm tra định dạng ngày, nhãn giai đoạn, số thứ tự danh nghĩa và mối liên kết bảng qua `user_id`.
3. **Làm sạch & Chuẩn hóa:** Ép kiểu ngày, loại bỏ khoảng trắng thừa, kiểm tra tính duy nhất của khóa chính `user_id` và xuất dữ liệu sạch ra `Data/clean/*.csv`. Giữ nguyên dữ liệu thô ban đầu.
4. **Phân tích bằng SQL:** Chạy 5 câu truy vấn phân tích chính: Tỷ lệ mua hàng quan sát, Tỷ lệ tiếp cận từng bước, Phễu tuần tự nghiêm ngặt, Chuyển đổi khách quay lại, và Thời gian tới khi chốt đơn.
5. **Kiểm tra chất lượng chuỗi thời gian:** Phát hiện và thống kê các trường hợp nghịch đảo thời gian giữa các bước liên tiếp.
6. **Đối soát chéo bằng Python:** Viết lại thuật toán bằng Python để kiểm tra từng con số với kết quả của SQL.
7. **Đọc hiểu & Khuyến nghị:** Đưa ra giải pháp nâng cấp hệ thống gắn thẻ sự kiện (tracking instrumentation).
8. **Xuất báo cáo & Manifest:** Tự động sinh báo cáo HTML trực quan và cập nhật mã băm SHA-256.

---

## 📐 Định Nghĩa KPI & Quy Tắc Nghiệp Vụ

| KPI | Công thức tính toán | Cách hiểu đúng |
|---|---|---|
| Tổng số người dùng | Đếm số dòng trong bảng users | Tập khách hàng quan sát được |
| Người mua hàng quan sát được | Đếm số `user_id` duy nhất có sự kiện `Purchase` | Số người có mua hàng, không xét thứ tự các bước trước |
| Tỷ lệ mua hàng quan sát được | Người mua hàng ÷ Tổng số người dùng | Tỷ lệ chuyển đổi tổng thể mô tả |
| Tỷ lệ tiếp cận bước (Stage Reach) | Số `user_id` duy nhất ghi nhận sự kiện ở bước đó | Khảo sát mức độ tham gia, không đòi hỏi bước trước |
| Phễu tuần tự (Ordered Funnel) | Số người dùng hoàn thành lần lượt các bước theo ngày không giảm | Điều kiện phễu nghiêm ngặt theo thời gian |
| Tỷ lệ mua của khách quay lại | Số người mua nhóm quay lại ÷ Tổng khách quay lại | Đánh giá hiệu quả nhóm khách hàng thân thiết |
| Số ngày tới khi chốt đơn | Ngày mua đầu tiên − Ngày quan sát đầu tiên (`first_seen_date`) | Thời gian cân nhắc mua hàng thực tế |
| Trung vị số ngày (Median Days) | Phân vị 50 (P50) của chuỗi số ngày mua hàng hợp lệ | Con số đại diện tiêu biểu cho thời gian chốt đơn |
| Nghịch đảo ngày giữa 2 bước | Bước danh nghĩa sau lại có ngày nhỏ hơn bước danh nghĩa trước | Chỉ báo chẩn đoán lỗi gắn thẻ sự kiện |

Chi tiết quy tắc: [Nguồn Gốc KPI (KPI Lineage)](Docs/KPI_Lineage.md)

---

## 💳 Phân Tích 1: Tổng Quan Hoạt Động Mua Hàng

### Câu Hỏi Nghiệp Vụ

Thực tế có bao nhiêu khách hàng đã phát sinh giao dịch mua hàng trên hệ thống?

### Kết Quả Đối Soát

| Chỉ số | Kết quả xác thực |
|---|---:|
| Tổng số người dùng | 6.000 |
| Số người dùng có sự kiện Mua hàng (Purchase) | 627 |
| Số người dùng không ghi nhận sự kiện Mua hàng | 5.373 |
| **Tỷ lệ mua hàng quan sát được (Observed Purchase Rate)** | **10,45%** |

### Công Thức Tính Tỷ Lệ Mua Hàng

\[
\text{Tỷ lệ mua hàng quan sát được} = \frac{627}{6.000} \times 100\% = 10,45\%
\]

### Các Phát Hiện Quan Trọng

- **Khách hàng thực sự có mua hàng:** Có 627 người dùng riêng biệt phát sinh sự kiện mua hàng. Đây là bằng chứng không thể chối cãi về việc sản phẩm có tạo ra chuyển đổi thương mại.
- **Tỷ lệ mua hàng cơ sở đạt 10,45%:** Trong số 6.000 người ghé thăm được theo dõi, cứ 10 người thì có khoảng 1 người thực hiện mua hàng.
- **Không được xóa bỏ sự thật này:** Dù phễu tuần tự sau này có cho ra kết quả là 0 người (do lỗi thứ tự ngày), một chuyên viên phân tích dữ liệu có trách nhiệm vẫn phải khẳng định rằng 627 người này thực sự đã mua hàng, và lỗi nằm ở hệ thống đo lường chứ không phải khách hàng không mua!

**Bằng chứng truy vấn:** [Tổng quan mua hàng (summary.csv)](Results/summary.csv)

---

## 🧭 Phân Tích 2: Tỷ Lệ Tiếp Cận Từng Bước Hành Trình (Stage Reach)

### Câu Hỏi Nghiệp Vụ

Có bao nhiêu người dùng duy nhất từng tham gia vào từng bước của hành trình mua sắm (không quan tâm họ có làm theo đúng thứ tự hay không)?

### Bảng Kết Quả Tiếp Cận Từng Bước (Stage Reach)

| Giai đoạn hành trình | Số người dùng duy nhất | Tỷ lệ tiếp cận trên tổng số người |
|---|---:|---:|
| 1. Trang đích (Landing) | 6.000 | 100,00% |
| 2. Xem danh mục (Browse) | 4.346 | 72,43% |
| 3. Xem chi tiết sản phẩm (Product View) | 2.923 | 48,72% |
| 4. Thêm hàng vào giỏ (Add to Cart) | 1.883 | 31,38% |
| 5. Bắt đầu thanh toán (Checkout) | 1.174 | 19,57% |
| 6. Mua hàng thành công (Purchase) | 627 | 10,45% |
| *Đăng ký tài khoản (Signup)* | 401 | 6,68% |

### Các Phát Hiện Quan Trọng

1. **100% người dùng đều có sự kiện Landing:** Toàn bộ 6.000 người dùng đều ghi nhận điểm chạm đầu tiên tại trang đích.
2. **Gần 3/4 người dùng có lướt xem danh mục:** 4.346 người (72,43%) có hành vi tìm kiếm hàng hóa.
3. **Gần một nửa xem chi tiết sản phẩm:** 2.923 người (48,72%) xem cụ thể một món hàng.
4. **Hơn 31% thêm hàng vào giỏ và gần 20% vào trang checkout:** Các bước thể hiện ý định mua hàng thu hút lượng lớn người dùng tham gia.
5. **Signup là hành vi độc lập:** Chỉ có 401 người đăng ký tài khoản, trong khi có tới 627 người mua hàng. Điều này chứng minh website cho phép mua hàng dạng vãng lai (guest checkout) hoặc việc đăng ký tài khoản không phải là điều kiện bắt buộc để hoàn tất đơn hàng.

**Bằng chứng truy vấn:** [Tiếp cận từng bước (stage_reach.csv)](Results/stage_reach.csv)

---

## 🚦 Phân Tích 3: Phễu Tuần Tự Theo Thời Gian (Ordered Funnel)

### Câu Hỏi Nghiệp Vụ

Có bao nhiêu người dùng hoàn thành lần lượt 6 bước của hành trình mua hàng theo đúng trình tự thời gian hợp lệ?

### Luồng Phễu Chuẩn Xác Thực

**Landing → Browse → Product View → Add to Cart → Checkout → Purchase**  
(Quy tắc: Ngày bước sau \(\ge\) Ngày bước trước \(\ge\) `first_seen_date`).

### Kết Quả Phễu Tuần Tự Nghiêm Ngặt

| Giai đoạn | Số người dùng đủ điều kiện | Tỷ lệ giữ chân từ bước trước |
|---|---:|---:|
| Bước 1: Landing | 6.000 | Mốc chuẩn (Baseline) |
| Bước 2: Browse | 2.304 | 38,40% |
| Bước 3: Product View | 590 | 25,61% |
| Bước 4: Add to Cart | 102 | 17,29% |
| Bước 5: Checkout | 12 | 11,76% |
| Bước 6: Purchase | **0** | **0,00%** |

### Chẩn Đoán Tỷ Lệ Rơi Rụng Giữa Các Bước Tuần Tự

| Bước chuyển tiếp | Số người bị loại | Tỷ lệ rơi rụng điều kiện |
|---|---:|---:|
| Landing → Browse | 3.696 | 61,60% |
| Browse → Product View | 1.714 | 74,39% |
| Product View → Add to Cart | 488 | 82,71% |
| Add to Cart → Checkout | 90 | 88,24% |
| Checkout → Purchase | 12 | **100,00%** |

### Sự Khác Biệt Giữa "Phễu Tiếp Cận" Và "Phễu Tuần Tự"

Hãy so sánh hai con số:
- Ở bước Browse: Có **4.346 người** có sự kiện Browse, nhưng chỉ có **2.304 người** có sự kiện Browse diễn ra vào ngày bằng hoặc sau ngày Landing!
- Ở bước Product View: Có **2.923 người** có sự kiện, nhưng chỉ có **590 người** thỏa mãn chuỗi Landing → Browse → Product View.
- Đến bước Checkout: Chỉ còn đúng **12 người** thỏa mãn chuỗi 5 bước đầu.
- Và ở bước Purchase: **Không có bất kỳ ai trong số 12 người này có sự kiện Purchase vào ngày bằng hoặc sau ngày Checkout!**

### Diễn Giải Bản Chất Vấn Đề

**Con số 0 người hoàn thành phễu tuần tự KHÔNG CÓ NGHĨA là không có ai mua hàng!**  
Thực tế đã chứng minh có 627 người mua hàng. Con số 0 này là bằng chứng rõ ràng nhất cho thấy: **Mô hình phễu tuần tự nghiêm ngặt đang bị phá vỡ hoàn toàn bởi sự cố dữ liệu ghi nhận sai lệch thứ tự thời gian.**  
Nếu một Data Analyst thiếu kinh nghiệm nhìn vào bảng này và báo cáo với ban giám đốc rằng "100% khách hàng vào trang thanh toán đều bỏ cuộc", đó sẽ là một sai lầm chết người!

**Bằng chứng truy vấn:** [Phễu tuần tự (ordered_funnel.csv)](Results/ordered_funnel.csv)

---

## 🔁 Phân Tích 4: Chuyển Đổi Nhóm Khách Hàng Quay Lại (Returning Users)

### Câu Hỏi Nghiệp Vụ

Tỷ lệ mua hàng của nhóm khách hàng quay lại khác biệt như thế nào so với nhóm khách mới?

### Kết Quả Đối Soát

| Nhóm khách hàng | Số lượng người dùng | Số người mua hàng | Tỷ lệ mua hàng quan sát được |
|---|---:|---:|---:|
| Khách mới (Non-Returning) | 4.346 | 359 | 8,26% |
| Khách quay lại (Returning) | 1.654 | 268 | **16,20%** |
| **Tổng cộng** | **6.000** | **627** | **10,45%** |

### Các Phát Hiện Quan Trọng

1. **Khách hàng quay lại có tỷ lệ chuyển đổi cao gần gấp đôi:** Nhóm khách quay lại đạt tỷ lệ mua **16,20%**, cao hơn nhóm khách mới (8,26%) tới **7,94 điểm phần trăm**.
2. **Hệ số chuyển đổi đạt 1,96 lần:**
   \[
   \frac{16,20\%}{8,26\%} \approx 1,96
   \]
   Xác suất mua hàng của khách quay lại cao gấp gần 2 lần so với khách mới ghé thăm lần đầu.
3. **Cảnh báo về tính nhân quả:** Đây là mối liên hệ quan sát được. Người dùng quay lại nhiều lần vốn dĩ đã có nhu cầu mua sắm cao hơn hoặc đã tin tưởng thương hiệu từ trước. Ta không thể khẳng định việc "bắt khách hàng quay lại" sẽ tự động biến họ thành người mua hàng.

**Bằng chứng truy vấn:** [Khách quay lại (returning_user_conversion.csv)](Results/returning_user_conversion.csv)

---

## ⏱️ Phân Tích 5: Thời Gian Từ Lúc Ghé Thăm Đến Khi Chốt Đơn

### Câu Hỏi Nghiệp Vụ

Khách hàng mất bao nhiêu ngày kể từ lần đầu xuất hiện trên hệ thống cho đến khi hoàn tất đơn hàng đầu tiên?

### Công Thức Đo Lường

\[
\text{Số ngày chốt đơn} = \text{Ngày mua hợp lệ đầu tiên} - \text{first\_seen\_date}
\]
(Chỉ tính trên tập 627 người dùng có phát sinh giao dịch mua hàng hợp lệ).

### Kết Quả Thống Kê Phân Vị

| Thước đo thời gian | Kết quả tính toán | Ý nghĩa thực tế |
|---|---:|---|
| **Trung vị số ngày (Median / P50)** | **7 ngày** | 50% người mua hàng chốt đơn trong vòng 7 ngày đầu |
| **Phân vị 90 (P90)** | **12 ngày** | 90% người mua hàng chốt đơn trong vòng 12 ngày |
| Độ phân giải dữ liệu | Mức ngày (Days) | Không có giờ phút giây |

### Các Phát Hiện Quan Trọng

- **Khách hàng cần thời gian cân nhắc:** Mốc trung vị là 7 ngày cho thấy hành vi mua sắm trên nền tảng không phải là mua sắm bốc đồng tức thì (impulse buying), mà người dùng thường lướt xem, so sánh giá và quay lại chốt đơn sau khoảng 1 tuần.
- **Cửa sổ vàng chuyển đổi là 12 ngày:** 90% các đơn hàng diễn ra trong vòng 12 ngày đầu tiên. Đây là căn cứ cực kỳ quan trọng để đội ngũ Marketing thiết lập lịch trình gửi email nhắc nhở giỏ hàng hoặc chạy quảng cáo bám đuổi (retargeting) trong khoảng 7–10 ngày sau lần ghé thăm đầu tiên.

**Bằng chứng truy vấn:** [Thời gian chốt đơn (time_to_purchase.csv)](Results/time_to_purchase.csv) | [Chỉ số bổ trợ (additional_metrics.json)](Results/additional_metrics.json)

---

## ⚠️ Phân Tích 6: Chất Lượng Dữ Liệu & Sai Lệch Thứ Tự Thời Gian

### Câu Hỏi Nghiệp Vụ

Hệ thống ghi nhận sự kiện có đảm bảo thứ tự thời gian logic của các hành động hay không?

### Bảng Thống Kê Sai Lệch Chất Lượng Dữ Liệu

| Chỉ số kiểm tra | Kết quả ghi nhận | Đánh giá |
|---|---:|---|
| Tổng số người dùng | 6.000 | Chuẩn |
| Tổng số dòng sự kiện | 17.354 | Chuẩn |
| Sự kiện xảy ra trước `first_seen_date` | 0 | Hợp lệ 100% |
| **Số người dùng bị đảo ngược ngày giữa các bước** | **3.296 người** | **Lỗi nghiêm trọng (54,93%)** |
| Số hành trình hoàn tất 6 bước tuần tự | 0 người | Cảnh báo hệ thống đo lường |
| Số người mua hàng thực tế | 627 người | Thực tế quan sát được |

### Bản Chất Hiện Tượng Đảo Ngược Ngày (Adjacent-Stage Date Inversion)

Hiện tượng này xảy ra khi một bước có số thứ tự danh nghĩa lớn hơn (ví dụ Bước 4: Add to Cart) lại có ngày ghi nhận diễn ra *trước* bước danh nghĩa nhỏ hơn (ví dụ Bước 3: Product View)!  
Có tới **3.296 người dùng (54,93%)** gặp tình trạng này trong lịch sử dữ liệu.

### Nguyên Nhân Cốt Lõi

1. **Độ phân giải thời gian quá thô:** Dữ liệu chỉ ghi nhận ngày (YYYY-MM-DD) mà không có timestamp chi tiết (giờ:phút:giây).
2. **Hệ thống tracking bất đồng bộ:** Nhật ký sự kiện có thể được gửi theo lô (batch logging) hoặc bị trễ mạng, dẫn đến việc sự kiện gửi sau lại mang ngày ghi nhận lệch với thực tế.
3. **Khách hàng quay lại mua sắm nhiều lần:** Người dùng có thể đã thêm vào giỏ hàng từ tuần trước, tuần này quay lại trang chủ rồi bấm mua luôn. Khi đó, sự kiện Browse mới có ngày mới hơn sự kiện Add to Cart cũ!

### Quyết Định Đạo Đức Của Data Analyst

Một chuyên viên dữ liệu trung thực tuyệt đối không được tự ý sửa ngày tháng trong cơ sở dữ liệu để làm đẹp phễu chuyển đổi. Phân tích chọn phương án công bố minh bạch thực trạng này và yêu cầu bộ phận kỹ thuật nâng cấp hệ thống tracking.

**Bằng chứng đối soát:** [Báo cáo chất lượng (quality.json)](Results/quality.json)

---

## 💻 Hiện Thực Hóa Bằng SQL

5 câu truy vấn SQLite chuẩn được lưu trữ trong `SQL/analysis.sql`:

### Truy Vấn 1 — Tính Tỷ Lệ Mua Hàng Quan Sát Được

```sql
SELECT
    COUNT(*) AS users,

    (
        SELECT COUNT(DISTINCT user_id)
        FROM journey_events_clean
        WHERE journey_stage = 'Purchase'
    ) AS purchasers,

    1.0 * (
        SELECT COUNT(DISTINCT user_id)
        FROM journey_events_clean
        WHERE journey_stage = 'Purchase'
    ) / NULLIF(COUNT(*), 0)
        AS observed_purchase_rate

FROM users_clean;
```

### Truy Vấn 2 — Phễu Tuần Tự Nghiêm Ngặt Bằng Chuỗi CTE Kế Tiếp

```sql
WITH s0 AS (
    SELECT user_id, first_seen_date AS reached
    FROM users_clean
),

s1 AS (
    SELECT p.user_id,
        (SELECT MIN(e.event_date) FROM journey_events_clean e
         WHERE e.user_id = p.user_id AND e.journey_stage = 'Landing' AND e.event_date >= p.reached) AS reached
    FROM s0 p WHERE p.reached IS NOT NULL
),

s2 AS (
    SELECT p.user_id,
        (SELECT MIN(e.event_date) FROM journey_events_clean e
         WHERE e.user_id = p.user_id AND e.journey_stage = 'Browse' AND e.event_date >= p.reached) AS reached
    FROM s1 p WHERE p.reached IS NOT NULL
),

s3 AS (
    SELECT p.user_id,
        (SELECT MIN(e.event_date) FROM journey_events_clean e
         WHERE e.user_id = p.user_id AND e.journey_stage = 'Product View' AND e.event_date >= p.reached) AS reached
    FROM s2 p WHERE p.reached IS NOT NULL
)

SELECT COUNT(reached) AS users_through_product_view FROM s3;
```

### Truy Vấn 3 — So Sánh Chuyển Đổi Khách Mới & Khách Quay Lại

```sql
WITH p AS (
    SELECT DISTINCT user_id
    FROM journey_events_clean
    WHERE journey_stage = 'Purchase'
)

SELECT
    u.is_returning,
    COUNT(*) AS users,
    COUNT(p.user_id) AS purchasers,
    1.0 * COUNT(p.user_id) / COUNT(*) AS purchase_rate
FROM users_clean u
LEFT JOIN p USING(user_id)
GROUP BY u.is_returning
ORDER BY u.is_returning;
```

### Truy Vấn 4 — Tính Số Ngày Từ Lúc Ghé Thăm Đến Khi Chốt Đơn

```sql
SELECT
    u.user_id,
    MIN(e.event_date) AS first_purchase_date,
    julianday(MIN(e.event_date)) - julianday(u.first_seen_date) AS days_to_purchase
FROM users_clean u
JOIN journey_events_clean e USING(user_id)
WHERE e.journey_stage = 'Purchase'
  AND e.event_date >= u.first_seen_date
GROUP BY u.user_id
ORDER BY u.user_id;
```

### Truy Vấn 5 — Tiếp Cận Từng Bước Hành Trình Độc Lập

```sql
SELECT
    journey_stage,
    COUNT(DISTINCT user_id) AS users
FROM journey_events_clean
GROUP BY journey_stage
ORDER BY users DESC;
```

**Xem toàn bộ mã nguồn SQL:** [SQL/analysis.sql](SQL/analysis.sql)

---

## 🐍 Phân Tích Bằng Python & Đối Soát Số Liệu

Mô-đun Python đóng vai trò kiểm định đa tầng:
- Đọc và làm sạch 2 bảng dữ liệu nguồn.
- Kiểm tra hợp đồng kiểu dữ liệu và toàn vẹn quan hệ qua `user_id`.
- Tính toán các phân vị thống kê thời gian chốt đơn bằng phương pháp phân vị tuyến tính của pandas:
  - Median = 7 ngày
  - P90 = 12 ngày
- Chạy thuật toán phát hiện lỗi đảo ngược thời gian và xuất báo cáo `quality.json`.
- Đối soát chéo từng con số với kết quả của SQL.

---

## 💡 Khuyến Nghị Kinh Doanh

### Bảng Ưu Tiên Hành Động

| Mức ưu tiên | Đề xuất hành động | Bằng chứng dữ liệu hỗ trợ | Phương án kiểm chứng |
|---|---|---|---|
| 🔴 Cấp thiết | Kiểm toán lại hệ thống tracking sự kiện | 3.296 người dùng bị lỗi đảo ngược ngày | Rà soát cơ chế gửi log và múi giờ server |
| 🔴 Cấp thiết | Bổ sung Timestamp chi tiết tới giây | Chỉ có ngày YYYY-MM-DD | Nâng cấp SDK tracking sự kiện |
| 🔴 Rất cao | Không dùng phễu tuần tự làm KPI đánh giá checkout | Phễu tuần tự ra 0 dù có 627 người mua | Dùng Stage Reach kết hợp phân tích phiên |
| 🟡 Trung bình | Thiết lập chiến dịch Re-marketing trong 7–12 ngày | Median chốt đơn là 7 ngày, P90 là 12 ngày | Gửi email nhắc nhở sau 3 ngày và 7 ngày |
| 🟡 Trung bình | Đẩy mạnh chương trình giữ chân khách hàng quay lại | Khách quay lại chuyển đổi cao gấp 1,96 lần | Tối ưu hóa chương trình khách hàng thân thiết |

### Lộ Trình Triển Khai 30 / 60 / 90 Ngày

- **Ngày 1–30 (Khảo sát kỹ thuật):** Làm việc với đội ngũ Kỹ thuật phần mềm để bổ sung trường `timestamp` (độ chính xác đến mili-giây) và `session_id` cho từng sự kiện.
- **Ngày 31–60 (Chuẩn hóa đo lường):** Tách bạch giữa các phiên ghé thăm khác nhau của cùng một người dùng (Sessionization). Xác định các luồng mua sắm hợp lệ cho phép bỏ qua bước xem danh mục.
- **Ngày 61–90 (Tái lập phễu chuẩn):** Xây dựng lại phễu chuyển đổi chuẩn trên nền tảng dữ liệu mới. Bắt đầu tối ưu hóa giao diện dựa trên dữ liệu phễu đã được xác thực.

---

## ✅ Chất Lượng Dữ Liệu & Đối Soát

| Tiêu chí chất lượng | Kết quả ghi nhận |
|---|---:|
| Bản ghi người dùng (Users) | 6.000 dòng |
| Bản ghi sự kiện hành trình (Journey Events) | 17.354 dòng |
| Tổng số dòng dữ liệu nguồn | 23.354 dòng |
| Số ô dữ liệu bắt buộc bị thiếu | 0 ô |
| Sự kiện phát sinh trước `first_seen_date` | 0 trường hợp |
| Người dùng bị lỗi đảo ngược ngày giữa các bước | 3.296 người (cảnh báo chất lượng) |
| Số bài kiểm thử tự động vượt qua | 15/15 passed |

**Các tệp kết quả kiểm thử:**
- [validation.json](Results/validation.json) — Biên bản kiểm thử kỹ thuật và đối soát số liệu
- [quality.json](Results/quality.json) — Báo cáo các phát hiện sai lệch thứ tự thời gian
- [manifest.json](Results/manifest.json) — Mã băm cryptographic SHA-256 bảo đảm tính toàn vẹn

---

## 📊 Tài Sản Business Intelligence & Dashboard

| Tài sản | Vị trí | Mục đích sử dụng |
|---|---|---|
| Sổ làm việc Excel | [Excel Model](Excel/05_User_Journey_Analytics_Model.xlsx) | Sổ tính toán đối soát công thức chuẩn |
| Tệp Tableau TWBX cũ | [Tableau Dashboard](Dashboard/User_Journey_Tableau_Dashboard.twbx) | Dashboard nguyên bản phục vụ kiểm toán |
| Tệp trích xuất Hyper chuẩn hóa | [Validated_Analysis.hyper](Dashboard/Validated_Analysis.hyper) | Dữ liệu nguồn chuẩn hóa phục vụ tạo lại visual |
| Ảnh chụp hành trình | [Thư mục Images](Images/user_journey.png) | Ảnh chụp biểu đồ hành trình tham khảo |
| Báo cáo HTML độc lập | [REPORT.html](REPORT.html) | Báo cáo trực quan độc lập hoàn chỉnh |

### Trạng Thái Đối Soát Dashboard Tableau Gốc

Rà soát kỹ thuật cho thấy dashboard Tableau gốc sử dụng một tệp dữ liệu trích xuất gồm khoảng 4.066 dòng sự kiện, khác biệt về quy mô và schema so với 17.354 dòng sự kiện chuẩn của dự án. Vì vậy, tệp TWBX cũ được giữ lại làm tư liệu tham khảo lịch sử, trong khi tệp `Validated_Analysis.hyper` và báo cáo `REPORT.html` đại diện cho các con số phân tích chuẩn xác đã qua kiểm định.

Xem thêm: [Biên Bản Đối Soát Dashboard](Docs/Dashboard_Reconciliation.md) | [Ánh Xạ Trường Dữ Liệu](Docs/Dashboard_Field_Mapping.md) | [Hướng Dẫn Kết Nối](Docs/Connect_To_Dashboard.md)

---

## 📂 Cấu Trúc Thư Mục Dự Án

```text
05_User_Journey_Analytics/
│
├── Data/
│   ├── raw/                              # Dữ liệu CSV thô ban đầu (23.354 dòng)
│   └── clean/                            # Dữ liệu CSV sạch chuẩn hóa
│
├── SQL/
│   ├── analysis.sql                      # Các truy vấn phân tích chính
│   └── advanced_queries.sql              # Các truy vấn nâng cao chuyên sâu
│
├── Python/
│   └── analysis.py                       # Điểm khởi chạy phân tích Python
│
├── Excel/
│   └── 05_User_Journey_Analytics_Model.xlsx # Sổ tính toán đối soát
│
├── Dashboard/
│   ├── User_Journey_Tableau_Dashboard.twbx # Dashboard Tableau nguyên bản
│   ├── Validated_Analysis.hyper          # Tệp trích xuất Hyper chuẩn hóa
│   └── README.md                         # Hướng dẫn tái lập dashboard
│
├── Images/
│   └── user_journey.png                  # Ảnh chụp visual hành trình gốc
│
├── Results/
│   ├── summary.csv                       # Tổng quan chuyển đổi mua hàng
│   ├── stage_reach.csv                   # Tiếp cận từng bước độc lập
│   ├── ordered_funnel.csv                # Phễu tuần tự theo thời gian
│   ├── returning_user_conversion.csv     # Chuyển đổi khách mới vs khách quay lại
│   ├── time_to_purchase.csv              # Thời gian chốt đơn từng người
│   ├── additional_metrics.json           # Phân vị thời gian và chẩn đoán phễu
│   ├── quality.json                      # Báo cáo bất thường chất lượng dữ liệu
│   ├── validation.json                   # Kết quả kiểm thử tự động
│   ├── query_plans.json                  # Kế hoạch thực thi SQLite
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

Bạn có thể tự mình chạy lại toàn bộ quy trình phân tích này trên máy tính cá nhân:

```bash
# 1. Sao chép kho mã nguồn
git clone https://github.com/buinhatphong/digital-product-analytics-portfolio.git
cd digital-product-analytics-portfolio

# 2. Tạo và kích hoạt môi trường ảo
python -m venv .venv
.venv\Scripts\Activate.ps1   # Trên Windows
# source .venv/bin/activate  # Trên macOS/Linux

# 3. Cài đặt thư viện
python -m pip install -r requirements.txt

# 4. Chạy phân tích dự án Hành Trình Khách Hàng
python -m portfolio.run --project 05_User_Journey_Analytics

# 5. Chạy bộ kiểm thử tự động
python -m unittest discover -s tests -v
```

Sau khi chạy xong, mở tệp `05_User_Journey_Analytics/REPORT.html` trên trình duyệt web bất kỳ để tương tác với báo cáo trực quan hoàn chỉnh.

---

## ⚠️ Giới Hạn Phân Tích & Hướng Phát Triển

### Giới Hạn Hiện Tại

1. **Dữ liệu mô phỏng:** Dữ liệu phục vụ portfolio cá nhân, không đại diện cho hành vi mua sắm của một nền tảng thực tế.
2. **Độ phân giải thời gian ở mức ngày:** Không có giờ phút giây, khiến việc phân định thứ tự các hành động diễn ra trong cùng một ngày bị hạn chế.
3. **Thiếu mã phiên truy cập (Session ID):** Không phân biệt được các hành động diễn ra trong một lần ghé thăm hay nhiều lần ghé thăm khác nhau.
4. **Lỗi đảo ngược thời gian trên diện rộng:** 54,93% người dùng có ngày các bước bị xáo trộn, làm vô hiệu hóa mô hình phễu tuần tự nghiêm ngặt.
5. **Chưa xử lý kiểm duyệt phải (Right-Censoring):** Thời gian chốt đơn chỉ tính trên nhóm đã mua hàng, chưa tính toán cho nhóm chưa mua nhưng có thể sẽ mua trong tương lai.

### Hướng Phát Triển Tương Lai

- Nâng cấp tracking sự kiện với độ chính xác đến mili-giây và bổ sung mã định danh sự kiện duy nhất (`event_id`).
- Thiết lập cơ chế gom nhóm phiên (Sessionization) để phân tích hành trình khách hàng theo từng phiên riêng biệt.
- Áp dụng mô hình phân tích sống sót Kaplan-Meier (Survival Analysis) để đo lường thời gian chuyển đổi có kiểm soát hiện tượng kiểm duyệt dữ liệu.
- Phân tích đa đường dẫn (Multi-path Funnel Analysis) cho phép khách hàng đi tắt đón đầu mà không bị coi là bỏ rơi phễu.

---

## 🧠 Đúc Kết Từ Dự Án

### Giá Trị Kỹ Thuật

- Thành thạo kỹ thuật xây dựng chuỗi CTE phức tạp để mô hình hóa luồng sự kiện tuần tự trong SQL.
- Sử dụng các hàm ngày tháng của SQLite để tính toán khoảng thời gian chốt đơn chính xác.
- Tự động hóa kiểm tra tính toàn vẹn dữ liệu và đối soát số học bằng Python.

### Giá Trị Nghiệp Vụ

- Không bao giờ tin tưởng số liệu một cách mù quáng: biết hoài nghi lành mạnh khi thấy một kết quả phễu bất thường (0 người hoàn tất phễu dù có 627 người mua).
- Phân biệt rạch ròi giữa lỗi đo lường kỹ thuật và hành vi khách hàng thực tế.
- Biết cách tư vấn cho ban giám đốc và đội ngũ kỹ thuật nâng cấp hạ tầng dữ liệu trước khi ra các quyết định kinh doanh mạo hiểm.

---

## 📚 Tài Liệu Hỗ Trợ & Bằng Chứng

| Tài nguyên | Nội dung chi tiết |
|---|---|
| [Từ Điển Dữ Liệu](Docs/Data_Dictionary.md) | Giải thích schema dữ liệu nguồn và hợp đồng kiểm thử |
| [Nguồn Gốc KPI](Docs/KPI_Lineage.md) | Công thức tính toán và quy tắc nghiệp vụ |
| [Mã Nguồn SQL Phân Tích](SQL/analysis.sql) | Toàn bộ câu truy vấn SQL thực thi |
| [Tổng Quan Mua Hàng](Results/summary.csv) | Kết quả các chỉ số kinh doanh chính |
| [Tiếp Cận Từng Bước](Results/stage_reach.csv) | Bảng số lượng người dùng từng bước độc lập |
| [Phễu Tuần Tự](Results/ordered_funnel.csv) | Kết quả phễu chuyển đổi tuần tự theo thời gian |
| [Khách Quay Lại](Results/returning_user_conversion.csv) | Bảng chuyển đổi khách mới vs khách quay lại |
| [Thời Gian Chốt Đơn](Results/time_to_purchase.csv) | Bảng số ngày mua hàng của từng người |
| [Báo Cáo Kiểm Thử](Results/validation.json) | Biên bản kiểm thử tự động lúc chạy thực tế |
| [Báo Cáo HTML Độc Lập](REPORT.html) | Báo cáo trực quan ngoại tuyến hoàn chỉnh |

---

## 👨‍💻 Về Tác Giả

**Bùi Nhất Phong**  
Data Analytics | Business Intelligence | SQL | Python | Phân Tích Khách Hàng

Tôi đam mê việc biến các tập dữ liệu hành vi phức tạp thành những chỉ số kinh doanh đáng tin cậy, kiểm soát chặt chẽ chất lượng tracking, đánh giá trung thực hiệu quả sản phẩm và truyền tải những góc nhìn sâu sắc hỗ trợ ra quyết định.

Các lĩnh vực quan tâm hàng đầu của tôi: Phân tích Hành trình Khách hàng & Sản phẩm, Phân tích Phễu chuyển đổi, Business Intelligence, Quản trị chất lượng dữ liệu và Phân tích nghiệp vụ.

📧 [Email](mailto:buinhatphong.analytics@gmail.com)  
💼 [LinkedIn](https://www.linkedin.com/in/buinhatphong/)  
💻 [GitHub Profile](https://github.com/buinhatphong)

### 🔗 Khám Phá Thêm Dự Án Trong Portfolio

[⬅️ Quay lại Trang Tổng Quan Portfolio](../README.md)

[📦 Dự án 04: Phân Tích Sàn Thương Mại Điện Tử Amazon](../04_Amazon_Marketplace_Analytics/README.md)

[📈 Dự án 01: Phân Tích Sản Phẩm SaaS](../01_SaaS_Product_Analytics_StreamFlow/README.md)

[🧪 Dự án 02: Thử Nghiệm A/B & Tác Động Tính Năng](../02_AB_Test_Feature_Impact/README.md)

[🛒 Dự án 03: Phân Tích Sản Phẩm Thương Mại Điện Tử](../03_Ecommerce_Product_Analytics/README.md)

---

**🔍 Phân Tích Hành Trình Khách Hàng | Xây dựng bởi Bùi Nhất Phong**  
*Góc nhìn sâu sắc từ SQL. Số liệu kiểm chứng bằng Python. Kiểm soát dữ liệu sự kiện chặt chẽ. Quyết định kinh doanh dựa trên bằng chứng minh bạch.*

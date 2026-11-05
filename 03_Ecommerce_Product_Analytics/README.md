# 🛒 Phân Tích Sản Phẩm Thương Mại Điện Tử | Chuyển Đổi, Hành Vi Khách Hàng & Doanh Thu

### SQL • Python • Phân Tích Phễu • Power BI • Phân Tích Doanh Thu • Chất Lượng Dữ Liệu

**Một case study phân tích dữ liệu E-commerce end-to-end, nghiên cứu sâu về tỷ lệ chuyển đổi website, tỷ lệ bỏ rơi giỏ hàng (cart abandonment), hành vi phiên truy cập của khách hàng, mức độ tập trung doanh thu theo sản phẩm (Pareto SKU) và hiệu quả của các chương trình giảm giá bằng SQL và Python.**

![Python](https://img.shields.io/badge/Python-3.12-3776AB)
![SQL](https://img.shields.io/badge/SQL-SQLite-4479A1)
![Power BI](https://img.shields.io/badge/Power_BI-Tài_Sản_Gốc-F2C811)
![Phân Tích Sản Phẩm](https://img.shields.io/badge/E--commerce-Product_Analytics-blueviolet)
![Kiểm Tra Chất Lượng](https://img.shields.io/badge/Validation-20%2F20-success)
![Bộ Dữ Liệu](https://img.shields.io/badge/Dữ_Liệu-Mô_Phỏng-orange)

**Người thực hiện:** Bùi Nhất Phong  
**Dự án:** 03 — Phân Tích Sản Phẩm Thương Mại Điện Tử  
**Portfolio:** [Data Analyst Portfolio](../README.md)  
**LinkedIn:** [Bùi Nhất Phong](https://www.linkedin.com/in/buinhatphong/)

---

## 📌 Tóm Tắt Dự Án (Executive Summary)

Dự án này phân tích hoạt động kinh doanh của một nền tảng thương mại điện tử mô phỏng nhằm tìm hiểu hành vi mua sắm của khách hàng, hiệu quả chuyển đổi đơn hàng, hiện tượng bỏ rơi giỏ hàng và cơ cấu phân bổ doanh thu giữa các nhóm sản phẩm.

Dựa trên **25.000 phiên truy cập website và 3.037 đơn hàng hoàn tất**, dự án ứng dụng kết hợp SQL, Python, quy trình kiểm soát chất lượng dữ liệu tự động và tư duy Business Intelligence để khám phá các quy luật ẩn sau những con số và đề xuất hướng tối ưu thực tế cho doanh nghiệp.

Nghiên cứu tập trung giải quyết 5 bài toán nghiệp vụ trọng tâm:

1. Phiên truy cập website chuyển đổi thành đơn hàng hiệu quả đến mức nào?
2. Hiện tượng bỏ rơi giỏ hàng (cart abandonment) diễn ra nghiêm trọng ra sao?
3. Hiệu quả chuyển đổi khác biệt thế nào giữa các loại thiết bị và kênh tiếp thị?
4. Doanh thu có bị phụ thuộc quá nhiều vào một số ít sản phẩm bán chạy (SKU Pareto) không?
5. Các chương trình giảm giá quan sát được liên hệ như thế nào với giá trị đơn hàng trung bình (AOV)?

### Kết Quả Cốt Lõi

| Chỉ số kinh doanh | Kết quả xác thực |
|---|---:|
| 👥 Tổng số phiên truy cập website | 25.000 |
| 🛒 Số phiên có thêm sản phẩm vào giỏ | 8.492 |
| 💳 Số đơn hàng mua thành công | 3.037 |
| 📈 Tỷ lệ chuyển đổi phiên (Session Conversion Rate) | 12,15% |
| 📉 Tỷ lệ bỏ rơi giỏ hàng (Cart Abandonment Rate) | 64,24% |
| 💰 Tổng doanh thu đơn hàng ghi nhận | 198.586,00 |
| 🧾 Giá trị đơn hàng trung bình (AOV) | 65,39 |
| 📦 Tổng số mã sản phẩm (SKU) riêng biệt | 400 |
| 🏆 Tỷ trọng doanh thu của Top 20% SKU | 31,42% |
| ✅ Bài kiểm thử dữ liệu & logic đã vượt qua | 20/20 passed |

**Công bố về dữ liệu:** Dự án sử dụng dữ liệu được sinh mô phỏng. Doanh thu được tính theo đơn vị tiền tệ chung của bộ dữ liệu. Kết quả không đại diện cho doanh số bán hàng của một doanh nghiệp thật ngoài đời.

### Các Phát Hiện Chính

**1. Tỷ lệ bỏ rơi giỏ hàng ở mức rất cao:** Trong số 8.492 phiên có hành động thêm hàng vào giỏ, chỉ có 3.037 phiên chốt đơn thành công, tương ứng với tỷ lệ bỏ rơi giỏ hàng lên tới **64,24%**.

**2. Hiệu quả chuyển đổi chênh lệch rõ rệt theo thiết bị và kênh:** Nhóm khách hàng vào bằng máy tính (Desktop) qua kênh Paid Social đạt tỷ lệ chuyển đổi cao nhất là **14,33%**, trong khi nhóm vào bằng điện thoại di động (Mobile) qua cùng kênh này chỉ đạt **9,72%** (chênh lệch 4,61 điểm phần trăm).

**3. Cơ cấu doanh thu sản phẩm phân bổ tương đối đồng đều:** Top 20% SKU đóng góp **31,42% tổng doanh thu**, khác xa so với quy luật 80/20 cực đoan thường thấy trong giả thuyết Pareto truyền thống. 80% sản phẩm còn lại vẫn đóng góp tới gần 68,58% doanh thu.

**4. Cần hết sức thận trọng khi đánh giá mã giảm giá:** Mặc dù số liệu quan sát cho thấy giá trị đơn hàng trung bình ở các đơn có giảm giá thấp hơn đơn không giảm giá ở một số ngành hàng, đây chỉ là mối liên hệ mô tả chứ không chứng minh việc giảm giá làm giảm doanh thu của công ty.

### Kết Luận Kinh Doanh

Dự án xác định rõ 3 điểm nghẽn chiến lược cần ưu tiên hành động: **tối ưu quy trình thanh toán (checkout friction), cải thiện trải nghiệm mua hàng trên di động (mobile UX) và rà soát cơ cấu danh mục hàng hóa (merchandising review)**.

Thay vì đoán mò nguyên nhân, case study cung cấp nền tảng dữ liệu minh bạch, có thể tái lập 100%, làm cơ sở vững chắc cho các cuộc phỏng vấn người dùng, kiểm toán kỹ thuật và thiết kế thử nghiệm A/B trong thực tế.

---

## 📚 Mục Lục

1. [Bài Toán Nghiệp Vụ](#-bài-toán-nghiệp-vụ)
2. [Tổng Quan Bộ Dữ Liệu](#-tổng-quan-bộ-dữ-liệu)
3. [Bộ Công Cụ Kỹ Thuật (Tech Stack)](#-bộ-công-cụ-kỹ-thuật-tech-stack)
4. [Quy Trình Phân Tích End-to-End](#-quy-trình-phân-tích-end-to-end)
5. [Định Nghĩa KPI & Quy Tắc Nghiệp Vụ](#-định-nghĩa-kpi--quy-tắc-nghiệp-vụ)
6. [Phân Tích 1: Hiệu Quả Chuyển Đổi E-commerce](#-phân-tích-1-hiệu-quả-chuyển-đổi-e-commerce)
7. [Phân Tích 2: Tỷ Lệ Bỏ Rơi Giỏ Hàng (Cart Abandonment)](#-phân-tích-2-tỷ-lệ-bỏ-rơi-giỏ-hàng-cart-abandonment)
8. [Phân Tích 3: Hiệu Quả Theo Thiết Bị & Kênh Nguồn Traffic](#-phân-tích-3-hiệu-quả-theo-thiết-bị--kênh-nguồn-traffic)
9. [Phân Tích 4: Phân Bổ Doanh Thu Sản Phẩm & SKU Pareto](#-phân-tích-4-phân-bổ-doanh-thu-sản-phẩm--sku-pareto)
10. [Phân Tích 5: Mối Liên Hệ Giữa Giảm Giá & Giá Trị Đơn Hàng](#-phân-tích-5-mối-liên-hệ-giữa-giảm-giá--giá-trị-đơn-hàng)
11. [Hiện Thực Hóa Bằng SQL](#-hiện-thực-hóa-bằng-sql)
12. [Phân Tích Bằng Python & Đối Soát Số Liệu](#-phân-tích-bằng-python--đối-soát-số-liệu)
13. [Khuyến Nghị Kinh Doanh](#-khuyến-nghị-kinh-doanh)
14. [Chất Lượng Dữ Liệu & Đối Soát](#-chất-lượng-dữ-liệu--đối-soát)
15. [Tài Sản Business Intelligence & Dashboard](#-tài-sản-business-intelligence--dashboard)
16. [Cấu Trúc Thư Mục Dự Án](#-cấu-trúc-thư-mục-dự-án)
17. [Hướng Dẫn Tái Lập Phân Tích](#-hướng-dẫn-tái-lập-phân-tích)
18. [Giới Hạn Phân Tích & Hướng Phát Triển](#-giới-hạn-phân-tích--hướng-phát-triển)
19. [Đúc Kết Từ Dự Án](#-đúc-kết-từ-dự-án)

---

## 🎯 Bài Toán Nghiệp Vụ

### Bối Cảnh Doanh Nghiệp

Mô hình thương mại điện tử phụ thuộc hoàn toàn vào chuỗi hành vi: thu hút lưu lượng truy cập (traffic) → khám phá sản phẩm (product discovery) → thêm hàng vào giỏ (add to cart) → thanh toán thành công (checkout).

Tuy nhiên, kéo được khách vào website không đồng nghĩa với việc sẽ thu được tiền. Rất nhiều người dùng lướt xem hàng, thêm đồ vào giỏ rồi thoát trang mà không bấm thanh toán.

Đồng thời, doanh nghiệp phải hiểu rõ từng kênh marketing, từng loại thiết bị và từng sản phẩm đang đóng góp ra sao vào bức tranh doanh thu chung.

Nếu thiếu hệ thống phân tích chuẩn xác, doanh nghiệp rất dễ lãng phí ngân sách quảng cáo vào những kênh kém hiệu quả hoặc bỏ qua những lỗi trải nghiệm nghiêm trọng tại bước thanh toán.

### Kịch Bản Phân Tích

Nền tảng thương mại điện tử cần đánh giá toàn diện hành vi mua sắm dựa trên 2 tệp dữ liệu được cung cấp: nhật ký các phiên truy cập website và chi tiết các đơn hàng hoàn tất.

### Câu Hỏi Nghiệp Vụ Cốt Lõi

**Quy trình mua hàng trên website đang bị rơi rụng doanh số tiềm năng ở đâu nhiều nhất, và những phân khúc khách hàng hay nhóm sản phẩm nào cần được ưu tiên điều tra cải thiện?**

### Mục Tiêu Phân Tích

| Mục tiêu | Trọng tâm phân tích | Ý nghĩa ra quyết định |
|---|---|---|
| Đánh giá tỷ lệ chuyển đổi | So sánh số phiên và số đơn hàng | Xác định hiệu suất bán hàng tổng thể |
| Khảo sát bỏ giỏ hàng | So sánh số phiên thêm giỏ và số đơn hàng | Tìm ra điểm nghẽn trong phễu mua sắm |
| Phân tích phân khúc | So sánh thiết bị và kênh tiếp thị | Tối ưu hóa phân bổ ngân sách marketing |
| Đánh giá doanh thu | Doanh thu đơn hàng và giá trị đơn trung bình (AOV) | Đánh giá hiệu quả thương mại |
| Đo lường tập trung sản phẩm | Xếp hạng doanh thu theo mã SKU | Đánh giá cơ cấu danh mục hàng hóa (Pareto) |
| Khảo sát chương trình giảm giá | Cờ giảm giá và giá trị đơn hàng | Đặt giả thuyết cho các chiến dịch khuyến mãi |
| Kiểm soát độ tin cậy số liệu | Đối soát hợp đồng dữ liệu và KPI | Đảm bảo dữ liệu báo cáo chuẩn xác 100% |

---

## 🗄️ Tổng Quan Bộ Dữ Liệu

Dự án sử dụng 2 bảng dữ liệu mô phỏng liên kết chặt chẽ với nhau, gồm tổng cộng **28.037 dòng dữ liệu gốc**.

### Các Bảng Dữ Liệu Nguồn

| Bảng dữ liệu | Số bản ghi | Mục đích sử dụng |
|---|---:|---|
| `web_sessions_raw.csv` | 25.000 | Hành vi phiên, thiết bị, kênh marketing, cờ thêm giỏ và cờ mua hàng |
| `orders_raw.csv` | 3.037 | Chi tiết đơn hàng, mã SKU, ngành hàng, cờ giảm giá và giá trị đơn |
| **Tổng cộng** | **28.037** | **2 bảng dữ liệu liên kết** |

### 1. Bảng Web Sessions (Phiên Truy Cập Website)

Mỗi bản ghi đại diện cho một phiên truy cập độc lập vào website thương mại điện tử.

| Tên cột | Kiểu dữ liệu | Ý nghĩa nghiệp vụ |
|---|---|---|
| `session_id` | Integer | Mã định danh duy nhất của phiên truy cập |
| `session_date` | Date | Ngày diễn ra phiên truy cập |
| `device` | Text | Thiết bị sử dụng (Desktop, Mobile) |
| `channel` | Text | Kênh tiếp thị thu hút phiên (Organic, Paid Search, Paid Social, Email, Affiliate) |
| `added_to_cart` | Binary | Cờ nhị phân: 1 nếu có thêm hàng vào giỏ, 0 nếu không |
| `purchased` | Binary | Cờ nhị phân: 1 nếu có hoàn tất mua hàng, 0 nếu không |

### 2. Bảng Orders (Đơn Hàng)

Chứa thông tin chi tiết của đơn hàng tương ứng với các phiên mua hàng thành công.

| Tên cột | Kiểu dữ liệu | Ý nghĩa nghiệp vụ |
|---|---|---|
| `session_id` | Integer | Mã phiên truy cập liên kết đã mua hàng |
| `session_date` | Date | Ngày phát sinh đơn hàng |
| `device` | Text | Thiết bị đặt hàng |
| `channel` | Text | Kênh tiếp thị mang lại đơn hàng |
| `sku` | Text | Mã định danh sản phẩm (SKU) |
| `category` | Text | Ngành hàng (Apparel, Beauty, Electronics, Fitness, Home) |
| `discount_applied` | Binary | Cờ nhị phân: 1 nếu có áp dụng mã giảm giá, 0 nếu không |
| `order_value` | Numeric | Tổng giá trị đơn hàng ghi nhận |
| `units` | Integer | Số lượng sản phẩm trong đơn |

### Mối Quan Hệ Dữ Liệu & Mức Độ Chi Tiết (Grain)

Hai bảng kết nối với nhau qua trường khóa `session_id`:

**Web Sessions (1) → (0 hoặc 1) Orders**

Hợp đồng dữ liệu xác thực rằng mỗi phiên mua hàng thành công (`purchased = 1`) có đúng một dòng đơn hàng tương ứng trong bảng orders.

**Lưu ý quan trọng về mức độ chi tiết:**
- Bộ dữ liệu ghi nhận ở mức phiên (`session_id`), **không có mã khách hàng định danh duy nhất (`customer_id`)**.
- Do đó, ta không thể tính toán các chỉ số vòng đời khách hàng lâu dài như RFM (Recency, Frequency, Monetary) hay giá trị vòng đời (Customer Lifetime Value - CLV) một cách chuẩn xác từ bộ dữ liệu này.

Tài liệu chi tiết: [📘 Từ Điển Dữ Liệu](Docs/Data_Dictionary.md) | [📂 Dữ Liệu Thô](Data/raw) | [📂 Dữ Liệu Đã Làm Sạch](Data/clean)

---

## 🛠️ Bộ Công Cụ Kỹ Thuật (Tech Stack)

| Hạng mục | Công nghệ | Ứng dụng thực tế |
|---|---|---|
| Ngôn ngữ lập trình | Python 3.12 | Làm sạch dữ liệu, kiểm thử tự động, đối soát chéo số liệu |
| Ngôn ngữ truy vấn | SQL | Tính toán KPI, phân tích phễu, xếp hạng Pareto bằng Window Functions |
| Cơ sở dữ liệu | SQLite | Thực thi truy vấn phân tích quan hệ cục bộ |
| Xử lý dữ liệu | pandas | Đối chiếu tính toán độc lập giữa Python và SQL |
| Trực quan hóa dữ liệu | Power BI | Tệp dashboard `.pbix` nguyên bản phục vụ đối soát |
| Mô hình bảng tính | Excel | Kiểm tra công thức và tái lập số liệu bằng sổ làm việc |
| Báo cáo kết quả | HTML & CSV | Xuất bảng kết quả và báo cáo tương tác ngoại tuyến |
| Đảm bảo chất lượng | Python unittest | Bộ kiểm thử tự động toàn diện (20 bài test) |
| Bảo toàn dữ liệu | SHA-256 | Băm mã cryptographic bảo đảm tính toàn vẹn 100% |
| Quản lý phiên bản | Git & GitHub | Quản lý mã nguồn và lịch sử phát triển |

### Kỹ Năng SQL Nâng Cao Được Thể Hiện

- Phép nối bảng `INNER JOIN` và `LEFT JOIN`
- Tổng hợp có điều kiện với `CASE WHEN`
- Bảng tạm dùng chung (Common Table Expressions - CTE)
- Các hàm cửa sổ (Window Functions): `ROW_NUMBER() OVER ()`, `SUM() OVER ()`, `COUNT() OVER ()`
- Tính toán doanh thu tích lũy và tỷ trọng lũy kế (Cumulative Share)
- Xử lý giải quyết trùng thứ hạng xác định (Deterministic tie-breaking)
- Tránh lỗi chia cho 0 bằng `NULLIF`
- Phân tích phễu chuyển đổi đa tầng

---

## 🔄 Quy Trình Phân Tích End-to-End

Dự án áp dụng quy trình phân tích 7 bước nghiêm ngặt:

1. **Xác định yêu cầu nghiệp vụ:** Định nghĩa rõ câu hỏi kinh doanh, tập mẫu số và quy tắc tính từng chỉ số.
2. **Khảo sát dữ liệu thô:** Kiểm tra grain, khóa chính, các cột bắt buộc, kiểu dữ liệu và mối quan hệ tham chiếu giữa sessions và orders.
3. **Làm sạch & Chuẩn hóa:** Ép kiểu dữ liệu chuẩn, cắt tỉa khoảng trắng, kiểm tra giá trị âm và xuất dữ liệu sạch ra `Data/clean/*.csv`. Dữ liệu thô ban đầu được bảo toàn nguyên trạng.
4. **Thực thi phân tích bằng SQL:** Nạp dữ liệu vào SQLite và chạy 4 câu truy vấn phân tích nghiệp vụ chính.
5. **Đối soát chéo bằng Python:** Viết lại toàn bộ logic tính toán bằng Python/pandas để so sánh từng con số với kết quả SQL, đảm bảo không có sai lệch logic.
6. **Đọc hiểu & Đưa ra đề xuất:** Diễn giải ý nghĩa kinh doanh của các con số, chỉ rõ ranh giới giữa dữ liệu quan sát và bằng chứng nhân quả.
7. **Báo cáo & Tái lập:** Xuất các bảng kết quả CSV, báo cáo trực quan `REPORT.html` và cập nhật mã băm SHA-256 vào `manifest.json`.

---

## 📐 Định Nghĩa KPI & Quy Tắc Nghiệp Vụ

| KPI | Công thức tính toán | Cách hiểu đúng |
|---|---|---|
| Tổng số phiên (Sessions) | Đếm tổng số dòng trong bảng web_sessions | Tổng lưu lượng truy cập quan sát được |
| Số phiên có giỏ hàng (Cart Sessions) | Tổng số cờ `added_to_cart = 1` | Các phiên có thể hiện ý định mua sắm |
| Số đơn hàng mua (Purchases) | Tổng số cờ `purchased = 1` | Các phiên chốt đơn thành công |
| Tỷ lệ chuyển đổi phiên (Conversion Rate) | Số đơn mua ÷ Tổng số phiên | Hiệu suất chuyển đổi tổng thể của website |
| Tỷ lệ bỏ rơi giỏ hàng (Cart Abandonment) | 1 − (Số đơn mua ÷ Số phiên có giỏ hàng) | Tỷ lệ phiên có giỏ hàng nhưng không mua |
| Tổng doanh thu ghi nhận (Total Revenue) | Tổng giá trị trường `order_value` | Doanh thu ghi nhận trên các đơn hàng |
| Giá trị đơn hàng trung bình (AOV) | Tổng doanh thu ÷ Số lượng đơn hàng | Doanh thu bình quân mỗi đơn thành công |
| Tỷ trọng doanh thu Top 20% SKU | Doanh thu của 20% mã SKU cao nhất ÷ Tổng doanh thu | Đánh giá mức độ tập trung danh mục (Pareto) |
| AOV đơn có giảm giá | Trung bình `order_value` của các đơn có `discount_applied = 1` | Số liệu quan sát, không phải hiệu ứng nhân quả |

### Quy Tắc Nghiệp Vụ Bắt Buộc

- **Mẫu số của tỷ lệ chuyển đổi là phiên truy cập (sessions), không phải người dùng:** Vì không có mã khách hàng định danh duy nhất.
- **Mua hàng phải qua bước giỏ hàng:** Dữ liệu xác thực 100% phiên có `purchased = 1` đều có `added_to_cart = 1`.
- **Mỗi phiên mua hàng có đúng 1 đơn hàng:** Tổng số dòng trong bảng orders bằng đúng số phiên mua thành công (3.037).
- **Quy tắc xếp hạng SKU:** Khi các SKU có cùng doanh thu, sử dụng mã SKU theo thứ tự chữ cái để phân định thứ hạng (deterministic tie-breaking), đảm bảo kết quả luôn nhất quán khi chạy lại.

Chi tiết quy tắc: [Nguồn Gốc KPI (KPI Lineage)](Docs/KPI_Lineage.md)

---

## 📈 Phân Tích 1: Hiệu Quả Chuyển Đổi E-commerce

### Câu Hỏi Nghiệp Vụ

Tỷ lệ phiên truy cập website chuyển đổi thành đơn hàng thành công là bao nhiêu?

### Kết Quả Đối Soát

| Chỉ số | Kết quả xác thực |
|---|---:|
| Tổng số phiên truy cập website | 25.000 |
| Số phiên có thêm hàng vào giỏ | 8.492 |
| Số đơn hàng mua thành công | 3.037 |
| Tỷ lệ chuyển đổi phiên | 12,15% |
| Tỷ lệ có hành động thêm giỏ | 33,97% |
| Tổng doanh thu ghi nhận | 198.586,00 |
| Giá trị đơn hàng trung bình (AOV) | 65,39 |

### Công Thức Tính Tỷ Lệ Chuyển Đổi

\[
\text{Tỷ lệ chuyển đổi} = \frac{3.037}{25.000} \times 100\% = 12,15\%
\]

### Các Phát Hiện Chính

- **Đa số phiên truy cập không phát sinh giao dịch:** Có 12,15% số phiên dẫn đến đơn hàng thành công. Đây là con số cơ sở (baseline) để doanh nghiệp theo dõi qua các kỳ kinh doanh.
- **Khoảng 1/3 số phiên có ý định mua sắm:** Có tới 33,97% số phiên có hành động thêm hàng vào giỏ. Điều này chứng minh rằng người dùng có tìm thấy sản phẩm họ thích, nhưng một lượng lớn đã bỏ cuộc ở các bước thanh toán phía sau.
- **Giá trị đơn hàng trung bình đạt 65,39 đơn vị tiền tệ:** Tổng doanh thu 198.586,00 chia đều cho 3.037 đơn hàng mang lại giá trị AOV là 65,39.

**Bằng chứng truy vấn:** [Tổng quan E-commerce (summary.csv)](Results/summary.csv)

---

## 🛒 Phân Tích 2: Tỷ Lệ Bỏ Rơi Giỏ Hàng (Cart Abandonment)

### Câu Hỏi Nghiệp Vụ

Tần suất các phiên có thêm hàng vào giỏ nhưng không hoàn tất đơn hàng là bao nhiêu?

### Phân Tích Các Tầng Phễu Mua Sắm

| Tầng phễu | Số phiên | Tỷ trọng trên tổng phiên |
|---|---:|---:|
| 1. Ghé thăm website (Sessions) | 25.000 | 100,00% |
| 2. Thêm hàng vào giỏ (Added to Cart) | 8.492 | 33,97% |
| 3. Mua hàng thành công (Purchased) | 3.037 | 12,15% |

### Tỷ Lệ Hoàn Tất Giỏ Hàng

\[
\text{Tỷ lệ hoàn tất} = \frac{3.037}{8.492} \times 100\% = 35,76\%
\]

### Tỷ Lệ Bỏ Rơi Giỏ Hàng

\[
\text{Tỷ lệ bỏ rơi giỏ hàng} = 1 - \frac{3.037}{8.492} = 64,24\%
\]

### Các Phát Hiện Quan Trọng

1. **Gần 2/3 số giỏ hàng bị bỏ quên:** Trong số 8.492 phiên có hàng trong giỏ, có tới 5.455 phiên kết thúc mà không có đơn hàng nào được tạo ra (tỷ lệ 64,24%).
2. **Điểm nghẽn nằm ở bước thanh toán:** Khoảng cách sụt giảm giữa bước Thêm giỏ (8.492) và Mua hàng (3.037) cho thấy quy trình thanh toán đang có vấn đề lớn.
3. **Các nguyên nhân tiềm ẩn cần điều tra:**
   - Chi phí vận chuyển hoặc phụ phí phát sinh bất ngờ ở bước cuối.
   - Bắt buộc phải đăng ký tài khoản rườm rà thay vì cho phép mua hàng ẩn danh (guest checkout).
   - Thiếu phương thức thanh toán thuận tiện (ví điện tử, thẻ nội địa).
   - Khách hàng thêm vào giỏ để lưu tạm hoặc so sánh giá với các sàn khác.
4. **Không thể coi giỏ hàng bỏ rơi là "doanh thu bị mất" hoàn toàn:** Dữ liệu không ghi nhận giá trị món hàng trong các giỏ bị bỏ rơi, do đó không thể lấy 5.455 giỏ nhân với AOV để kết luận rằng công ty bị mất một số tiền cụ thể nào đó. Đó là cách diễn giải thiếu căn cứ khoa học.

**Bằng chứng truy vấn:** [Phân tích phễu theo phân khúc (funnel_by_segment.csv)](Results/funnel_by_segment.csv)

---

## 📱 Phân Tích 3: Hiệu Quả Theo Thiết Bị & Kênh Nguồn Traffic

### Câu Hỏi Nghiệp Vụ

Sự kết hợp giữa loại thiết bị và kênh tiếp thị nào mang lại tỷ lệ chuyển đổi cao nhất, và nhóm nào đang gặp vấn đề rơi rụng nghiêm trọng nhất?

### Bảng Kết Quả 10 Phân Khúc Chi Tiết

| Thiết bị | Kênh tiếp thị | Số phiên | Số đơn mua | Tỷ lệ chuyển đổi | Tỷ lệ bỏ giỏ hàng |
|---|---|---:|---:|---:|---:|
| 💻 Desktop | Paid Social | 2.247 | 322 | 14,33% | 60,10% |
| 💻 Desktop | Paid Search | 3.448 | 475 | 13,78% | 61,63% |
| 💻 Desktop | Email | 1.739 | 239 | 13,74% | 61,20% |
| 💻 Desktop | Affiliate | 1.201 | 153 | 12,74% | 67,17% |
| 💻 Desktop | Organic | 3.452 | 431 | 12,49% | 64,93% |
| 📱 Mobile | Affiliate | 1.232 | 153 | 12,42% | 63,22% |
| 📱 Mobile | Paid Search | 3.669 | 424 | 11,56% | 64,37% |
| 📱 Mobile | Email | 1.817 | 199 | 10,95% | 65,27% |
| 📱 Mobile | Organic | 3.788 | 407 | 10,74% | 66,67% |
| 📱 Mobile | Paid Social | 2.407 | 234 | 9,72% | 68,21% |

### Các Phát Hiện Quan Trọng

1. **Desktop Paid Social đạt hiệu quả chuyển đổi cao nhất:** Đạt tỷ lệ chuyển đổi **14,33%** và tỷ lệ bỏ giỏ hàng thấp nhất (60,10%).
2. **Mobile Paid Social có hiệu quả thấp nhất:** Tỷ lệ chuyển đổi chỉ đạt **9,72%**, và tỷ lệ bỏ giỏ hàng lên tới **68,21%**. Mặc dù mang lại lượng traffic lớn (2.407 phiên), nhưng tỷ lệ chuyển đổi lại rớt xuống dưới 10%.
3. **Khoảng cách chuyển đổi lớn giữa Mobile và Desktop:** Cùng là kênh quảng cáo Paid Social, nhưng người dùng máy tính chuyển đổi cao hơn người dùng điện thoại tới **4,61 điểm phần trăm** (14,33% so với 9,72%). Điều này báo hiệu trải nghiệm mua sắm trên thiết bị di động có thể đang gặp lỗi giao diện, tốc độ tải trang chậm hoặc luồng điền form quá dài dòng.
4. **Kênh Mobile Organic cũng chịu tỷ lệ bỏ giỏ hàng rất cao:** Đạt mức 66,67% bỏ giỏ hàng trên tập mẫu 3.788 phiên.

**Bằng chứng truy vấn:** [Chi tiết thiết bị & kênh (funnel_by_segment.csv)](Results/funnel_by_segment.csv)

---

## 📦 Phân Tích 4: Phân Bổ Doanh Thu Sản Phẩm & SKU Pareto

### Câu Hỏi Nghiệp Vụ

Doanh thu bán hàng tập trung vào các sản phẩm bán chạy nhất ở mức độ nào? Có tuân theo quy luật Pareto 80/20 không?

### Tổng Quan Về Sản Phẩm

| Chỉ số | Kết quả xác thực |
|---|---:|
| Tổng số mã SKU riêng biệt | 400 SKU |
| Số lượng SKU trong nhóm Top 20% | 80 SKU |
| Tổng doanh thu đơn hàng ghi nhận | 198.586,00 |
| Tỷ trọng doanh thu của nhóm Top 20% SKU | **31,42%** |

### Phương Pháp Luận Phân Tích Pareto

1. Gom nhóm và tính tổng doanh thu theo từng mã SKU.
2. Xếp hạng giảm dần theo doanh thu bằng Window Function `ROW_NUMBER()`.
3. Phân định thứ hạng bằng mã `sku` khi doanh thu bằng nhau để đảm bảo tính xác định.
4. Tính doanh thu lũy kế bằng `SUM(revenue) OVER (ORDER BY revenue DESC, sku ROWS UNBOUNDED PRECEDING)`.
5. Xác định nhóm Top 20% sản phẩm (80 SKU đầu tiên).
6. Tính tỷ lệ phần trăm đóng góp của nhóm này trên tổng doanh thu.

### Top 10 Sản Phẩm Có Doanh Thu Cao Nhất

| Thứ hạng | Mã SKU | Doanh thu ghi nhận |
|---|---|---:|
| 1 | SKU-0028 | 1.249,99 |
| 2 | SKU-0143 | 992,65 |
| 3 | SKU-0081 | 948,51 |
| 4 | SKU-0339 | 930,70 |
| 5 | SKU-0104 | 920,64 |
| 6 | SKU-0344 | 903,81 |
| 7 | SKU-0122 | 896,86 |
| 8 | SKU-0273 | 889,10 |
| 9 | SKU-0234 | 879,20 |
| 10 | SKU-0047 | 876,01 |

### Các Phát Hiện Quan Trọng

1. **Sản phẩm dẫn đầu doanh thu là SKU-0028:** Đóng góp 1.249,99 đơn vị tiền tệ.
2. **Mức độ tập trung doanh thu ở mức vừa phải:** 80 sản phẩm thuộc Top 20% chỉ đóng góp **31,42% tổng doanh thu**. Điều này chứng minh cơ cấu bán hàng của website phân bổ đều trên danh mục rộng (Long Tail), hoàn toàn không phụ thuộc thái quá vào một nhóm nhỏ vài sản phẩm chủ lực.
3. **Doanh thu không đồng nghĩa với lợi nhuận:** Một sản phẩm có doanh thu cao chưa chắc đã mang lại biên lợi nhuận tốt nếu chi phí vốn hàng bán (COGS) hoặc tỷ lệ hoàn trả quá cao. Cần bổ sung dữ liệu chi phí để đánh giá toàn diện.

**Bằng chứng truy vấn:** [Kết quả xếp hạng SKU (sku_pareto.csv)](Results/sku_pareto.csv)

---

## 🏷️ Phân Tích 5: Mối Liên Hệ Giữa Giảm Giá & Giá Trị Đơn Hàng

### Câu Hỏi Nghiệp Vụ

Giá trị đơn hàng và số lượng sản phẩm khác biệt thế nào giữa các đơn có áp dụng mã giảm giá và đơn không giảm giá?

### Kết Quả Khảo Sát Một Số Phân Khúc

| Thiết bị | Ngành hàng | Có giảm giá? | Số đơn hàng | Giá trị đơn trung bình (AOV) |
|---|---|---|---:|---:|
| 💻 Desktop | Quần áo (Apparel) | Không | 283 | 67,90 |
| 💻 Desktop | Quần áo (Apparel) | Có | 163 | 61,82 |
| 💻 Desktop | Mỹ phẩm (Beauty) | Không | 203 | 67,06 |
| 💻 Desktop | Mỹ phẩm (Beauty) | Có | 98 | 62,71 |
| 💻 Desktop | Điện tử (Electronics) | Không | 210 | 68,08 |
| 💻 Desktop | Điện tử (Electronics) | Có | 123 | 61,91 |
| 💻 Desktop | Thể thao (Fitness) | Không | 120 | 71,31 |
| 💻 Desktop | Thể thao (Fitness) | Có | 64 | 60,42 |
| 💻 Desktop | Đồ gia dụng (Home) | Không | 225 | 67,92 |
| 💻 Desktop | Đồ gia dụng (Home) | Có | 131 | 63,78 |

### Các Phát Hiện Quan Trọng

1. **Đơn hàng có giảm giá có AOV thấp hơn ở nhiều nhóm:** Trong các danh mục trên máy tính hiển thị ở trên, giá trị đơn hàng trung bình của nhóm có giảm giá thấp hơn nhóm không giảm giá khoảng từ 4 đến 11 đơn vị tiền tệ.
2. **AOV thấp hơn không đồng nghĩa với chương trình giảm giá thất bại:** Mục tiêu của khuyến mãi có thể là: xả hàng tồn kho, thu hút khách hàng mới, hoặc kích thích người dùng bấm thanh toán thay vì bỏ rơi giỏ hàng. Nếu giảm giá giúp tăng số lượng đơn hàng tổng thể đủ lớn để bù đắp cho mức giảm AOV thì chương trình vẫn thành công về mặt lợi nhuận gộp.
3. **Cảnh báo về thiên lệch tự chọn (Selection Bias):** Vì dữ liệu không phải là thử nghiệm ngẫu nhiên A/B, khách hàng chủ động tìm kiếm mã giảm giá có thể vốn dĩ là nhóm khách nhạy cảm về giá và có xu hướng chọn những món đồ rẻ tiền hơn. Ta không được kết luận một cách ngây thơ rằng "giảm giá làm giảm giá trị đơn hàng".

**Bằng chứng truy vấn:** [Mối liên hệ giảm giá (discount_association.csv)](Results/discount_association.csv)

---

## 💻 Hiện Thực Hóa Bằng SQL

Toàn bộ các phân tích đều được thực thi trực tiếp bằng các truy vấn SQLite chuẩn, tối ưu hóa hiệu năng và bảo đảm tính tái lập:

### Truy Vấn 1 — Tổng Hợp Toàn Diện Hiệu Suất E-commerce

```sql
SELECT
    COUNT(*) AS sessions,
    SUM(added_to_cart) AS cart_sessions,
    SUM(purchased) AS purchases,

    -- Tỷ lệ chuyển đổi tổng thể
    AVG(1.0 * purchased) AS conversion_rate,

    -- Tỷ lệ bỏ rơi giỏ hàng (tránh chia cho 0)
    1.0 - SUM(1.0 * purchased)
        / NULLIF(SUM(added_to_cart), 0)
        AS cart_abandonment_rate,

    -- Tổng doanh thu từ bảng đơn hàng
    (
        SELECT SUM(order_value)
        FROM orders_clean
    ) AS revenue,

    -- Giá trị đơn hàng trung bình
    (
        SELECT AVG(order_value)
        FROM orders_clean
    ) AS average_order_value

FROM web_sessions_clean;
```

### Truy Vấn 2 — Phân Tích Phễu Chuyển Đổi Theo Phân Khúc

```sql
SELECT
    device,
    channel,

    COUNT(*) AS sessions,
    SUM(added_to_cart) AS carts,
    SUM(purchased) AS purchases,

    AVG(1.0 * purchased)
        AS conversion_rate,

    1.0 - SUM(1.0 * purchased)
        / NULLIF(SUM(added_to_cart), 0)
        AS cart_abandonment_rate

FROM web_sessions_clean

GROUP BY
    device,
    channel

ORDER BY conversion_rate DESC;
```

### Truy Vấn 3 — Xếp Hạng Doanh Thu SKU & Tỷ Trọng Lũy Kế (Pareto)

```sql
WITH revenue AS (
    SELECT
        sku,
        SUM(order_value) AS revenue
    FROM orders_clean
    GROUP BY sku
),

ranked AS (
    SELECT
        *,
        ROW_NUMBER() OVER (
            ORDER BY revenue DESC, sku
        ) AS rank,

        COUNT(*) OVER () AS sku_count,
        SUM(revenue) OVER () AS total_revenue,

        SUM(revenue) OVER (
            ORDER BY revenue DESC, sku
            ROWS UNBOUNDED PRECEDING
        ) AS cumulative_revenue

    FROM revenue
)

SELECT
    *,
    cumulative_revenue / NULLIF(total_revenue, 0) AS cumulative_share,
    (rank <= (sku_count + 4) / 5) AS in_top_20_percent

FROM ranked
ORDER BY rank;
```

**Xem toàn bộ mã nguồn SQL:** [SQL/analysis.sql](SQL/analysis.sql)

---

## 🐍 Phân Tích Bằng Python & Đối Soát Số Liệu

Mô-đun Python đóng vai trò là "chốt chặn kiểm soát chất lượng":
- Đọc dữ liệu, kiểm tra tính toàn vẹn kiểu dữ liệu và các ràng buộc logic.
- Tính toán độc lập các chỉ số KPI: Sessions, Carts, Purchases, Conversion Rate, Abandonment Rate, Revenue, AOV, Top 20% SKU Share.
- So sánh từng con số với kết quả của SQL; nếu có bất kỳ sự sai lệch nào dù chỉ 0,0001, pipeline sẽ lập tức báo lỗi và dừng thực thi.

---

## 💡 Khuyến Nghị Kinh Doanh

### Bảng Ưu Tiên Hành Động

| Mức ưu tiên | Đề xuất hành động | Bằng chứng dữ liệu hỗ trợ | Phương án kiểm chứng |
|---|---|---|---|
| 🔴 Rất cao | Tối ưu luồng thanh toán để giảm bỏ giỏ hàng | 64,24% giỏ hàng bị bỏ rơi | Nghiên cứu trải nghiệm người dùng (UX) và triển khai thanh toán 1 bước |
| 🔴 Rất cao | Nâng cấp trải nghiệm mua sắm trên Di Động | Kênh Mobile Paid Social chỉ đạt 9,72% conversion | Kiểm toán hiệu năng Mobile, kiểm tra hiển thị form điền |
| 🟡 Trung bình | Tối ưu luồng mua sắm kênh Mobile Organic | 66,67% bỏ giỏ hàng trên 3.788 phiên | Phân tích các bước rớt khách hàng và tích hợp Apple Pay/Google Pay |
| 🟡 Trung bình | Bổ sung dữ liệu biên lợi nhuận cho danh mục SKU | Top 20% SKU chỉ chiếm 31,42% doanh thu | Kết hợp dữ liệu giá vốn và chi phí lưu kho để đánh giá danh mục |
| 🟡 Trung bình | Chạy thử nghiệm A/B cho các chiến dịch giảm giá | AOV ở đơn có giảm giá thấp hơn | Thiết kế thử nghiệm A/B có kiểm soát đối chứng |

### Lộ Trình Triển Khai 30 / 60 / 90 Ngày

- **Ngày 1–30 (Khảo sát & Đo lường):** Gắn thẻ tracking chi tiết từng bước trong quy trình thanh toán (Shipping, Billing, Review). Phỏng vấn người dùng gặp sự cố trên thiết bị di động.
- **Ngày 31–60 (Thiết kế giải pháp):** Thiết kế lại giao diện thanh toán trên điện thoại (tích hợp tự động điền địa chỉ, các nút thanh toán nhanh). Thiết kế thử nghiệm A/B cho luồng checkout mới.
- **Ngày 61–90 (Đánh giá & Triển khai):** Phân tích kết quả thử nghiệm A/B. Nếu tỷ lệ bỏ giỏ hàng giảm có ý nghĩa thống kê, phát hành giao diện mới cho 100% người dùng.

---

## ✅ Chất Lượng Dữ Liệu & Đối Soát

| Tiêu chí chất lượng | Kết quả xác thực |
|---|---:|
| Bản ghi phiên truy cập website | 25.000 dòng |
| Bản ghi đơn hàng | 3.037 dòng |
| Tổng số dòng dữ liệu nguồn | 28.037 dòng |
| Số ô dữ liệu bắt buộc bị thiếu | 0 ô |
| Dòng dữ liệu trùng lặp nguyên bản | 0 dòng |
| Số bài kiểm thử tự động vượt qua | 20/20 passed |

**Các tệp kết quả kiểm thử:**
- [validation.json](Results/validation.json) — Biên bản kiểm thử kỹ thuật và đối soát số liệu
- [quality.json](Results/quality.json) — Nhật ký chất lượng dữ liệu và giới hạn phân tích
- [manifest.json](Results/manifest.json) — Mã băm cryptographic SHA-256

---

## 📊 Tài Sản Business Intelligence & Dashboard

| Tài sản | Vị trí | Mục đích sử dụng |
|---|---|---|
| Sổ làm việc Excel | [Excel Model](Excel/03_Ecommerce_Product_Analytics_Model.xlsx) | Sổ tính toán đối soát công thức chuẩn |
| Tệp Power BI PBIX cũ | [Power BI Dashboard](Dashboard/Ecommerce_Product_Analytics.pbix) | Dashboard nguyên bản phục vụ kiểm toán |
| Ảnh chụp phễu trực quan | [Thư mục Images](Images/ecommerce_funnel.png) | Ảnh chụp biểu đồ phễu tham khảo |
| Báo cáo HTML độc lập | [REPORT.html](REPORT.html) | Báo cáo trực quan độc lập hoàn chỉnh |

### Trạng Thái Đối Soát Dashboard Power BI Gốc

Rà soát kỹ thuật cho thấy tệp Power BI `.pbix` nguyên bản chứa cấu trúc mô hình nhúng khác biệt về bảng và mức độ chi tiết so với 2 bảng CSV chuẩn của dự án. Vì vậy, tệp PBIX cũ được giữ lại làm tư liệu tham khảo lịch sử, trong khi báo cáo `REPORT.html` và các tệp kết quả CSV đại diện cho số liệu phân tích chuẩn xác đã qua kiểm định.

Xem thêm: [Biên Bản Đối Soát Dashboard](Docs/Dashboard_Reconciliation.md) | [Ánh Xạ Trường Dữ Liệu](Docs/Dashboard_Field_Mapping.md) | [Hướng Dẫn Kết Nối](Docs/Connect_To_Dashboard.md)

---

## 📂 Cấu Trúc Thư Mục Dự Án

```text
03_Ecommerce_Product_Analytics/
│
├── Data/
│   ├── raw/                              # Dữ liệu CSV thô ban đầu (28.037 dòng)
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
│   └── 03_Ecommerce_Product_Analytics_Model.xlsx  # Sổ tính toán đối soát
│
├── Dashboard/
│   ├── Ecommerce_Product_Analytics.pbix  # Dashboard Power BI nguyên bản
│   └── README.md                         # Hướng dẫn tái lập dashboard
│
├── Images/
│   └── ecommerce_funnel.png              # Hình ảnh biểu đồ phễu tham khảo
│
├── Results/
│   ├── summary.csv                       # Tổng quan hiệu suất e-commerce
│   ├── funnel_by_segment.csv             # Phân tích phễu theo thiết bị và kênh
│   ├── sku_pareto.csv                    # Xếp hạng doanh thu sản phẩm (Pareto)
│   ├── discount_association.csv          # Khảo sát hiệu quả giảm giá
│   ├── additional_metrics.json           # Các chỉ số bổ trợ
│   ├── quality.json                      # Báo cáo chất lượng dữ liệu
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

# 4. Chạy phân tích dự án E-commerce
python -m portfolio.run --project 03_Ecommerce_Product_Analytics

# 5. Chạy bộ kiểm thử tự động
python -m unittest discover -s tests -v
```

Sau khi chạy xong, mở tệp `03_Ecommerce_Product_Analytics/REPORT.html` trên trình duyệt web bất kỳ để tương tác với báo cáo trực quan hoàn chỉnh.

---

## ⚠️ Giới Hạn Phân Tích & Hướng Phát Triển

### Giới Hạn Hiện Tại

1. **Dữ liệu mô phỏng:** Kết quả phục vụ minh họa năng lực phân tích portfolio, không phải hoạt động thương mại thực tế ngoài đời.
2. **Thiếu mã khách hàng định danh duy nhất:** Không có `customer_id` nên không thể tính toán các chỉ số vòng đời như RFM hay Customer Lifetime Value (CLV).
3. **Mức độ chi tiết đơn hàng đơn giản:** Mỗi phiên mua hàng chỉ gắn với một dòng đơn hàng và một mã SKU; ngoài đời thực một đơn hàng thường chứa nhiều món hàng khác nhau.
4. **Chưa có nhật ký chi tiết các bước checkout:** Dữ liệu chỉ có cờ thêm giỏ và cờ mua hàng, chưa thể hiện chi tiết khách rớt ở bước nhập địa chỉ hay bước thanh toán thẻ.
5. **Chưa có dữ liệu biên lợi nhuận:** Phân tích Pareto dựa trên doanh thu chứ chưa phản ánh lợi nhuận ròng của từng sản phẩm.

### Hướng Phát Triển Tương Lai

- Bổ sung mã khách hàng để phân tích tần suất mua lại và phân khúc khách hàng theo mô hình RFM.
- Thiết lập tracking chi tiết từng bước thanh toán (Checkout Funnel Instrumentation).
- Tích hợp dữ liệu giá vốn (COGS) để phân tích khả năng sinh lời thực tế của từng sản phẩm.
- Triển khai thử nghiệm A/B có đối chứng cho các chương trình khuyến mãi và luồng thanh toán trên di động.

---

## 🧠 Đúc Kết Từ Dự Án

### Giá Trị Kỹ Thuật

- Khả năng xử lý, kết nối và phân tích dữ liệu quan hệ E-commerce bằng SQL thuần thục.
- Ứng dụng Window Functions giải quyết các bài toán xếp hạng lũy kế phức tạp (Pareto Analysis).
- Xây dựng pipeline kiểm soát chất lượng dữ liệu tự động bằng Python.
- Đối soát chéo số liệu đa tầng triệt tiêu mọi rủi ro sai lệch báo cáo.

### Giá Trị Nghiệp Vụ

- Chuyển đổi các bài toán kinh doanh thành các chỉ số KPI đo lường được.
- Đánh giá khách quan số liệu, không nhầm lẫn giữa tương quan quan sát với tác động nhân quả.
- Xác định đúng điểm nghẽn chiến lược (Mobile Checkout & Cart Abandonment) và đề xuất giải pháp có thể kiểm chứng.

---

## 📚 Tài Liệu Hỗ Trợ & Bằng Chứng

| Tài nguyên | Nội dung chi tiết |
|---|---|
| [Từ Điển Dữ Liệu](Docs/Data_Dictionary.md) | Giải thích schema dữ liệu nguồn và hợp đồng kiểm thử |
| [Nguồn Gốc KPI](Docs/KPI_Lineage.md) | Công thức tính toán và quy tắc nghiệp vụ |
| [Mã Nguồn SQL Phân Tích](SQL/analysis.sql) | Toàn bộ câu truy vấn SQL thực thi |
| [Tổng Quan E-commerce](Results/summary.csv) | Kết quả các chỉ số kinh doanh chính |
| [Phân Tích Phễu Theo Phân Khúc](Results/funnel_by_segment.csv) | Bảng chuyển đổi theo thiết bị và kênh tiếp thị |
| [Xếp Hạng Doanh Thu SKU](Results/sku_pareto.csv) | Bảng phân bổ doanh thu sản phẩm lũy kế |
| [Khảo Sát Giảm Giá](Results/discount_association.csv) | Bảng so sánh đơn hàng có và không có giảm giá |
| [Báo Cáo Kiểm Thử](Results/validation.json) | Biên bản kiểm thử tự động lúc chạy thực tế |
| [Báo Cáo HTML Độc Lập](REPORT.html) | Báo cáo trực quan ngoại tuyến hoàn chỉnh |

---

## 👨‍💻 Về Tác Giả

**Bùi Nhất Phong**  
Data Analytics | Business Intelligence | SQL | Python | Phân Tích Sản Phẩm

Tôi tập trung vào việc biến dữ liệu thô thành những góc nhìn kinh doanh tin cậy, tối ưu hóa hiệu quả hoạt động, chuẩn hóa chất lượng báo cáo và hỗ trợ ra quyết định chiến lược.

Các lĩnh vực quan tâm hàng đầu của tôi: Phân tích E-commerce & Sản phẩm kỹ thuật số, Hành vi khách hàng, Business Intelligence, Tối ưu hóa phễu chuyển đổi và Đảm bảo chất lượng dữ liệu.

📧 [Email](mailto:buinhatphong.analytics@gmail.com)  
💼 [LinkedIn](https://www.linkedin.com/in/buinhatphong/)  
💻 [GitHub Profile](https://github.com/buinhatphong)

### 🔗 Khám Phá Thêm Dự Án Trong Portfolio

[⬅️ Quay lại Trang Tổng Quan Portfolio](../README.md)

[🧪 Dự án trước: Thử Nghiệm A/B & Tác Động Tính Năng](../02_AB_Test_Feature_Impact/README.md)

[📦 Dự án tiếp theo: Phân Tích Doanh Thu Sàn & Người Bán Amazon](../04_Amazon_Marketplace_Analytics/README.md)

---

**🛒 Phân Tích Sản Phẩm Thương Mại Điện Tử | Xây dựng bởi Bùi Nhất Phong**  
*Phân tích sắc bén bằng SQL. Số liệu kiểm chứng bằng Python. Quyết định kinh doanh thực tế và minh bạch.*

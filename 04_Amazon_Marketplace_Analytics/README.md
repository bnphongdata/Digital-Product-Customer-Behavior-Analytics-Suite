# 📦 Phân Tích Sàn Thương Mại Điện Tử Amazon | Doanh Thu, Hiệu Quả Người Bán & Đối Soát Dữ Liệu

### SQL • Python • Phân Tích Sàn Thương Mại • Đối Soát Tài Chính • Business Intelligence

**Một case study phân tích dữ liệu sàn thương mại điện tử (Marketplace) end-to-end, đi sâu vào doanh thu bán hàng, hiệu quả từng ngành hàng, mức độ tập trung nguồn thu của người bán (seller concentration), mối liên hệ tồn kho và đối soát sự bất thường trong dữ liệu tài chính bằng SQL và Python.**

![Python](https://img.shields.io/badge/Python-3.12-3776AB)
![SQL](https://img.shields.io/badge/SQL-SQLite-4479A1)
![Power BI](https://img.shields.io/badge/Power_BI-Tài_Sản_Gốc-F2C811)
![Phân Tích Sàn](https://img.shields.io/badge/Marketplace-Analytics-blueviolet)
![Kiểm Tra Chất Lượng](https://img.shields.io/badge/Validation-19%2F19-success)
![Bộ Dữ Liệu](https://img.shields.io/badge/Dữ_Liệu-Mô_Phỏng-orange)

**Người thực hiện:** Bùi Nhất Phong  
**Dự án:** 04 — Phân Tích Sàn Thương Mại Điện Tử Amazon  
**Portfolio:** [Data Analyst Portfolio](../README.md)  
**LinkedIn:** [Bùi Nhất Phong](https://www.linkedin.com/in/buinhatphong/)

---

## 📌 Tóm Tắt Dự Án (Executive Summary)

Dự án này phân tích hoạt động kinh doanh trên một sàn thương mại điện tử mô phỏng theo mô hình Amazon Marketplace để làm rõ hiệu quả bán hàng, mức độ tập trung doanh thu giữa các nhà bán hàng (sellers), đóng góp của từng ngành hàng, trạng thái tồn kho và đặc biệt là **sự sai lệch trong dữ liệu doanh thu tài chính**.

Dựa trên **24.000 dòng dữ liệu giao dịch bán hàng và 1.800 bài đăng sản phẩm (listings)**, dự án kết hợp truy vấn SQL, phân tích Python, kiểm tra ràng buộc quan hệ dữ liệu và tư duy đối soát tài chính để chuyển đổi dữ liệu thô thành các chỉ số đáng tin cậy.

Khác với các dashboard bán hàng thông thường chỉ biết cộng tổng doanh thu một cách máy móc, case study này đặt trọng tâm vào **đối soát tài chính (financial reconciliation), độ tin cậy của dữ liệu nguồn và tư duy phân tích có trách nhiệm**.

Dự án tập trung giải quyết 5 bài toán nghiệp vụ trọng tâm:

1. Tổng doanh thu ghi nhận thực tế trên sàn là bao nhiêu?
2. Ngành hàng nào đóng góp doanh thu lớn nhất?
3. Doanh thu có bị phụ thuộc quá mức vào một vài nhà bán hàng lớn hay không?
4. Tại sao có sự chênh lệch lớn giữa doanh thu ghi nhận và phép tính số học đơn giản (Đơn giá × Số lượng)?
5. Dữ liệu trạng thái tồn kho hiện tại phản ánh điều gì, và doanh nghiệp cần thu thập thêm thông tin gì trước khi đưa ra quyết định nhập hàng?

### Kết Quả Cốt Lõi

| Chỉ số kinh doanh | Kết quả xác thực |
|---|---:|
| 📦 Tổng số bài đăng sản phẩm (Listings) | 1.800 |
| 🛒 Tổng số dòng giao dịch bán hàng (Sales records) | 24.000 |
| 📊 Tổng số lượng sản phẩm bán ra | 48.063 |
| 👥 Số lượng nhà bán hàng riêng biệt (Sellers) | 316 |
| 💰 Doanh thu ghi nhận trong bảng (Recorded Revenue) | 1.830.085,36 |
| 🧮 Doanh thu tính theo phép nhân (Đơn giá × Số lượng) | 1.901.153,19 |
| ⚠️ Số dòng bị lệch doanh thu (> 1 cent) | 9.019 dòng (37,58%) |
| 📈 Tỷ trọng doanh thu của Top 10 nhà bán hàng lớn nhất | 8,44% |
| 📉 Chỉ số tập trung người bán (Seller HHI) | 42,39 (Rất thấp) |
| ✅ Bài kiểm thử dữ liệu & logic đã vượt qua | 19/19 passed |

**Công bố về dữ liệu:** Dự án sử dụng dữ liệu mô phỏng phục vụ portfolio cá nhân. Dù mang tiêu đề Amazon Marketplace, dữ liệu này không phải là số liệu thật của tập đoàn Amazon và không đại diện cho bất kỳ sàn thương mại điện tử thực tế nào. Doanh thu được tính theo đơn vị tiền tệ chung của bộ dữ liệu.

### Các Phát Hiện Quan Trọng

**1. Đối soát doanh thu là vấn đề chất lượng dữ liệu nghiêm trọng nhất:**  
Tổng doanh thu ghi nhận sẵn trong bảng là **1.830.085,36**, trong khi nếu lấy từng đơn giá nhân với số lượng sản phẩm bán ra rồi cộng tổng lại thì ra **1.901.153,19**.  
Mức chênh lệch lên tới **71.067,83 đơn vị tiền tệ**, và có tới **9.019 dòng giao dịch (37,58%)** bị lệch quá dung sai cho phép (1 cent).  
Vì dữ liệu nguồn không cung cấp các quy tắc về chiết khấu, thuế, phí sàn hay chuẩn kế toán, một Data Analyst chuẩn mực sẽ không tự ý sửa số liệu mà phải gắn cờ cảnh báo để đối soát với các bên liên quan.

**2. Nguồn thu phân bổ rất rộng rãi giữa các nhà bán hàng:**  
Top 10 nhà bán hàng lớn nhất cộng lại chỉ chiếm **8,44% tổng doanh thu**. Chỉ số Herfindahl-Hirschman (HHI) đạt 42,39 (trên thang điểm 10.000), khẳng định thị trường hoàn toàn không bị chi phối bởi một nhóm độc quyền nào.

**3. Đồ gia dụng (Home) và Đồ điện tử (Electronics) dẫn đầu doanh số:**  
Ngành hàng Home đạt doanh thu cao nhất (416.940,49), bám sát nút phía sau là Electronics (415.820,13).

**4. Dữ liệu tồn kho chỉ là ảnh chụp tĩnh, không phản ánh lịch sử đứt hàng:**  
Cờ `in_stock` là một ảnh chụp không ghi ngày tháng. Dù có 2.936 dòng giao dịch xuất hiện ở các sản phẩm đang có cờ hết hàng, ta không thể vội vàng kết luận đây là thất thoát doanh thu trong quá khứ vì có thể hàng được bán trước khi hết tồn kho.

### Kết Luận Kinh Doanh

Khuyến nghị cấp thiết hàng đầu là: **Phải điều tra và chuẩn hóa lại định nghĩa doanh thu kế toán trước khi sử dụng bộ dữ liệu này cho các báo cáo tài chính chính thức**. Các phân tích về người bán, ngành hàng và tồn kho mang lại góc nhìn vận hành hữu ích, nhưng cần được đặt trong bối cảnh hiểu đúng ranh giới của dữ liệu.

---

## 📚 Mục Lục

1. [Bài Toán Nghiệp Vụ](#-bài-toán-nghiệp-vụ)
2. [Tổng Quan Bộ Dữ Liệu](#-tổng-quan-bộ-dữ-liệu)
3. [Bộ Công Cụ Kỹ Thuật (Tech Stack)](#-bộ-công-cụ-kỹ-thuật-tech-stack)
4. [Quy Trình Phân Tích End-to-End](#-quy-trình-phân-tích-end-to-end)
5. [Định Nghĩa KPI & Quy Tắc Nghiệp Vụ](#-định-nghĩa-kpi--quy-tắc-nghiệp-vụ)
6. [Phân Tích 1: Tổng Quan Doanh Thu Sàn](#-phân-tích-1-tổng-quan-doanh-thu-sàn)
7. [Phân Tích 2: Đối Soát Sai Lệch Doanh Thu Tài Chính](#-phân-tích-2-đối-soát-sai-lệch-doanh-thu-tài-chính)
8. [Phân Tích 3: Hiệu Quả & Mức Độ Tập Trung Người Bán](#-phân-tích-3-hiệu-quả--mức-độ-tập-trung-người-bán)
9. [Phân Tích 4: Hiệu Quả Các Ngành Hàng Sản Phẩm](#-phân-tích-4-hiệu-quả-các-ngành-hàng-sản-phẩm)
10. [Phân Tích 5: Khảo Sát Mối Liên Hệ Trạng Thái Tồn Kho](#-phân-tích-5-khảo-sát-mối-liên-hệ-trạng-thái-tồn-kho)
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

Mô hình sàn thương mại điện tử kết nối hàng trăm, hàng ngàn nhà bán hàng độc lập với người tiêu dùng. Để vận hành sàn hiệu quả, ban giám đốc không thể chỉ nhìn vào một con số tổng doanh thu trên dashboard mà phải nắm bắt được:

- Doanh thu thực tế và khối lượng hàng hóa bán ra
- Hiệu quả kinh doanh của từng ngành hàng
- Mức độ phụ thuộc vào các nhà bán hàng lớn (rủi ro tập trung)
- Khả năng cung ứng và trạng thái còn hàng của sản phẩm
- Sự thống nhất giữa số liệu bán hàng và số liệu tài chính kế toán
- Tính toàn vẹn và độ tin cậy của toàn bộ hệ thống báo cáo

Nếu định nghĩa chỉ số thiếu rõ ràng hoặc số liệu doanh thu bị lệch mà không rõ nguyên nhân, doanh nghiệp rất dễ đưa ra các quyết định phân bổ nguồn lực sai lầm hoặc báo cáo tài chính thiếu chuẩn xác.

### Kịch Bản Phân Tích

Một sàn thương mại điện tử quy mô vừa gồm 316 nhà bán hàng và 1.800 sản phẩm niêm yết. Bộ phận phân tích dữ liệu nhận được dữ liệu nhật ký bán hàng và thông tin bài đăng sản phẩm để đánh giá hiệu quả kinh doanh, đồng thời kiểm tra xem các chỉ số tài chính có đủ tin cậy để đưa vào vận hành thực tế hay không.

### Câu Hỏi Nghiệp Vụ Cốt Lõi

**Doanh thu trên sàn phân bổ như thế nào giữa các nhà bán hàng và ngành hàng, và những vấn đề chất lượng dữ liệu nào đang cản trở việc báo cáo tài chính một cách tự tin?**

---

## 🗄️ Tổng Quan Bộ Dữ Liệu

Dự án sử dụng 2 bảng dữ liệu mô phỏng gồm tổng cộng **25.800 bản ghi**.

### Bảng Dữ Liệu Nguồn

| Bảng dữ liệu | Số bản ghi | Mục đích sử dụng |
|---|---:|---|
| `listings_raw.csv` | 1.800 | Danh sách sản phẩm niêm yết, mã người bán, ngành hàng, giá, đánh giá và trạng thái tồn kho |
| `sales_raw.csv` | 24.000 | Nhật ký giao dịch bán hàng, số lượng bán, doanh thu ghi nhận và thông tin bài đăng |
| **Tổng cộng** | **25.800** | **2 bảng dữ liệu quan hệ** |

### 1. Bảng Listings (Sản Phẩm Niêm Yết)

Mỗi dòng đại diện cho một bài đăng sản phẩm duy nhất trên sàn.

| Cột | Kiểu dữ liệu | Ý nghĩa nghiệp vụ |
|---|---|---|
| `listing_id` | Integer | Mã định danh duy nhất của bài đăng sản phẩm (Khóa chính) |
| `seller_id` | Integer | Mã định danh của nhà bán hàng sở hữu bài đăng |
| `category` | Text | Ngành hàng (Home, Electronics, Sports, Beauty, Toys) |
| `price` | Numeric | Giá niêm yết của sản phẩm |
| `rating` | Numeric | Điểm đánh giá trung bình theo thang 0–5 sao |
| `in_stock` | Binary | Cờ nhị phân chụp trạng thái còn hàng (1: còn hàng, 0: hết hàng) |

### 2. Bảng Sales (Giao Dịch Bán Hàng)

Mỗi dòng đại diện cho một bản ghi bán hàng phát sinh liên kết với bài đăng sản phẩm.

| Cột | Kiểu dữ liệu | Ý nghĩa nghiệp vụ |
|---|---|---|
| `sale_date` | Date | Ngày phát sinh giao dịch bán hàng |
| `listing_id` | Integer | Mã bài đăng sản phẩm liên kết (Khóa ngoại) |
| `units_sold` | Integer | Số lượng đơn vị sản phẩm bán được trong dòng giao dịch |
| `seller_id` | Integer | Mã nhà bán hàng |
| `price` | Numeric | Đơn giá ghi nhận tại dòng giao dịch |
| `rating` | Numeric | Điểm đánh giá ghi nhận |
| `in_stock` | Binary | Cờ tồn kho ghi nhận kèm theo dòng |
| `category` | Text | Ngành hàng của sản phẩm |
| `revenue` | Numeric | Doanh thu ghi nhận của dòng giao dịch |

### Mối Quan Hệ Dữ Liệu & Ranh Giới Grain

Hai bảng kết nối qua trường khóa `listing_id`:

**Listings (1) → (Nhiều) Sales**

**Các lưu ý đặc biệt về grain dữ liệu:**
- Bảng sales không có mã đơn hàng duy nhất (`order_id`) hay mã giao dịch (`transaction_id`). Mỗi dòng là một bản ghi bán hàng, do đó **không được đánh đồng số dòng sales với số lượng đơn hàng**.
- Dữ liệu không cung cấp tỷ lệ hoa hồng của sàn (commission rate) hay phí giao dịch, vì vậy doanh thu ở đây là doanh thu bán hàng ghi nhận, không phải là doanh thu thu phí sàn của công ty vận hành.

Tài liệu chi tiết: [📘 Từ Điển Dữ Liệu](Docs/Data_Dictionary.md) | [📂 Dữ Liệu Thô](Data/raw) | [📂 Dữ Liệu Đã Làm Sạch](Data/clean)

---

## 🛠️ Bộ Công Cụ Kỹ Thuật (Tech Stack)

| Hạng mục | Công nghệ | Ứng dụng thực tế |
|---|---|---|
| Ngôn ngữ lập trình | Python 3.12 | Làm sạch dữ liệu, kiểm thử tự động, đối soát chéo số liệu |
| Ngôn ngữ truy vấn | SQL | Phân tích doanh thu, xếp hạng người bán, phát hiện sai lệch |
| Cơ sở dữ liệu | SQLite | Thực thi truy vấn phân tích quan hệ cục bộ |
| Xử lý dữ liệu | pandas | Đối soát tính toán độc lập giữa Python và SQL |
| Phân tích tài chính | SQL & Python | Đối soát doanh thu ghi nhận và doanh thu tính theo số học |
| Đo lường tập trung | Window Functions | Xếp hạng người bán và tính chỉ số tập trung thị trường HHI |
| Bảng tính Excel | Excel | Sổ tính toán đối soát công thức và mô hình tóm tắt |
| Trực quan hóa | Power BI | Tệp dashboard `.pbix` nguyên bản phục vụ kiểm toán |
| Báo cáo kết quả | HTML & CSV | Xuất bảng kết quả và báo cáo tương tác ngoại tuyến |
| Đảm bảo chất lượng | Python unittest | Bộ kiểm thử tự động toàn diện (19 bài test) |
| Bảo toàn dữ liệu | SHA-256 | Băm mã cryptographic bảo đảm tính toàn vẹn 100% |

---

## 🔄 Quy Trình Phân Tích End-to-End

1. **Xác định bài toán & Ranh giới số liệu:** Làm rõ câu hỏi kinh doanh, xác định cách hiểu đúng của từng trường doanh thu và số lượng.
2. **Khảo sát dữ liệu thô:** Kiểm tra tính toàn vẹn của `listing_id`, tính đồng nhất của các trường thông tin chung (seller, category, price) giữa 2 bảng.
3. **Làm sạch & Chuẩn hóa:** Ép kiểu, kiểm tra giá trị âm và xuất dữ liệu sạch ra `Data/clean/*.csv`. Giữ nguyên dữ liệu thô ban đầu.
4. **Phân tích bằng SQL:** Chạy 4 câu truy vấn phân tích chính: Tổng quan doanh thu sàn, Xếp hạng tập trung người bán, Hiệu quả ngành hàng, và Mối liên hệ trạng thái tồn kho.
5. **Đối soát chéo bằng Python:** Viết mã Python độc lập tính lại các chỉ số tài chính, đếm số dòng lệch và kiểm tra từng số liệu với kết quả SQL.
6. **Đọc hiểu & Khuyến nghị:** Đánh giá các rủi ro vận hành và tài chính, đưa ra lộ trình tháo gỡ điểm nghẽn.
7. **Lưu trữ bằng chứng & Báo cáo:** Tự động sinh báo cáo HTML trực quan và cập nhật manifest băm SHA-256.

---

## 📐 Định Nghĩa KPI & Quy Tắc Nghiệp Vụ

| KPI | Công thức tính toán | Cách hiểu đúng |
|---|---|---|
| Dòng giao dịch bán (Sales Rows) | Đếm số dòng trong bảng sales | Số dòng bán hàng, không phải số đơn hàng |
| Số lượng sản phẩm bán (Units) | Tổng số lượng trường `units_sold` | Tổng sản phẩm bán ra được ghi nhận |
| Doanh thu ghi nhận (Recorded Revenue) | Tổng trường `revenue` | Doanh thu theo dữ liệu nguồn cung cấp |
| Doanh thu tính toán (Price × Units) | Tổng của phép nhân `price * units_sold` | Phép tính số học lý thuyết độc lập |
| Dòng lệch doanh thu (Discrepancy Rows) | Đếm các dòng có `ABS(revenue - price * units) > 0.011` | Các giao dịch có sai lệch cần đối soát |
| Số lượng nhà bán hàng (Sellers) | Đếm số mã `seller_id` riêng biệt có giao dịch | Tập người bán đang phát sinh hoạt động |
| Tỷ trọng doanh thu người bán | Doanh thu người bán ÷ Tổng doanh thu ghi nhận | Mức độ đóng góp của từng người bán |
| Tỷ trọng Top 10 người bán | Tổng doanh thu của 10 người bán lớn nhất ÷ Tổng doanh thu | Đánh giá mức độ phụ thuộc vào đối tác lớn |
| Chỉ số tập trung người bán (HHI) | \(10.000 \times \sum (\text{Tỷ trọng doanh thu người bán})^2\) | Chỉ số mô tả độ tập trung thị trường |
| Doanh thu bình quân bài đăng | Doanh thu trung bình của các listing trong nhóm (kể cả bài 0 đơn) | Chỉ số mô tả hiệu quả niêm yết |

Chi tiết quy tắc: [Nguồn Gốc KPI (KPI Lineage)](Docs/KPI_Lineage.md)

---

## 💰 Phân Tích 1: Tổng Quan Doanh Thu Sàn

### Câu Hỏi Nghiệp Vụ

Quy mô hoạt động thương mại ghi nhận được trên sàn là bao nhiêu?

### Kết Quả Đối Soát

| Chỉ số | Kết quả xác thực |
|---|---:|
| Số dòng giao dịch bán hàng | 24.000 |
| Tổng số lượng sản phẩm bán ra | 48.063 |
| Doanh thu ghi nhận trong bảng | 1.830.085,36 |
| Doanh thu tính theo phép nhân (Đơn giá × Số lượng) | 1.901.153,19 |
| Số nhà bán hàng phát sinh giao dịch | 316 |
| Tổng số bài đăng sản phẩm | 1.800 |

### Các Phát Hiện Chính

- **Hoạt động bán hàng diễn ra sôi động:** 24.000 dòng giao dịch ghi nhận tổng cộng 48.063 sản phẩm bán ra.
- **Quy mô doanh thu đạt trên 1,8 triệu đơn vị tiền tệ:** Doanh thu ghi nhận là 1.830.085,36.
- **Tồn tại hai con số doanh thu không khớp nhau:** Phép nhân đơn giá với số lượng cho ra 1.901.153,19 (chênh lệch hơn 71.000 đơn vị tiền tệ so với số ghi nhận).
- **Không tự ý dán nhãn sai lệch:** Không được tự tiện gọi con số 1,83 triệu này là "doanh thu Amazon" hay "lợi nhuận sàn" vì dữ liệu gốc không có căn cứ pháp lý hay kế toán để chứng minh điều đó.

**Bằng chứng truy vấn:** [Tổng quan doanh số (summary.csv)](Results/summary.csv)

---

## 🧮 Phân Tích 2: Đối Soát Sai Lệch Doanh Thu Tài Chính

### Câu Hỏi Nghiệp Vụ

Tại sao doanh thu ghi nhận trong bảng lại khác biệt so với kết quả phép nhân giữa đơn giá và số lượng bán?

### Bảng Đối Soát Chi Tiết

| Thước đo tài chính | Kết quả |
|---|---:|
| Doanh thu ghi nhận (Recorded Revenue) | 1.830.085,36 |
| Doanh thu tính toán (Price × Units) | 1.901.153,19 |
| Độ lệch tuyệt đối giữa hai tổng số | **71.067,83** |
| Tổng số dòng giao dịch | 24.000 |
| Số dòng bị lệch quá dung sai (> 1 cent) | **9.019 dòng** |
| Tỷ lệ dòng giao dịch bị lệch | **37,58%** |

### Công Thức Đối Soát

Một dòng giao dịch bị coi là "lệch bất thường" khi:
\[
|\text{revenue} - \text{price} \times \text{units\_sold}| > 0,011
\]
(Dung sai 0,011 tương đương hơn 1 cent trong đơn vị tiền tệ mô phỏng).

### Các Phát Hiện Sâu Sắc

1. **Sai lệch có tính hệ thống trên diện rộng:** Có tới 37,58% số dòng giao dịch (9.019 dòng) bị lệch. Điều này khẳng định đây không phải là lỗi làm tròn số ngẫu nhiên ở 1 vài dòng cá biệt, mà phản ánh một quy tắc nghiệp vụ nào đó chưa được tài liệu hóa trong dữ liệu thô.
2. **Tổng giá trị chênh lệch rất lớn:** Chênh lệch tới 71.067,83 đơn vị tiền tệ là một con số trọng yếu đối với bất kỳ báo cáo tài chính nào.
3. **Các giả thuyết có thể đặt ra:**
   - Đơn hàng có áp dụng mã giảm giá nhưng trường `discount` không được lưu riêng.
   - Có khoản khấu trừ phí sàn hoặc thuế trước khi ghi nhận doanh thu vào cột `revenue`.
   - Có đơn hàng bị hoàn tiền một phần (partial refund).
   - Đơn giá `price` là giá niêm yết tại thời điểm trích xuất dữ liệu, trong khi giao dịch thực tế diễn ra ở mức giá khuyến mãi trước đó.
4. **Quyết định đúng đắn của Data Analyst:** Không tự ý lấy phép nhân đè lên cột `revenue`, cũng không tự ý "sửa số cho đẹp". Quy trình phân tích chọn phương án giữ nguyên cả 2 con số, công bố minh bạch và gắn cờ cảnh báo rủi ro tài chính.

**Bằng chứng đối soát:** [Báo cáo chất lượng (quality.json)](Results/quality.json) | [Tóm tắt doanh số (summary.csv)](Results/summary.csv)

---

## 👥 Phân Tích 3: Hiệu Quả & Mức Độ Tập Trung Người Bán

### Câu Hỏi Nghiệp Vụ

Bao nhiêu phần trăm doanh thu đến từ những nhà bán hàng lớn nhất, và sàn có chịu rủi ro bị phụ thuộc vào một số ít đối tác hay không?

### Tổng Quan Về Nhà Bán Hàng (Sellers)

| Chỉ số | Kết quả xác thực |
|---|---:|
| Số lượng nhà bán hàng có giao dịch | 316 nhà bán |
| Nhà bán hàng có doanh thu cao nhất | Seller 223 |
| Doanh thu của Seller 223 | 19.882,06 |
| Tỷ trọng của Seller 223 trên toàn sàn | 1,09% |
| Tỷ trọng của Top 10 nhà bán hàng lớn nhất | **8,44%** |
| Chỉ số tập trung người bán (Seller HHI) | **42,39** |

### Top 10 Nhà Bán Hàng Dẫn Đầu Doanh Thu

| Thứ hạng | Mã người bán (Seller ID) | Doanh thu ghi nhận | Tỷ trọng trên sàn |
|---|---|---:|---:|
| 1 | 223 | 19.882,06 | 1,09% |
| 2 | 264 | 17.618,46 | 0,96% |
| 3 | 247 | 15.950,69 | 0,87% |
| 4 | 114 | 15.485,38 | 0,85% |
| 5 | 307 | 15.376,04 | 0,84% |
| 6 | 269 | 14.661,24 | 0,80% |
| 7 | 86 | 14.459,63 | 0,79% |
| 8 | 283 | 13.731,95 | 0,75% |
| 9 | 61 | 13.720,32 | 0,75% |
| 10 | 218 | 13.522,13 | 0,74% |

### Các Phát Hiện Quan Trọng

1. **Nhà bán hàng số 1 cũng chỉ chiếm 1,09% doanh thu:** Seller 223 dẫn đầu sàn với doanh số 19.882,06, nhưng tỷ trọng rất nhỏ.
2. **Top 10 chỉ chiếm 8,44% doanh thu:** 91,56% doanh thu còn lại đến từ hơn 300 nhà bán hàng khác.
3. **Chỉ số HHI cực thấp (42,39):** Trong kinh tế học, chỉ số HHI dưới 1.500 được xếp vào nhóm thị trường có mức độ tập trung thấp, phân tán cao. Sàn hoàn toàn không có rủi ro bị "thâu tóm" hay phụ thuộc sống còn vào một vài đối tác lớn.

**Bằng chứng truy vấn:** [Tập trung người bán (seller_concentration.csv)](Results/seller_concentration.csv)

---

## 🏷️ Phân Tích 4: Hiệu Quả Các Ngành Hàng Sản Phẩm

### Câu Hỏi Nghiệp Vụ

Ngành hàng nào đóng góp nhiều doanh thu và số lượng sản phẩm bán ra nhất trên sàn?

### Bảng Kết Quả Chi Tiết 5 Ngành Hàng

| Ngành hàng | Doanh thu ghi nhận | Số lượng bán (Units) | Số dòng giao dịch |
|---|---:|---:|---:|
| 🏠 Đồ gia dụng (Home) | 416.940,49 | 10.548 | 5.268 |
| 💻 Đồ điện tử (Electronics) | 415.820,13 | 10.891 | 5.404 |
| 🏅 Đồ thể thao (Sports) | 388.528,46 | 10.387 | 5.203 |
| 💄 Mỹ phẩm (Beauty) | 330.135,80 | 8.639 | 4.324 |
| 🧸 Đồ chơi (Toys) | 278.660,48 | 7.598 | 3.801 |
| **Tổng cộng** | **1.830.085,36** | **48.063** | **24.000** |

### Các Phát Hiện Quan Trọng

1. **Home dẫn đầu về mặt doanh thu:** Đạt 416.940,49 đơn vị tiền tệ, chiếm vị trí quán quân.
2. **Electronics dẫn đầu về mặt sản lượng bán:** Đạt 10.891 sản phẩm bán ra (cao hơn Home với 10.548 sản phẩm). Điều này cho thấy giá trị trung bình trên mỗi sản phẩm của Home cao hơn Electronics.
3. **Cơ cấu ngành hàng khá cân bằng:** Ba ngành hàng dẫn đầu (Home, Electronics, Sports) đóng góp doanh thu rất sát nhau, tạo nên chân kiềng vững chắc cho sàn.

**Bằng chứng truy vấn:** [Hiệu quả ngành hàng (category_performance.csv)](Results/category_performance.csv)

---

## 📦 Phân Tích 5: Khảo Sát Mối Liên Hệ Trạng Thái Tồn Kho

### Câu Hỏi Nghiệp Vụ

Doanh thu bình quân của các bài đăng sản phẩm có sự khác biệt thế nào giữa các dải giá và trạng thái cờ còn hàng/hết hàng?

### Phân Bổ Dải Giá (Price Bands)

- **Dưới 50 (Under 50):** Giá niêm yết < 50
- **Từ 50 đến 99,99 (50 to 99.99):** Giá từ 50 đến dưới 100
- **Từ 100 trở lên (100+):** Giá từ 100 trở lên

### Kết Quả Trích Xuất Tiêu Biểu

| Ngành hàng | Dải giá | Trạng thái tồn kho | Số bài đăng | Doanh thu bình quân bài đăng |
|---|---|---|---:|---:|
| Beauty | 50–99.99 | Hết hàng (Out of Stock) | 17 | 0,00 |
| Beauty | 50–99.99 | Còn hàng (In Stock) | 91 | 1.819,68 |
| Electronics | 50–99.99 | Hết hàng (Out of Stock) | 15 | 0,00 |
| Electronics | 50–99.99 | Còn hàng (In Stock) | 109 | 1.951,91 |
| Home | 50–99.99 | Còn hàng (In Stock) | 106 | 1.927,04 |
| Sports | 50–99.99 | Còn hàng (In Stock) | 95 | 1.846,42 |
| Toys | 50–99.99 | Còn hàng (In Stock) | 74 | 1.860,65 |

### Cảnh Báo Về Mặt Phương Pháp Luận Khi Phân Tích Tồn Kho

Báo cáo chất lượng dữ liệu ghi nhận có **2.936 dòng giao dịch** liên kết với các bài đăng đang có cờ `in_stock = 0`.  
Một người phân tích thiếu kinh nghiệm có thể vội vàng kết luận đây là lỗi hệ thống ("hết hàng sao vẫn bán được?"). Tuy nhiên:
- Cờ `in_stock` trong bộ dữ liệu chỉ là **ảnh chụp tĩnh tại thời điểm trích xuất dữ liệu**, không có mốc thời gian (timestamp).
- Rất có thể các giao dịch đó diễn ra lúc hàng vẫn còn trong kho, và sau khi bán hết thì sản phẩm mới chuyển trạng thái sang hết hàng!
- Do đó, không thể dùng dữ liệu này để tính toán thiệt hại doanh số do đứt hàng (Lost Sales) một cách võ đoán.

**Bằng chứng truy vấn:** [Liên hệ tồn kho (stock_status_association.csv)](Results/stock_status_association.csv)

---

## 💻 Hiện Thực Hóa Bằng SQL

Tất cả các con số phân tích đều được thực thi trực tiếp bằng các truy vấn SQLite chuẩn:

### Truy Vấn 1 — Tổng Hợp Doanh Thu & Đối Soát Sai Lệch

```sql
SELECT
    COUNT(*) AS sales_rows,
    SUM(units_sold) AS units,
    SUM(revenue) AS recorded_revenue,

    -- Tính doanh thu theo số học
    SUM(price * units_sold) AS price_times_units,

    -- Đếm số dòng bị lệch vượt dung sai 1 cent
    SUM(
        ABS(revenue - price * units_sold) > 0.011
    ) AS revenue_discrepancy_rows,

    COUNT(DISTINCT seller_id) AS sellers

FROM sales_clean;
```

### Truy Vấn 2 — Xếp Hạng Mức Độ Tập Trung Người Bán

```sql
WITH seller AS (
    SELECT
        seller_id,
        SUM(revenue) AS revenue
    FROM sales_clean
    GROUP BY seller_id
),

ranked AS (
    SELECT
        *,
        ROW_NUMBER() OVER (
            ORDER BY revenue DESC, seller_id
        ) AS rank,

        SUM(revenue) OVER () AS total_revenue
    FROM seller
)

SELECT
    *,
    revenue / NULLIF(total_revenue, 0) AS revenue_share
FROM ranked
ORDER BY rank;
```

### Truy Vấn 3 — Hiệu Quả Doanh Thu Theo Ngành Hàng

```sql
SELECT
    category,
    SUM(revenue) AS recorded_revenue,
    SUM(units_sold) AS units,
    COUNT(*) AS sales_rows

FROM sales_clean

GROUP BY category

ORDER BY recorded_revenue DESC;
```

### Truy Vấn 4 — Khảo Sát Tồn Kho Bao Gồm Cả Bài Đăng 0 Lượt Bán

```sql
WITH r AS (
    SELECT
        listing_id,
        SUM(revenue) AS revenue
    FROM sales_clean
    GROUP BY listing_id
)

SELECT
    l.category,

    CASE
        WHEN l.price < 50 THEN 'Under 50'
        WHEN l.price < 100 THEN '50 to 99.99'
        ELSE '100+'
    END AS price_band,

    l.in_stock,
    COUNT(*) AS listings,

    -- Sử dụng COALESCE để tính trung bình cả các bài đăng chưa phát sinh lượt bán nào
    AVG(COALESCE(r.revenue, 0)) AS mean_recorded_revenue

FROM listings_clean l

LEFT JOIN r USING(listing_id)

GROUP BY
    l.category,
    price_band,
    l.in_stock

ORDER BY
    l.category,
    price_band,
    l.in_stock;
```

**Xem toàn bộ mã nguồn SQL:** [SQL/analysis.sql](SQL/analysis.sql)

---

## 🐍 Phân Tích Bằng Python & Đối Soát Số Liệu

Mô-đun Python chịu trách nhiệm:
- Đọc và kiểm tra hợp đồng dữ liệu thô của 2 bảng `listings_raw.csv` và `sales_raw.csv`.
- Xác thực tính duy nhất của khóa chính `listing_id` và kiểm tra toàn vẹn khóa ngoại.
- Tính toán chỉ số tập trung thị trường Herfindahl-Hirschman Index (HHI):
  \[
  \text{HHI} = 10.000 \times \sum \left(\frac{\text{Doanh thu người bán}}{\text{Tổng doanh thu}}\right)^2 = 42,3946
  \]
- Đối soát chéo từng chỉ số giữa Python và SQL, phát hiện và cảnh báo 9.019 dòng giao dịch bị lệch số học.

---

## 💡 Khuyến Nghị Kinh Doanh

### Bảng Ưu Tiên Hành Động

| Mức ưu tiên | Đề xuất hành động | Bằng chứng dữ liệu hỗ trợ | Phương án kiểm chứng |
|---|---|---|---|
| 🔴 Cấp thiết | Đối soát và làm rõ định nghĩa Doanh Thu | 9.019 dòng lệch, tổng chênh lệch 71.067,83 | Làm việc với bộ phận Kế toán và Kỹ thuật dữ liệu nguồn |
| 🔴 Rất cao | Ban hành chuẩn báo cáo tài chính chính thức | Doanh thu ghi nhận khác Doanh thu số học | Quy định rõ cách tính chiết khấu, thuế và phí sàn |
| 🟡 Trung bình | Bổ sung nhật ký lịch sử tồn kho theo thời gian | 2.936 dòng bán ở sản phẩm có cờ hết hàng | Nâng cấp hệ thống tracking tồn kho thời gian thực |
| 🟡 Trung bình | Bổ sung mã đơn hàng định danh duy nhất | Thiếu `order_id` khiến không thể đếm số đơn hàng | Bổ sung trường `order_id` vào pipeline thu thập dữ liệu |
| 🟢 Tiêu chuẩn | Duy trì chính sách hỗ trợ đa dạng người bán | HHI = 42,39 (phân tán lành mạnh) | Tiếp tục thu hút các nhà bán hàng quy mô vừa và nhỏ |

### Lộ Trình Triển Khai 30 / 60 / 90 Ngày

- **Ngày 1–30 (Đối soát tài chính):** Rà soát lại thuật toán trích xuất dữ liệu của cột `revenue`. Xác định xem độ lệch 71.067,83 đến từ đâu (chiết khấu, hoàn tiền hay phí sàn).
- **Ngày 31–60 (Chuẩn hóa hệ thống):** Ban hành tài liệu định nghĩa chỉ số KPI kế toán chính thức. Bổ sung trường `order_id` vào hệ thống ghi nhận giao dịch.
- **Ngày 61–90 (Nâng cấp báo cáo):** Xây dựng hệ thống cảnh báo tự động khi xuất hiện giao dịch bị lệch doanh thu. Tích hợp dữ liệu chi phí để đánh giá lợi nhuận thực tế theo từng ngành hàng.

---

## ✅ Chất Lượng Dữ Liệu & Đối Soát

| Tiêu chí kiểm tra | Kết quả ghi nhận |
|---|---:|
| Số bản ghi bài đăng sản phẩm | 1.800 bản ghi |
| Số bản ghi giao dịch bán hàng | 24.000 bản ghi |
| Tổng số dòng dữ liệu nguồn | 25.800 dòng |
| Số ô dữ liệu bắt buộc bị thiếu | 0 ô |
| Dòng giao dịch trùng lặp nguyên bản | 140 dòng (được đếm và giữ nguyên) |
| Dòng giao dịch bị lệch doanh thu | 9.019 dòng (gắn cờ kiểm tra) |
| Dòng giao dịch gắn cờ hết hàng | 2.936 dòng (cảnh báo ngữ nghĩa) |
| Số bài kiểm thử tự động vượt qua | 19/19 passed |

**Các tệp kết quả kiểm thử:**
- [validation.json](Results/validation.json) — Biên bản kiểm thử tự động lúc chạy thực tế
- [quality.json](Results/quality.json) — Báo cáo các phát hiện bất thường và sai lệch dữ liệu
- [manifest.json](Results/manifest.json) — Mã băm cryptographic SHA-256 bảo đảm tính toàn vẹn

---

## 📊 Tài Sản Business Intelligence & Dashboard

| Tài sản | Vị trí | Mục đích sử dụng |
|---|---|---|
| Sổ làm việc Excel | [Excel Model](Excel/04_Amazon_Marketplace_Analytics_Model.xlsx) | Sổ tính toán đối soát công thức chuẩn |
| Tệp Power BI PBIX cũ | [Power BI Dashboard](Dashboard/Amazon_Marketplace_Analytics_Dashboard.pbix) | Dashboard nguyên bản phục vụ kiểm toán |
| Ảnh chụp Dashboard | [Thư mục Images](Images/amazon_marketplace_dashboard.png) | Ảnh chụp giao diện dashboard gốc |
| Báo cáo HTML độc lập | [REPORT.html](REPORT.html) | Báo cáo trực quan độc lập hoàn chỉnh |

### Trạng Thái Đối Soát Dashboard Power BI Gốc

Rà soát kỹ thuật cho thấy dashboard Power BI gốc sử dụng một mô hình nhúng chứa khoảng 85.000 dòng `fact_orders`, hoàn toàn khác biệt về quy mô và schema so với 24.000 dòng sales chuẩn của dự án. Vì vậy, tệp PBIX cũ được giữ lại làm tài sản kiểm toán lịch sử, trong khi báo cáo `REPORT.html` đại diện cho các con số phân tích chuẩn xác đã qua kiểm định.

Xem thêm: [Biên Bản Đối Soát Dashboard](Docs/Dashboard_Reconciliation.md) | [Ánh Xạ Trường Dữ Liệu](Docs/Dashboard_Field_Mapping.md) | [Hướng Dẫn Kết Nối](Docs/Connect_To_Dashboard.md)

---

## 📂 Cấu Trúc Thư Mục Dự Án

```text
04_Amazon_Marketplace_Analytics/
│
├── Data/
│   ├── raw/                              # Dữ liệu CSV thô ban đầu (25.800 dòng)
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
│   └── 04_Amazon_Marketplace_Analytics_Model.xlsx  # Sổ tính toán đối soát
│
├── Dashboard/
│   ├── Amazon_Marketplace...pbix         # Dashboard Power BI nguyên bản
│   └── README.md                         # Hướng dẫn tái lập dashboard
│
├── Images/
│   └── amazon_marketplace_dashboard.png  # Ảnh chụp dashboard gốc
│
├── Results/
│   ├── summary.csv                       # Tổng quan doanh số sàn
│   ├── seller_concentration.csv          # Xếp hạng và tỷ trọng người bán
│   ├── category_performance.csv          # Hiệu quả theo ngành hàng
│   ├── stock_status_association.csv      # Khảo sát liên hệ tồn kho
│   ├── additional_metrics.json           # Các chỉ số bổ trợ (HHI, Top 10 share)
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

# 4. Chạy phân tích dự án Sàn Thương Mại
python -m portfolio.run --project 04_Amazon_Marketplace_Analytics

# 5. Chạy bộ kiểm thử tự động
python -m unittest discover -s tests -v
```

Sau khi chạy xong, mở tệp `04_Amazon_Marketplace_Analytics/REPORT.html` trên trình duyệt web bất kỳ để tương tác với báo cáo trực quan hoàn chỉnh.

---

## ⚠️ Giới Hạn Phân Tích & Hướng Phát Triển

### Giới Hạn Hiện Tại

1. **Dữ liệu mô phỏng:** Dữ liệu phục vụ portfolio, không đại diện cho hoạt động thương mại của tập đoàn Amazon.
2. **Thiếu mã đơn hàng duy nhất:** Không có `order_id` nên không thể xác định quy mô giỏ hàng hay số lượng đơn hàng thực tế.
3. **Chưa rõ nguyên nhân sai lệch doanh thu:** Sai lệch 71.067,83 giữa doanh thu ghi nhận và doanh thu tính toán cần được đối soát thêm với quy tắc nghiệp vụ nguồn.
4. **Thiếu thông tin phí sàn:** Không có dữ liệu về tỷ lệ hoa hồng nên không tính được doanh thu thực thu của công ty quản lý sàn.
5. **Dữ liệu tồn kho thiếu chiều thời gian:** Cờ tồn kho không có ngày tháng, không thể suy diễn thất thu do hết hàng.

### Hướng Phát Triển Tương Lai

- Bổ sung trường mã giao dịch duy nhất (`transaction_id`) và mã đơn hàng (`order_id`).
- Tích hợp bảng biểu phí hoa hồng (Commission Rate Schedule) để tính doanh thu thực của sàn.
- Xây dựng hệ thống theo dõi biến động tồn kho theo thời gian thực (Time-series Inventory Tracking).
- Phân tích vòng đời và tỷ lệ giữ chân nhà bán hàng (Seller Retention Cohorts).

---

## 🧠 Đúc Kết Từ Dự Án

### Giá Trị Kỹ Thuật

- Thành thạo kỹ năng kết nối, biến đổi và phân tích dữ liệu bán hàng đa chiều bằng SQL.
- Ứng dụng các hàm cửa sổ Window Functions tính toán chỉ số tập trung kinh tế HHI.
- Tự động hóa kiểm tra tính toàn vẹn dữ liệu và đối soát số học bằng Python.

### Giá Trị Nghiệp Vụ

- Không chấp nhận dữ liệu một cách thụ động: dũng cảm phát hiện và nêu bật sự bất thường trong số liệu tài chính thay vì giấu giếm.
- Hiểu rõ ranh giới của dữ liệu: không suy diễn bừa bãi khi dữ liệu thiếu mốc thời gian hay định nghĩa chuẩn.
- Đề xuất các giải pháp quản trị dữ liệu thiết thực giúp doanh nghiệp xây dựng hệ thống báo cáo vững chắc.

---

## 📚 Tài Liệu Hỗ Trợ & Bằng Chứng

| Tài nguyên | Nội dung chi tiết |
|---|---|
| [Từ Điển Dữ Liệu](Docs/Data_Dictionary.md) | Giải thích schema dữ liệu nguồn và hợp đồng kiểm thử |
| [Nguồn Gốc KPI](Docs/KPI_Lineage.md) | Công thức tính toán và quy tắc nghiệp vụ |
| [Mã Nguồn SQL Phân Tích](SQL/analysis.sql) | Toàn bộ câu truy vấn SQL thực thi |
| [Tổng Quan Doanh Số](Results/summary.csv) | Kết quả các chỉ số kinh doanh chính |
| [Tập Trung Người Bán](Results/seller_concentration.csv) | Bảng xếp hạng và tỷ trọng người bán |
| [Hiệu Quả Ngành Hàng](Results/category_performance.csv) | Bảng doanh thu và sản lượng theo ngành hàng |
| [Khảo Sát Tồn Kho](Results/stock_status_association.csv) | Bảng liên hệ giữa giá, tồn kho và doanh thu |
| [Báo Cáo Kiểm Thử](Results/validation.json) | Biên bản kiểm thử tự động lúc chạy thực tế |
| [Báo Cáo HTML Độc Lập](REPORT.html) | Báo cáo trực quan ngoại tuyến hoàn chỉnh |

---

## 👨‍💻 Về Tác Giả

**Bùi Nhất Phong**  
Data Analytics | Business Intelligence | SQL | Python | Phân Tích Nghiệp Vụ

Tôi đam mê việc biến các tập dữ liệu phức tạp thành các chỉ số kinh doanh đáng tin cậy, phát hiện các điểm nghẽn báo cáo, đánh giá hiệu quả vận hành và truyền tải những góc nhìn sâu sắc hỗ trợ ra quyết định.

Các lĩnh vực quan tâm hàng đầu của tôi: Phân tích Sàn thương mại & E-commerce, Đối soát tài chính, Business Intelligence, Quản trị chất lượng dữ liệu và Phân tích nghiệp vụ.

📧 [Email](mailto:buinhatphong.analytics@gmail.com)  
💼 [LinkedIn](https://www.linkedin.com/in/buinhatphong/)  
💻 [GitHub Profile](https://github.com/buinhatphong)

### 🔗 Khám Phá Thêm Dự Án Trong Portfolio

[⬅️ Quay lại Trang Tổng Quan Portfolio](../README.md)

[🛒 Dự án trước: Phân Tích Sản Phẩm Thương Mại Điện Tử](../03_Ecommerce_Product_Analytics/README.md)

[🔍 Dự án tiếp theo: Phân Tích Hành Trình Khách Hàng](../05_User_Journey_Analytics/README.md)

---

**📦 Phân Tích Sàn Thương Mại Điện Tử Amazon | Xây dựng bởi Bùi Nhất Phong**  
*Góc nhìn sâu sắc từ SQL. Số liệu kiểm chứng bằng Python. Đối soát tài chính minh bạch và chuẩn xác.*

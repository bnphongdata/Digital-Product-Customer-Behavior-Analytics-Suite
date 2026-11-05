# 📊 Portfolio Phân Tích Dữ Liệu | Bùi Nhất Phong

**Data Analytics • SQL • Python • Excel • Business Intelligence • Phân tích Thống kê**

**Biến dữ liệu phức tạp thành góc nhìn kinh doanh thực tế thông qua phân tích có khả năng tái lập, đối soát chất lượng dữ liệu, tư duy thống kê và báo cáo tập trung vào việc ra quyết định.**

[![Validate analysis](https://github.com/buinhatphong/digital-product-analytics-portfolio/actions/workflows/validate.yml/badge.svg)](https://github.com/buinhatphong/digital-product-analytics-portfolio/actions/workflows/validate.yml)

![Python](https://img.shields.io/badge/Python-3.12-blue)
![SQL](https://img.shields.io/badge/SQL-SQLite-4479A1)
![Dự án](https://img.shields.io/badge/Analytics_Projects-5-success)
![Kiểm thử](https://img.shields.io/badge/Automated_Tests-48-informational)

🌐 [LinkedIn](https://www.linkedin.com/in/buinhatphong/) | 💻 [GitHub](https://github.com/buinhatphong) | 📧 [Email](mailto:buinhatphong.analytics@gmail.com)

---

## 🖥️ Trải Nghiệm Portfolio Tương Tác

**[Mở trình khám phá dữ liệu ngoại tuyến (Analytics Explorer)](demo/analytics-explorer.html)** · [Cách thức kiểm tra đối soát dữ liệu](docs/INTERACTIVE_EXPLORER.md)

Đây là công cụ so sánh 5 dự án chạy độc lập trong trình duyệt, hỗ trợ lọc theo chỉ số KPI, phân khúc khách hàng và thứ hạng. Toàn bộ số liệu hiển thị đều được trích xuất trực tiếp từ các tệp CSV kết quả SQL đã lưu trong kho lưu trữ và được kiểm thử tự động đối soát với nguồn. Bạn chỉ cần tải tệp HTML về và mở trực tiếp trên trình duyệt máy tính (trình xem mã nguồn của GitHub không chạy JavaScript trực tiếp). Bản demo dùng tập dữ liệu mô phỏng, không gửi request ra mạng bên ngoài, và hoạt động độc lập không phụ thuộc vào dashboard Power BI hay Tableau gốc.

**Xác thực tự động (CI/CD):** Quy trình [GitHub Actions](.github/workflows/validate.yml) tự động chạy toàn bộ các bài kiểm thử unit/integration bằng Python, làm mới dữ liệu đầu ra từ SQL/Python, đối soát mã băm SHA-256 của các tệp kết quả và quét lịch sử Git để đảm bảo an toàn thông tin. Việc vượt qua CI là bằng chứng chứng minh mã nguồn chạy đúng theo phạm vi kiểm thử được thiết kế.

---

## 👨‍💻 Giới Thiệu Về Portfolio

Chào bạn! Đây là Portfolio Phân Tích Dữ Liệu của mình, gồm 5 dự án phân tích thực chiến từ đầu đến cuối (end-to-end). Portfolio này thể hiện cách mình chuyển hóa dữ liệu thô thành các chỉ số đáng tin cậy, tìm ra xu hướng kinh doanh, rà soát lỗi dữ liệu và đưa ra những khuyến nghị thực tế giúp doanh nghiệp ra quyết định chuẩn xác hơn.

Quan điểm làm việc của mình là kết hợp kỹ thuật xử lý dữ liệu với tư duy kinh doanh. Thay vì chỉ đưa ra những con số vô hồn, mình luôn chú trọng tìm hiểu bản chất cách tính của từng chỉ số, kiểm tra độ chính xác, đánh giá mức độ tin cậy và giải thích ý nghĩa số liệu bằng ngôn ngữ kinh doanh gần gũi, dễ hiểu.

Portfolio này bao gồm các kỹ năng thực tế:

- **SQL:** Truy vấn trích xuất dữ liệu, kết nối bảng (JOIN), lọc dữ liệu, gom nhóm và tính toán tổng hợp, bảng tạm (CTE), hàm cửa sổ (window functions), phân tích chuyên sâu và tối ưu kế hoạch truy vấn (query plan).
- **Python:** Xử lý và biến đổi dữ liệu với thư viện pandas, tính toán thống kê, tự động hóa quy trình phân tích, viết kiểm thử tự động và xuất báo cáo.
- **Làm sạch dữ liệu & ETL:** Kiểm tra cấu trúc bảng (schema), chuẩn hóa kiểu dữ liệu, xác thực khóa chính - khóa ngoại, đảm bảo tính tái lập và truy xuất nguồn gốc từ đầu vào đến đầu ra.
- **Phân tích khám phá dữ liệu (EDA):** Nhận diện quy luật, phân khúc dữ liệu, so sánh hiệu suất giữa các nhóm, phân tích phễu chuyển đổi và đo lường mức độ tập trung doanh thu.
- **Phân tích thống kê:** Kiểm định giả thuyết (hypothesis testing), tính toán khoảng tin cậy (confidence interval), phân tích tỷ lệ chuyển đổi và giải thích kết quả thử nghiệm A/B.
- **Business Intelligence (BI):** Chuẩn hóa định nghĩa KPI, đối soát báo cáo, kiểm tra công thức bảng tính Excel, trích xuất dữ liệu Tableau Hyper và xây dựng bằng chứng xác thực measure trong Power BI.
- **Chất lượng dữ liệu (Data Quality):** Rà soát dòng trùng lặp, kiểm tra tính toàn vẹn quan hệ, kiểm tra tính tuần tự thời gian và đối soát chéo kết quả giữa SQL và Python.
- **Giao tiếp & Báo cáo kinh doanh:** Trình bày kết quả rõ ràng, minh bạch các giả định phân tích, đưa ra khuyến nghị thực tế và tài liệu hóa chi tiết từng bước làm.

**Tính minh bạch về dữ liệu:** Toàn bộ các dự án trong portfolio đều sử dụng các tập dữ liệu mô phỏng được cung cấp sẵn. Kết quả phân tích phản ánh đặc điểm của các tập dữ liệu này và không đại diện cho số liệu kinh doanh của bất kỳ khách hàng hay hệ thống thực tế nào.

---

## 🚀 Tổng Quan Về Portfolio

| Chỉ số Portfolio | Bằng chứng được ghi nhận |
|---|---|
| Số lượng dự án phân tích end-to-end | 5 dự án |
| Số dòng dữ liệu gốc | 121.366 dòng trên 10 tệp CSV |
| Số bước kiểm tra xác thực runtime | 93 bước |
| Số bài test tự động (unit/integration test) | 48 bài |
| Phương pháp phân tích | SQL, Python, thống kê mô tả, suy diễn thử nghiệm A/B |
| Định dạng báo cáo | Báo cáo HTML offline, tệp CSV kết quả, bảng tính Excel, tài liệu đối soát BI |
| Khả năng tái lập | Python 3.12, SQLite, quản lý phiên bản thư viện rõ ràng |
| Theo dõi tính toàn vẹn | Quản lý mã băm SHA-256 manifest và lưu trữ kết quả kiểm tra |

Các bài kiểm tra này nhằm xác minh tính chính xác về mặt kỹ thuật và tính toán; không khẳng định việc triển khai trên môi trường production thực tế hay thay thế hoàn toàn giao diện trực quan gốc của Power BI/Tableau Desktop.

### Điều Hướng Nhanh

- 📂 [Khám phá 5 dự án phân tích nổi bật](#-5-dự-án-phân-tích-nổi-bật)
- 🛠️ [Kỹ năng kỹ thuật & Công cụ sử dụng](#-kỹ-năng-kỹ-thuật--công-cụ-sử-dụng)
- 🔄 [Quy trình phân tích dữ liệu thực tế](#-quy-trình-phân-tích-dữ-liệu-thực-tế)
- ✅ [Kiểm thử & Đảm bảo chất lượng dữ liệu](#-kiểm-thử--đảm-bảo-chất-lượng-dữ-liệu)
- 📊 [Đối soát Business Intelligence & Sổ làm việc gốc](#-đối-soát-business-intelligence--sổ-làm-việc-gốc)
- 💻 [Cách chạy lại dự án trên máy của bạn](#-cách-chạy-lại-dự-án-trên-máy-của-bạn)
- 📚 [Tài liệu kỹ thuật & Hướng dẫn đi kèm](#-tài-liệu-kỹ-thuật--hướng-dẫn-đi-kèm)

---

## 📁 5 Dự Án Phân Tích Nổi Bật

Năm nghiên cứu tình huống (case studies) giải quyết các bài toán kinh doanh điển hình: mô hình SaaS, thử nghiệm tính năng, sàn thương mại điện tử, đối soát doanh thu và hành trình khách hàng.

### 01 | 📈 Phân Tích Sản Phẩm SaaS — StreamFlow

**Trọng tâm:** Kích hoạt người dùng, Doanh thu gói thuê bao, Phễu Onboarding & Phân tích Churn

**Bài toán kinh doanh**

Người dùng gặp khó khăn và rơi rụng nhiều nhất ở bước nào trong quy trình onboarding, và mức độ hoạt động của khách hàng có mối liên hệ như thế nào với nhãn rời bỏ (churn)?

**Cách tiếp cận phân tích**

- Khai thác dữ liệu ở cả 3 cấp độ: thông tin người dùng, gói thuê bao và lịch sử sự kiện (event logs).
- Dùng SQL tổng hợp doanh thu thuê bao, phân loại nhóm khách hàng và đo lường tiến độ onboarding.
- Xây dựng phễu tuần tự theo dòng thời gian để tìm ra bước kích hoạt có tỷ lệ rơi rụng cao nhất.
- Khảo sát mối tương quan giữa mức độ sử dụng tính năng và nhãn churn được gắn sẵn.
- Tự động đối soát chéo toàn bộ chỉ số chính bằng các hàm tính độc lập trong Python.

**Kết quả chính**

| Chỉ số KPI | Kết quả thực tế |
|---|---:|
| Tổng số người dùng | 1.500 |
| Người dùng trả phí | 698 |
| Doanh thu định kỳ hàng tháng (MRR Snapshot) | 189.975,00 |
| Doanh thu định kỳ quy năm (ARR Snapshot) | 2.279.700,00 |
| Tỷ lệ churn ở nhóm trả phí | 21,06% |
| Tỷ lệ rơi rụng từ Bước 1 sang Bước 2 (Onboarding) | 62,59% |

Doanh thu được thể hiện theo đơn vị tiền tệ quy ước trong dữ liệu. Con số ARR được ước tính từ ảnh chụp MRR tại thời điểm lấy dữ liệu, không phải số liệu ghi nhận theo chuẩn kế toán.

**Góc nhìn & Đề xuất kinh doanh**

Mức rơi rụng lớn nhất diễn ra ngay khi người dùng chuyển từ bước tạo tài khoản sang bước thiết lập không gian làm việc (Workspace). Doanh nghiệp nên ưu tiên nghiên cứu trải nghiệm người dùng (UX research) tại bước này, rà soát lại cơ chế tracking sự kiện và thiết kế thử nghiệm A/B để tối ưu quy trình onboarding trước khi kết luận về tác động giữ chân khách hàng.

**Kỹ năng thể hiện:** Gom nhóm dữ liệu trong SQL, thống kê mô tả về churn, tính toán chỉ số tài chính SaaS, dựng phễu tuần tự, đối soát KPI và đề xuất giải pháp kinh doanh.

**Tài nguyên dự án**

[📖 Chi tiết Case Study](01_SaaS_Product_Analytics_StreamFlow/README.md) | [💻 Mã SQL phân tích](01_SaaS_Product_Analytics_StreamFlow/SQL/analysis.sql) | [📊 Bảng kết quả CSV](01_SaaS_Product_Analytics_StreamFlow/Results) | [📄 Báo cáo HTML hoàn chỉnh](01_SaaS_Product_Analytics_StreamFlow/REPORT.html)

---

## 02 | 🧪 Thử Nghiệm A/B — Đánh Giá Tác Động Của Tính Năng Mới

**Trọng tâm:** Kiểm định giả thuyết thống kê, Tối ưu hóa tỷ lệ chuyển đổi & Đánh giá thử nghiệm

**Bài toán kinh doanh**

Biến thể thử nghiệm B (Variant B) có thực sự đem lại tỷ lệ chuyển đổi phiên cao hơn nhóm gốc (Control) hay không, và mức độ chắc chắn của sự chênh lệch này là bao nhiêu?

**Cách tiếp cận phân tích**

- Phân tích 12.000 phiên truy cập trong tập dữ liệu thử nghiệm mô phỏng.
- So sánh tỷ lệ chuyển đổi giữa nhóm Control và Variant B.
- Thực hiện kiểm định z-test gộp hai phía cho hai tỷ lệ (two-sided pooled z-test).
- Tính khoảng tin cậy 95% Newcombe-Wilson cho mức chênh lệch tuyệt đối.
- Đo lường mức tăng trưởng tuyệt đối và tương đối.
- Khảo sát các chỉ số cảnh báo rủi ro (guardrail metrics) như tỷ lệ thoát (bounce rate), doanh thu trung bình mỗi phiên và điểm tương tác.
- Làm rõ các giả định về việc phân bổ ngẫu nhiên và tính độc lập của các phiên.

**Kết quả chính**

| Chỉ số KPI | Kết quả thực tế |
|---|---:|
| Số phiên nhóm Control | 5.987 |
| Số phiên nhóm Variant B | 6.013 |
| Tỷ lệ chuyển đổi nhóm Control | 19,84% |
| Tỷ lệ chuyển đổi nhóm Variant B | 23,08% |
| Mức tăng tuyệt đối (Absolute Lift) | +3,24 điểm phần trăm |
| Mức tăng tương đối (Relative Lift) | +16,33% |
| Khoảng tin cậy 95% cho độ chênh lệch | +1,77 đến +4,71 điểm phần trăm |
| Giá trị p-value (kiểm định hai phía) | Xấp xỉ 0,0000154 |

**Góc nhìn & Đề xuất kinh doanh**

Variant B cho thấy tỷ lệ chuyển đổi cao hơn rõ rệt trong tập dữ liệu thử nghiệm. Tuy nhiên, một kết quả có ý nghĩa thống kê (statistically significant) chưa đủ để tự động quyết định ra mắt tính năng cho toàn bộ người dùng.

Để triển khai an toàn trong thực tế, nhóm sản phẩm cần xác minh lại đơn vị phân bổ ngẫu nhiên (phiên hay người dùng), kiểm tra log phân bổ thực tế, đánh giá thời gian chạy thử nghiệm và kiểm soát các chỉ số rủi ro về mặt vận hành.

**Kỹ năng thể hiện:** Phương pháp A/B test, suy diễn thống kê, lập trình Python, truy vấn SQL, báo cáo thử nghiệm, phân tích chuyển đổi và ra quyết định dựa trên bằng chứng.

**Tài nguyên dự án**

[📖 Chi tiết Case Study](02_AB_Test_Feature_Impact/README.md) | [💻 Mã SQL phân tích](02_AB_Test_Feature_Impact/SQL/analysis.sql) | [📊 Bảng kết quả CSV](02_AB_Test_Feature_Impact/Results) | [📄 Báo cáo HTML hoàn chỉnh](02_AB_Test_Feature_Impact/REPORT.html)

---

## 03 | 🛒 Phân Tích Sản Phẩm Thương Mại Điện Tử

**Trọng tâm:** Phễu chuyển đổi, Bỏ giỏ hàng, Hành vi theo phiên & Mức độ tập trung sản phẩm (SKU)

**Bài toán kinh doanh**

Những phân khúc người dùng nào gặp nhiều trở ngại nhất khi mua hàng, và doanh thu phân bổ như thế nào giữa các mặt hàng khác nhau?

**Cách tiếp cận phân tích**

- Khảo sát các phiên truy cập trang web kết nối với các bản ghi đơn hàng phát sinh.
- Đo lường chi tiết tỷ lệ chuyển đổi phiên và tỷ lệ bỏ giỏ hàng (cart abandonment).
- So sánh hành vi mua sắm giữa các loại thiết bị (Desktop vs Mobile) và kênh tiếp thị (Organic, Paid, Email, v.v.).
- Đánh giá mức độ tập trung doanh thu theo từng mã SKU dựa trên nguyên lý Pareto (80/20).
- Khảo sát mối liên hệ của việc áp dụng mã giảm giá mà không suy diễn vội vã quan hệ nhân quả.
- Đối soát định nghĩa phễu và công thức tính toán để đảm bảo số liệu chính xác.

**Kết quả chính**

| Chỉ số KPI | Kết quả thực tế |
|---|---:|
| Tổng số phiên truy cập | 25.000 |
| Số lượt mua hàng thành công | 3.037 |
| Tỷ lệ chuyển đổi phiên | 12,15% |
| Tỷ lệ bỏ giỏ hàng | 64,24% |
| Tổng doanh thu đơn hàng ghi nhận | 198.586 |
| Giá trị đơn hàng trung bình (AOV) | 65,39 |
| Tỷ trọng doanh thu của top 20% SKU | 31,42% |

**Góc nhìn & Đề xuất kinh doanh**

Tỷ lệ bỏ giỏ hàng hơn 64% là cơ hội lớn để tối ưu, nhất là ở các phân khúc có lưu lượng truy cập cao nhưng tỷ lệ bỏ giỏ lớn (như thiết bị di động từ kênh quảng cáo trả phí).

Về mặt danh mục hàng hóa, top 20% SKU chỉ chiếm khoảng 31,42% doanh thu, cho thấy doanh thu phân bổ tương đối dàn trải chứ không tập trung cực đoan vào một vài sản phẩm chủ lực. Doanh nghiệp nên rà soát lại chính sách tồn kho và hiển thị sản phẩm thay vì vội vàng cắt giảm danh mục.

**Kỹ năng thể hiện:** Kết nối bảng (SQL JOIN), phân tích phiên truy cập, phân khúc dữ liệu, tính toán tỷ lệ chuyển đổi, phân tích doanh thu Pareto và kiểm chứng KPI.

**Tài nguyên dự án**

[📖 Chi tiết Case Study](03_Ecommerce_Product_Analytics/README.md) | [💻 Mã SQL phân tích](03_Ecommerce_Product_Analytics/SQL/analysis.sql) | [📊 Bảng kết quả CSV](03_Ecommerce_Product_Analytics/Results) | [📄 Báo cáo HTML hoàn chỉnh](03_Ecommerce_Product_Analytics/REPORT.html)

---

## 04 | 📦 Phân Tích Sàn Thương Mại Điện Tử — Doanh Thu & Người Bán

**Trọng tâm:** Báo cáo hoạt động sàn, Mức độ tập trung người bán, Đối soát doanh thu & Chất lượng dữ liệu

**Bài toán kinh doanh**

Doanh thu ghi nhận trên sàn phân bổ ra sao giữa các nhà bán hàng (sellers), và những sai lệch dữ liệu nào đang cản trở việc đối soát tài chính hoàn chỉnh?

**Cách tiếp cận phân tích**

- Phân tích các dòng giao dịch bán hàng và thông tin niêm yết của người bán.
- Tính toán doanh thu theo ngành hàng và phân tích mức độ tập trung doanh thu vào top nhà bán hàng.
- So sánh doanh thu ghi nhận trong dữ liệu với phép tính số lượng bán × giá niêm yết.
- Xác định cụ thể các dòng giao dịch bị lệch để chuyển nhóm quản trị dữ liệu nguồn điều tra.
- Khảo sát mối tương quan giữa trạng thái tồn kho và doanh thu trung bình.
- Giữ nguyên các điểm bất thường của dữ liệu nguồn để phản ánh trung thực, không tự ý can thiệp làm sai lệch số liệu.

**Kết quả chính**

| Chỉ số KPI | Kết quả thực tế |
|---|---:|
| Tổng số dòng bán hàng | 24.000 |
| Tổng số lượng sản phẩm bán ra | 48.063 |
| Số lượng nhà bán hàng (Sellers) | 316 |
| Doanh thu ghi nhận theo nguồn | 1.830.085,36 |
| Số dòng bị lệch giá trị doanh thu | 9.019 dòng |
| Tỷ trọng doanh thu của Top 10 người bán | 8,44% |

**Góc nhìn & Đề xuất kinh doanh**

Việc có tới hơn 9.000 dòng dữ liệu lệch giữa giá × số lượng và doanh thu ghi nhận cho thấy tầm quan trọng của việc đối soát nguồn trước khi sử dụng số liệu vào báo cáo tài chính chính thức. Phân tích này giữ nguyên giá trị doanh thu gốc thay vì võ đoán áp đặt các giả định chưa được kiểm chứng về phí sàn hay chiết khấu.

Mức độ tập trung của top 10 người bán ở mức 8,44% cho thấy sàn có mức độ đa dạng người bán tốt, rủi ro phụ thuộc vào một vài cá nhân hay cửa hàng lớn là không cao.

**Kỹ năng thể hiện:** SQL phân tích tài chính, kiểm tra tính toàn vẹn dữ liệu, đối soát chéo, phân khúc người bán, phát hiện điểm bất thường và lập báo cáo quản trị.

**Tài nguyên dự án**

[📖 Chi tiết Case Study](04_Amazon_Marketplace_Analytics/README.md) | [💻 Mã SQL phân tích](04_Amazon_Marketplace_Analytics/SQL/analysis.sql) | [📊 Bảng kết quả CSV](04_Amazon_Marketplace_Analytics/Results) | [📄 Báo cáo HTML hoàn chỉnh](04_Amazon_Marketplace_Analytics/REPORT.html)

---

## 05 | 🔍 Phân Tích Hành Trình Khách Hàng (User Journey)

**Trọng tâm:** Hành vi người dùng, Tiến trình phễu, Theo dõi sự kiện (Tracking) & Tính chuẩn xác về thời gian

**Bài toán kinh doanh**

Số lượng người mua hàng quan sát được thực tế so với phễu chuyển đổi tuần tự nghiêm ngặt theo thời gian chênh lệch như thế nào, và điều này phản ánh điều gì về chất lượng hệ thống tracking sự kiện?

**Cách tiếp cận phân tích**

- Phân tích chuỗi hành động của người dùng qua các giai đoạn trong hành trình mua hàng.
- Phân biệt rõ giữa tỷ lệ tiếp cận giai đoạn (stage reach) và tỷ lệ hoàn thành phễu tuần tự (ordered funnel).
- Kiểm tra tính hợp lệ về mặt thời gian giữa các bước liên tiếp nhau.
- So sánh tỷ lệ mua hàng giữa nhóm người dùng mới và người dùng quay lại.
- Khảo sát phân phối thời gian (số ngày) từ khi xuất hiện lần đầu đến khi mua hàng.
- Chỉ rõ các điểm bất cập trong dữ liệu khiến việc kết luận về tỷ lệ bỏ phễu trở nên thiếu căn cứ.

**Kết quả chính**

| Chỉ số KPI | Kết quả thực tế |
|---|---:|
| Tổng số người dùng | 6.000 |
| Số người mua hàng quan sát được | 627 |
| Tỷ lệ mua hàng thực tế | 10,45% |
| Thời gian mua hàng trung vị (P50) | 7 ngày |
| Thời gian mua hàng phân vị 90 (P90) | 12 ngày |
| Số người dùng bị đảo lộn ngày giữa các bước kế tiếp | 3.296 |
| Số người dùng hoàn thành đủ 6 bước đúng thứ tự ngày | 0 |

**Góc nhìn & Đề xuất kinh doanh**

Dữ liệu ghi nhận thực tế có 627 người dùng có phát sinh sự kiện mua hàng (Purchase), nhưng không có bất kỳ ai hoàn thành đủ 6 bước đúng theo trình tự ngày tăng dần nghiêm ngặt.

Sự mâu thuẫn này chỉ ra rằng hệ thống tracking đang gặp lỗi ghi nhận thời gian sự kiện (timestamp sequencing error), chứ không phải người dùng không mua hàng hay tỷ lệ bỏ thanh toán là 100%. Hành động đúng đắn của Data Analyst lúc này là phối hợp với đội ngũ kỹ thuật để chuẩn hóa lại cơ chế ghi nhận sự kiện trước khi tiến hành tối ưu hóa giao diện.

**Kỹ năng thể hiện:** Hàm cửa sổ trong SQL, phân tích chuỗi thời gian, phân khúc người dùng, phân tích phễu hành trình, kiểm định dữ liệu bằng Python và đánh giá chất lượng hệ thống tracking.

**Tài nguyên dự án**

[📖 Chi tiết Case Study](05_User_Journey_Analytics/README.md) | [💻 Mã SQL phân tích](05_User_Journey_Analytics/SQL/analysis.sql) | [📊 Bảng kết quả CSV](05_User_Journey_Analytics/Results) | [📄 Báo cáo HTML hoàn chỉnh](05_User_Journey_Analytics/REPORT.html)

---

## 🛠️ Kỹ Năng Kỹ Thuật & Công Cụ Sử Dụng

| Nhóm kỹ năng | Công nghệ & Năng lực chuyên môn |
|---|---|
| Ngôn ngữ lập trình | Python, SQL |
| Phân tích dữ liệu | Thư viện pandas, phân tích khám phá (EDA), thống kê mô tả |
| Cơ sở dữ liệu | SQLite, kết nối bảng quan hệ, đánh chỉ mục (index), tối ưu query plan |
| Chuẩn bị dữ liệu | Làm sạch dữ liệu, kiểm tra schema, chuẩn hóa dữ liệu, biến đổi định dạng |
| Phương pháp thống kê | Kiểm định giả thuyết, khoảng tin cậy, so sánh tỷ lệ chuyển đổi |
| Phân tích kinh doanh | Thiết lập KPI, phân tích doanh thu, phân tích phễu, phân khúc khách hàng |
| Đảm bảo chất lượng dữ liệu | Kiểm tra tính toàn vẹn, rà soát dữ liệu bất thường, đối soát chéo số học |
| Bảng tính Excel | Tổng hợp bằng công thức, kiểm tra tính toán lại, liên kết dữ liệu nguồn |
| Business Intelligence | Kiểm tra mô hình Power BI, chuẩn bị xác thực DAX, trích xuất dữ liệu Tableau Hyper |
| Báo cáo & Trực quan hóa | Báo cáo phân tích HTML, trích xuất CSV, tài liệu hóa kỹ thuật rõ ràng |
| Kiểm thử tự động | Thư viện Python unittest, kiểm tra tích hợp, CI/CD với GitHub Actions |
| Tính tái lập (Reproducibility) | Quản lý mã nguồn với Git/GitHub, cố định phiên bản thư viện, tạo mã băm SHA-256 |

### Kỹ Năng SQL Nòng Cốt

- Lọc dữ liệu, sắp xếp và gom nhóm tổng hợp (`WHERE`, `ORDER BY`, `GROUP BY`, `HAVING`).
- Thành thạo các phép kết nối: `INNER JOIN`, `LEFT JOIN`.
- Bảng tạm dùng chung: Common Table Expressions (CTE).
- Hàm cửa sổ và xếp hạng: `ROW_NUMBER()`, `COUNT(*) OVER()`, `SUM() OVER(PARTITION BY...)`.
- Xử lý chuỗi thời gian và ngày tháng.
- Tính toán tỷ lệ chuyển đổi, tỷ lệ rời bỏ và các chỉ số đo lường kinh doanh.
- Xử lý giá trị NULL và phòng tránh lỗi chia cho 0 (`NULLIF`, `COALESCE`).
- Kiểm tra tính toàn vẹn khóa chính và quan hệ dữ liệu.
- Phân tích kế hoạch thực thi truy vấn (`EXPLAIN QUERY PLAN`).

Toàn bộ các câu truy vấn SQL trong portfolio đều tương thích hoàn toàn với chuẩn SQLite 3.25+.

### Kỹ Năng Python Nòng Cốt

- Đọc, chuẩn hóa và xác thực dữ liệu từ các tệp CSV.
- Làm sạch và biến đổi dữ liệu có cấu trúc bằng `pandas`.
- Tái lập và kiểm tra độc lập các kết quả tính từ câu lệnh SQL.
- Tính toán các chỉ số thống kê mô tả và thống kê suy diễn.
- Tự động hóa quá trình xuất báo cáo phân tích HTML và CSV.
- Xây dựng pipeline dữ liệu có khả năng tái lập hoàn toàn.
- Chẩn đoán chất lượng dữ liệu và phát hiện điểm bất thường.
- Thiết lập hệ thống kiểm thử tự động với `unittest`.

---

## 🔄 Quy Trình Phân Tích Dữ Liệu Thực Tế

Mỗi dự án đều tuân thủ một quy trình phân tích chuẩn mực, rõ ràng và có thể lặp lại:

**01 — Xác định bài toán kinh doanh**  
Làm rõ quyết định cần hỗ trợ, các câu hỏi phân tích cốt lõi, hệ thống chỉ số KPI cần đo lường và các giới hạn ảnh hưởng đến việc diễn giải dữ liệu.

↓

**02 — Khảo sát & Đánh giá dữ liệu nguồn**  
Rà soát cấu trúc bảng (schema), số lượng dòng, các trường bắt buộc, khóa chính, kiểu dữ liệu, quan hệ giữa các bảng và các hạn chế đã biết.

↓

**03 — Làm sạch & Chuẩn hóa dữ liệu**  
Thực hiện các bước chuẩn hóa kiểu dữ liệu và làm sạch theo quy ước mà không làm thay đổi các tệp dữ liệu gốc ban đầu.

↓

**04 — Thực thi phân tích bằng SQL**  
Nạp dữ liệu đã làm sạch vào SQLite, chạy các truy vấn phân tích được đặt tên cụ thể và xuất kết quả ra các tệp CSV.

↓

**05 — Đối soát độc lập bằng Python**  
Tính toán lại các chỉ số chính bằng Python, kiểm tra ràng buộc quan hệ và đối chiếu kết quả để đảm bảo không có sai lệch logic.

↓

**06 — Diễn giải kết quả kinh doanh**  
Đánh giá ý nghĩa số liệu dưới góc nhìn kinh doanh, xem xét độ tin cậy thống kê, chất lượng dữ liệu và các cách giải thích đa chiều.

↓

**07 — Tạo báo cáo & Lưu trữ bằng chứng**  
Xuất tệp CSV kết quả, tạo báo cáo phân tích HTML, lưu hồ sơ kiểm tra xác thực và ghi nhận mã băm SHA-256.

↓

**08 — Đưa ra khuyến nghị hành động**  
Chuyển hóa kết quả thành các khuyến nghị thực tế, phân biệt rõ giữa bằng chứng đã chứng minh và các giả thuyết cần thử nghiệm thêm.

### Kiến Trúc Pipeline Dữ Liệu

**CSV thô → Ràng buộc hợp đồng dữ liệu → Làm sạch & Biến đổi → SQLite → Truy vấn SQL → Đối soát Python → Kết quả & Báo cáo → Bằng chứng kiểm định**

Toàn bộ quy trình này chạy hoàn toàn trên máy tính cá nhân, không yêu cầu dịch vụ đám mây trả phí hay cài đặt máy chủ cơ sở dữ liệu phức tạp.

---

## ✅ Kiểm Thử & Đảm Bảo Chất Lượng Dữ Liệu

Phân tích đáng tin cậy đòi hỏi nhiều hơn việc câu lệnh SQL chạy không báo lỗi. Portfolio này áp dụng một khung kiểm thử có cấu trúc để mọi kết quả đều có thể truy vết, tái lập và phản biện một cách minh bạch.

### Khung Kiểm Thử & Xác Thực

| Khía cạnh xác thực | Cách thức triển khai |
|---|---|
| Tính toàn vẹn cấu trúc (Schema) | Kiểm tra sự hiện diện của các cột bắt buộc và đúng kiểu dữ liệu |
| Giá trị bị khuyết | Kiểm tra các trường dữ liệu bắt buộc không được để trống |
| Tính toàn vẹn khóa chính | Phát hiện và chặn các dòng trùng lặp khóa chính |
| Tính toàn vẹn quan hệ (Referential) | Kiểm tra liên kết bảng và phát hiện các bản ghi mồ côi (orphan records) |
| Chất lượng dữ liệu | Chẩn đoán các dòng trùng lặp, logic ngày tháng và điểm bất thường |
| Đối soát chỉ số | So sánh chéo trực tiếp kết quả giữa SQL và tính toán trong Python |
| Tính chuẩn xác thống kê | Kiểm tra công thức khoảng tin cậy và các điều kiện biên của phép thử |
| Tính tuần tự thời gian | Kiểm tra trình tự xảy ra sự kiện và tính hợp lệ của bước chuyển đổi |
| Kiểm tra thực thi truy vấn | Đảm bảo mọi truy vấn SQL đều chạy thành công và sinh dữ liệu kết quả |
| Khả năng truy vết nguồn gốc | Lưu trữ mã băm SHA-256 của từng tệp trong manifest |
| Kiểm thử hồi quy | Lưu trữ kết quả số học và tự động phát hiện sai lệch khi cập nhật |

### Mức Độ Bao Phủ Của Kiểm Thử

- **93 bước kiểm tra runtime** chạy xuyên suốt qua 5 dự án.
- **48 bài kiểm thử tự động** bao phủ các trường hợp biên của thống kê, hợp đồng dữ liệu, quan hệ bảng, tính tuần tự thời gian, tính toán SQL và tính nhất quán của bằng chứng.
- Tự động hóa kiểm thử trên GitHub Actions mỗi khi cập nhật mã nguồn.
- Đối soát chéo từng chỉ số bằng thư viện pandas độc lập.
- Tệp manifest cập nhật mã băm SHA-256 để liên kết chính xác giữa dữ liệu đầu vào, mã phân tích và kết quả đầu ra.

---

## 📊 Đối Soát Business Intelligence & Sổ Làm Việc Gốc

Repository này lưu trữ các sổ làm việc BI cũ, các bảng tổng hợp Excel và một gói tài liệu kiểm tra xác thực tệp gốc chuyên biệt.

Quá trình kiểm tra phân định rành mạch giữa việc đọc cấu trúc tệp, kiểm thử số học, tính toán lại công thức và việc kiểm tra nghiệm thu trên phần mềm Desktop gốc.

### Ma Trận Xác Thực Tài Sản BI

| Tài sản | Bằng chứng được xác thực | Giới hạn cần lưu ý |
|---|---|---|
| 5 bảng tổng hợp Excel | Đã đính chính công thức, khớp dữ liệu chuẩn và có bằng chứng tính toán lại | Không khẳng định việc thực thi trên ứng dụng Microsoft Excel bản quyền |
| 3 tệp Tableau Hyper | 18 bảng dữ liệu nguồn/kết quả đã được đọc lại qua Hyper API | Chưa chạy làm mới giao diện trên Tableau Desktop |
| 2 mô hình Power BI cũ | 19 giá trị baseline tính độc lập và truy vấn kiểm tra DAX Query View | Chưa thực thi tính toán DAX trực tiếp trên Power BI Desktop |
| 5 dashboard BI cũ | Đã rà soát dữ liệu nhúng bên trong | Dữ liệu nhúng khác với tập dữ liệu phân tích chuẩn của dự án |
| Báo cáo chuẩn | Kết quả SQL/Python và báo cáo HTML trực quan offline | Độc lập với giao diện hình ảnh của dashboard cũ |

### Ý Nghĩa Của Việc Đối Soát

Một phát hiện quan trọng khi rà soát các tệp dashboard Power BI và Tableau cũ là chúng sử dụng tập dữ liệu khác với dữ liệu chuẩn của dự án phân tích.

Thay vì lấy các ảnh chụp màn hình dashboard không khớp số liệu để làm bằng chứng, mình đã giữ nguyên các tài sản gốc này và ghi chép rõ ràng sự khác biệt dữ liệu của chúng trong tài liệu đối soát.

**Khám phá bằng chứng kiểm định:**

[📘 Báo cáo xác thực sổ làm việc gốc](verification/native/README.md) | [🔎 Chi tiết rà soát Workbooks](verification/native/workbook_audit.json) | [📊 Bằng chứng tính lại công thức Excel](verification/native/excel_calc_verification.json)

---

## 💻 Cách Chạy Lại Dự Án Trên Máy Của Bạn

### Yêu Cầu Hệ Thống

- Python 3.12 trở lên.
- Git.
- Hệ điều hành tương thích: Windows, macOS hoặc Linux.
- Không cần tài khoản trả phí BI, đám mây hay máy chủ cơ sở dữ liệu ngoài để chạy phân tích cốt lõi.

### Bước 1 — Sao Chép Kho Lưu Trữ (Clone Repository)

```bash
git clone https://github.com/buinhatphong/digital-product-analytics-portfolio.git
cd data-analyst-portfolio
```

### Bước 2 — Tạo Môi Trường Ảo (Virtual Environment)

```bash
python -m venv .venv
```

Kích hoạt trên macOS/Linux:
```bash
source .venv/bin/activate
```

Kích hoạt trên Windows PowerShell:
```powershell
.venv\Scripts\Activate.ps1
```

### Bước 3 — Cài Đặt Thư Viện Cần Thiết

```bash
python -m pip install -r requirements.txt
```

### Bước 4 — Thực Thi Toàn Bộ 5 Dự Án

```bash
python -m portfolio.run
```

Lệnh này sẽ tự động làm sạch dữ liệu, tạo database SQLite cục bộ, chạy toàn bộ truy vấn SQL, đối soát Python, lưu kết quả CSV và tạo báo cáo HTML.

### Bước 5 — Chạy Toàn Bộ Các Bài Kiểm Thử Tự Động

```bash
python -m unittest discover -s tests -v
```

### Bước 6 — Chạy Riêng Lẻ Một Dự Án

Ví dụ, nếu bạn chỉ muốn chạy riêng dự án A/B Testing:

```bash
python -m portfolio.run --project 02_AB_Test_Feature_Impact
```

### Bước 7 — Xem Báo Cáo Phân Tích

Mở tệp `index.html` trực tiếp trên trình duyệt của bạn để duyệt qua danh mục báo cáo của 5 dự án, hoặc mở trực tiếp tệp `REPORT.html` trong từng thư mục dự án tương ứng.

Để biết thêm hướng dẫn xử lý sự cố chi tiết, bạn có thể xem thêm [Hướng dẫn chạy lại (Runbook)](docs/RUNBOOK.md).

---

## 📂 Cấu Trúc Thư Mục Kho Lưu Trữ

| Thư mục / Tệp tin | Vai trò & Nội dung |
|---|---|
| `01_SaaS_Product_Analytics_StreamFlow/` | Kích hoạt người dùng SaaS, doanh thu thuê bao và phễu onboarding |
| `02_AB_Test_Feature_Impact/` | Thử nghiệm A/B và suy diễn thống kê |
| `03_Ecommerce_Product_Analytics/` | Phễu TMĐT và phân tích đóng góp doanh thu theo sản phẩm |
| `04_Amazon_Marketplace_Analytics/` | Chất lượng doanh thu sàn marketplace và hiệu quả người bán |
| `05_User_Journey_Analytics/` | Hành trình khách hàng theo trình tự và chẩn đoán chất lượng sự kiện |
| `portfolio/` | Các module Python dùng chung: làm sạch, SQL, thống kê, kiểm tra và xuất báo cáo |
| `tests/` | Các bài kiểm thử tự động unit test và integration test |
| `docs/` | Tài liệu phương pháp luận, hướng dẫn chạy lại và cẩm nang phỏng vấn |
| `verification/native/` | Tài liệu và kết quả đối soát các tệp BI và bảng tính gốc |
| `scripts/` | Các công cụ tiện ích hỗ trợ xác thực và kiểm tra liên kết |
| `requirements.txt` | Danh sách thư viện Python và phiên bản tương ứng |
| `index.html` | Trang điều hướng báo cáo ngoại tuyến |
| `README.md` | Tài liệu tổng quan chính của portfolio |

---

## 🧠 Tư Duy Phân Tích & Ra Quyết Định Kinh Doanh

Một mục tiêu trọng tâm của portfolio này là thể hiện năng lực nhận diện các trường hợp số liệu trông có vẻ bình thường nhưng thực chất lại tiềm ẩn rủi ro hoặc thiếu căn cứ.

| Thách thức phân tích | Quyết định xử lý | Giá trị mang lại cho doanh nghiệp |
|---|---|---|
| Thiếu mã định danh khách hàng cố định | Không tự ý phân tích RFM thiếu căn cứ | Tránh việc phân khúc khách hàng sai lệch |
| Doanh thu không khớp phép tính giá × số lượng | Báo cáo rõ chênh lệch thay vì tự bịa công thức chiết khấu | Bảo vệ tính toàn vẹn của báo cáo tài chính |
| Sự kiện khách hàng bị đảo lộn thời gian | Tách bạch giữa tỷ lệ tiếp cận và phễu tuần tự nghiêm ngặt | Tránh hiểu nhầm lỗi kỹ thuật thành khách hàng bỏ cuộc |
| Thiếu thông tin phân bổ ngẫu nhiên A/B test | Nêu rõ các giả định khi báo cáo kết quả thống kê | Tránh vội vã kết luận ra mắt tính năng |
| Dữ liệu dashboard cũ bị lệch nguồn | Giữ nguyên tài sản cũ và ghi nhận rõ sự khác biệt | Tránh đưa ra hình ảnh minh họa thiếu căn cứ |
| Dòng trùng lặp không có mã sự kiện cố định | Giữ nguyên và định lượng số lượng dòng lặp | Tránh xóa nhầm các hành động hợp lệ của người dùng |
| Các dự phóng kinh doanh thiếu cơ sở | Tập trung vào kết quả đo lường và đề xuất kiểm chứng thêm | Giữ vững nguyên tắc báo cáo dựa trên bằng chứng |

**Nguyên tắc cốt lõi:** Một nhận định phân tích trung thực về giới hạn của dữ liệu luôn có giá trị hơn một kết luận kinh doanh thiếu căn cứ.

---

## 🎯 Ứng Dụng Vào Công Việc Thực Tế Của Data Analyst

Các dự án trong portfolio phản ánh những kỹ năng thực tế được ứng dụng rộng rãi trong doanh nghiệp:

- **Product Analytics (Phân tích sản phẩm):** Đo lường hành vi người dùng, tối ưu onboarding, theo dõi chỉ số kích hoạt, phân tích churn và đánh giá thử nghiệm tính năng.
- **Business Intelligence & Reporting:** Xây dựng định nghĩa KPI chuẩn, đối soát dữ liệu, chuẩn bị dữ liệu cho báo cáo và kiểm tra tính nhất quán của số đo.
- **Phân tích Doanh thu & Vận hành:** Rà soát chênh lệch tài chính, theo dõi hiệu suất kinh doanh, đánh giá mức độ tập trung doanh thu và cảnh báo rủi ro số liệu.
- **Marketing & Ecommerce Analytics:** Đo lường tỷ lệ chuyển đổi, phân khúc khách hàng theo kênh, đánh giá điểm nghẽn thanh toán và phân tích hiệu quả chiến dịch.
- **Data Quality & Hỗ trợ Analytics Engineering:** Xác thực dữ liệu đầu vào, đảm bảo tính minh bạch của quy trình biến đổi dữ liệu, kiểm thử định nghĩa chỉ số và xây dựng quy trình phân tích tự động.

---

## 📚 Tài Liệu Kỹ Thuật & Hướng Dẫn Kèm Theo

| Tài liệu | Nội dung chi tiết |
|---|---|
| [Phương pháp luận & Giới hạn](docs/METHODOLOGY.md) | Các giả định dữ liệu, giải thích thống kê, hợp đồng dữ liệu và phạm vi phân tích |
| [Hướng dẫn chạy lại (Runbook)](docs/RUNBOOK.md) | Hướng dẫn thiết lập môi trường, chạy dự án, xử lý lỗi và mô tả kết quả đầu ra |
| [Cẩm nang trao đổi phỏng vấn](docs/INTERVIEW_GUIDE.md) | Diễn giải chi tiết từng dự án và định hướng trả lời câu hỏi chuyên môn |
| [Ghi chú nâng cấp](docs/UPGRADE_NOTES.md) | Lịch sử cải tiến và hoàn thiện các tính năng của portfolio |
| [Xác thực sổ làm việc gốc](verification/native/README.md) | Bằng chứng kiểm tra Excel, Tableau, Power BI và các bước kiểm tra tiếp theo |
| [Trang chủ báo cáo](index.html) | Điểm truy cập trực tiếp vào các báo cáo phân tích ngoại tuyến |

---

## 🔎 Giới Hạn Cần Lưu Ý Của Dự Án

Để đảm bảo tính minh bạch và khách quan:

1. Toàn bộ 5 dự án đều dùng dữ liệu mô phỏng, không phải dữ liệu thực tế của khách hàng hay hệ thống production.
2. Đơn vị tiền tệ không được quy định cụ thể, hiển thị theo đơn vị số trong tập dữ liệu.
3. Mối tương quan trong dữ liệu quan sát không khẳng định mối quan hệ nhân quả.
4. Thử nghiệm A/B dựa trên các giả định về tính độc lập và phân bổ ngẫu nhiên chưa được xác minh đầy đủ từ metadata nguồn.
5. Sự cố đảo lộn thứ tự thời gian trong hành trình người dùng giới hạn việc kết luận về hành vi từ bỏ thực tế của khách hàng.
6. Các tệp dashboard BI cũ và dữ liệu phân tích chuẩn hiện tại không dùng chung một tập dữ liệu nguồn.
7. Quá trình kiểm tra tự động bằng code độc lập với việc kết xuất hình ảnh trực tiếp trên Power BI Desktop hay Tableau Desktop.

---

## 🤝 Kết Nối Với Mình

Mình luôn sẵn sàng tìm kiếm cơ hội làm việc trong lĩnh vực phân tích dữ liệu, nơi mình có thể vận dụng SQL, Python, phân tích kinh doanh và trực quan hóa dữ liệu để giúp doanh nghiệp thấu hiểu khách hàng và tối ưu hóa vận hành.

Các vị trí công việc mình quan tâm:

**Data Analyst • Junior Data Analyst • Business Intelligence Analyst • Reporting Analyst • Operations Data Analyst**

Mình luôn đề cao sự chuẩn xác của dữ liệu, tinh thần học hỏi không ngừng, tư duy giải quyết vấn đề thực tế và khả năng truyền đạt rõ ràng giữa kỹ thuật và kinh doanh.

📧 **Email:** [buinhatphong.analytics@gmail.com](mailto:buinhatphong.analytics@gmail.com)  
💼 **LinkedIn:** [linkedin.com/in/buinhatphong](https://www.linkedin.com/in/buinhatphong/)  
💻 **GitHub:** [github.com/buinhatphong](https://github.com/buinhatphong)

---

### 📌 Lời Kết

**Năm dự án. Quy trình phân tích SQL và Python có khả năng tái lập hoàn toàn. Kiểm thử kỹ thuật minh bạch. Trả lời đúng trọng tâm câu hỏi kinh doanh bằng các khuyến nghị dựa trên bằng chứng.**

Portfolio này được xây dựng không chỉ để thể hiện cách tính toán các chỉ số, mà còn phản ánh năng lực kiểm chứng, giải thích và sử dụng dữ liệu một cách có trách nhiệm.

**Được xây dựng và duy trì bởi Bùi Nhất Phong.**

## Bản quyền và tài liệu liên quan

Xem [LICENSE](LICENSE) để biết thông tin chi tiết về giấy phép mã nguồn mở. Các đoạn mã, tập dữ liệu và hình ảnh bên thứ ba vẫn giữ nguyên các điều khoản bản quyền tương ứng.

## Hướng dẫn cho người đánh giá & Nguồn gốc tài sản

Để điều hướng các bằng chứng kiểm định của dự án và danh mục rà soát quyền tài sản, vui lòng xem [REVIEWER_GUIDE.md](REVIEWER_GUIDE.md).

## Nâng cấp kiểm định thống kê A/B

Module `portfolio/metrics.py` kiểm tra chặt chẽ số lượng phiên và số lượt chuyển đổi ở từng nhóm là số nguyên hợp lệ. Khoảng tin cậy Wilson sẽ từ chối các mức độ tin cậy không hợp lệ. Đối với các thử nghiệm không phân bổ 50:50 (ví dụ 70:30), bạn có thể truyền tỷ lệ phân bổ dự kiến bằng cú pháp `experiment(..., expected_treatment_share=0.3)` và theo dõi chỉ số `srm_p_value_expected_allocation`. Giá trị kiểm tra mặc định `srm_p_value_50_50` vẫn được giữ nguyên để phục vụ chẩn đoán riêng.

Toàn bộ [kiểm thử hồi quy thống kê](tests/test_metrics.py) và kiểm tra tính toàn vẹn manifest đều được chạy tự động trong [quy trình xác thực](.github/workflows/validate.yml).

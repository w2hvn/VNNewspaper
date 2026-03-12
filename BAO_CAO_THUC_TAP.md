# BÁO CÁO THỰC TẬP TỐT NGHIỆP NGÀNH CÔNG NGHỆ THÔNG TIN

---

## MỞ ĐẦU

### TRANG BÌA
**TRƯỜNG ĐẠI HỌC CỬU LONG**
**KHOA CÔNG NGHỆ THÔNG TIN**

**BÁO CÁO THỰC TẬP TỐT NGHIỆP**
**Đề tài:** THU THẬP DỮ LIỆU TIN TỨC BẰNG PYTHON

**Giảng viên hướng dẫn:** [Tên giảng viên hướng dẫn]
**Sinh viên thực hiện:** [Tên sinh viên]
**Mã số sinh viên:** [Mã số sinh viên]
**Lớp:** [Tên lớp]

**Vĩnh Long, Năm [Năm]**

### LỜI CẢM ƠN
Lời đầu tiên, em xin gửi lời cảm ơn chân thành và sâu sắc nhất đến Ban Giám hiệu, Quý Thầy Cô Khoa Công nghệ Thông tin - Trường Đại học Cửu Long đã tận tâm truyền đạt những kiến thức quý báu trong suốt thời gian em học tập tại trường.
Đặc biệt, em xin gửi lời cảm ơn đến Thầy/Cô [Tên giảng viên hướng dẫn], người đã trực tiếp hướng dẫn, định hướng và hỗ trợ tận tình để em có thể hoàn thành tốt đợt thực tập và cuốn báo cáo này.
Cuối cùng, em xin cảm ơn gia đình, bạn bè và đơn vị thực tập [Tên đơn vị thực tập] đã luôn động viên, tạo điều kiện thuận lợi nhất cho em trong suốt quá trình nghiên cứu và thực hiện đề tài.
Do kiến thức và kinh nghiệm thực tế còn hạn chế, báo cáo chắc chắn không tránh khỏi những thiếu sót. Em rất mong nhận được những ý kiến đóng góp quý báu từ Quý Thầy Cô để đề tài được hoàn thiện hơn.

### TÓM TẮT
Báo cáo thực tập trình bày quá trình nghiên cứu, thiết kế và phát triển ứng dụng "Thu thập dữ liệu tin tức bằng Python". Hệ thống được xây dựng trên nền tảng ngôn ngữ Python (phiên bản 3.10+), kết hợp với thư viện BeautifulSoup4 để bóc tách dữ liệu HTML, Requests để giao tiếp HTTP, cơ sở dữ liệu SQLite để lưu trữ, và giao diện web hiện đại thông qua thư viện Streamlit. Đề tài tập trung giải quyết bài toán tự động hóa việc thu thập lượng lớn dữ liệu bài viết (tiêu đề, tóm tắt, nội dung) từ các trang báo mạng điện tử lớn tại Việt Nam (VNExpress, VietNamNet), hỗ trợ đa dạng phương thức (theo URL, chuyên mục, tìm kiếm từ khóa) kết hợp cơ chế xử lý đa luồng (MultiThreading) giúp tối ưu hóa hiệu năng. Qua đó, ứng dụng cung cấp một giải pháp trực quan giúp người dùng dễ dàng thu thập, quản lý và trích xuất báo cáo dưới định dạng Excel, phục vụ cho các mục đích phân tích dữ liệu và nghiên cứu chuyên sâu.

### DANH MỤC HÌNH ẢNH
- Hình 1: Kiến trúc tổng thể của hệ thống.
- Hình 2: Lược đồ Usecase tổng quát.
- Hình 3: Giao diện chính của ứng dụng trên Streamlit.
- Hình 4: Giao diện chức năng xuất báo cáo.
- Hình 5: Cấu trúc cơ sở dữ liệu SQLite (ERD).

### DANH MỤC BẢNG
- Bảng 1: Phân tích các yêu cầu chức năng của hệ thống.
- Bảng 2: Cấu trúc bảng `articles` trong cơ sở dữ liệu.
- Bảng 3: So sánh hiệu năng giữa phương pháp tuần tự và đa luồng.

### DANH MỤC TỪ VIẾT TẮT
- **CSDL:** Cơ sở dữ liệu.
- **UI:** User Interface (Giao diện người dùng).
- **URL:** Uniform Resource Locator (Trình định vị tài nguyên thống nhất).
- **HTML:** HyperText Markup Language (Ngôn ngữ đánh dấu siêu văn bản).
- **CLI:** Command Line Interface (Giao diện dòng lệnh).

### MỤC LỤC
[Tự động cập nhật dựa trên trình soạn thảo văn bản]

---

# CHƯƠNG 1: GIỚI THIỆU

## 1.1 Giới thiệu đề tài
Trong kỷ nguyên số hóa hiện nay, khối lượng thông tin trên Internet, đặc biệt là tin tức trực tuyến, đang gia tăng theo cấp số nhân. Việc theo dõi, tổng hợp và phân tích thông tin từ nhiều nguồn báo chí điện tử khác nhau một cách thủ công đòi hỏi nguồn nhân lực lớn và tốn rất nhiều thời gian. Nhu cầu về các công cụ khai thác dữ liệu web (web scraping) tự động đang trở nên cấp thiết để phục vụ cho các mục đích như nghiên cứu thị trường, theo dõi truyền thông, phân tích ngôn ngữ tự nhiên (NLP) hay xây dựng các hệ thống khuyến nghị. Nhận thức được tầm quan trọng này, đề tài "Thu thập dữ liệu tin tức bằng Python" được thực hiện nhằm xây dựng một phần mềm tự động hóa quá trình thu thập, phân loại và lưu trữ nội dung tin tức, giúp tiết kiệm thời gian và cung cấp nguồn dữ liệu thô chất lượng cho các khâu xử lý tiếp theo.

## 1.2 Mục tiêu đề tài
Mục tiêu cốt lõi của đề tài là nghiên cứu và xây dựng một phần mềm thu thập tin tức tự động hoạt động đa luồng (MultiThreading) đảm bảo hiệu năng cao.
Phương pháp nghiên cứu: Tiến hành phân tích cấu trúc DOM (Document Object Model) của các trang báo mạng điện tử phổ biến tại Việt Nam; vận dụng kỹ thuật hướng đối tượng (OOP) và mẫu thiết kế Factory (Factory Pattern) để xây dựng hệ thống lõi Crawler có tính mở rộng cao. Xây dựng giao diện tương tác trên nền tảng Web thông qua thư viện Streamlit nhằm tối ưu hóa trải nghiệm người dùng.

## 1.3 Nội dung đề tài
Đề tài tiến hành xây dựng một hệ thống hoàn chỉnh với các thành phần chính:
- Modul cốt lõi (Core Crawler): Thu thập bài viết từ VNExpress và VietNamNet dựa trên URL cụ thể, theo chuyên mục hoặc thông qua tính năng tìm kiếm theo từ khóa. Sử dụng cơ chế ThreadPoolExecutor để tăng tốc độ lấy dữ liệu.
- Modul lưu trữ: Thiết kế cơ sở dữ liệu SQLite để lưu trữ thông tin bài viết (tiêu đề, tóm tắt, nội dung, ngày cào, nguồn báo), đồng thời xử lý loại bỏ các bản ghi trùng lặp.
- Modul giao diện và báo cáo: Xây dựng Dashboard bằng Streamlit để cấu hình luồng chạy, hiển thị dữ liệu trực quan bằng biểu đồ và cho phép trích xuất báo cáo ra file Excel (.xlsx).

## 1.4 Giới hạn đề tài
- Hệ thống tập trung bóc tách dữ liệu văn bản (text) bao gồm tiêu đề, mô tả và nội dung đoạn văn. Các nội dung đa phương tiện như video, audio chưa được hỗ trợ.
- Hệ thống hiện tại chỉ được tinh chỉnh để tương thích với cấu trúc HTML của 2 trang báo điện tử: VNExpress và VietNamNet.
- Ứng dụng triển khai ở dạng Localhost hoặc triển khai nội bộ, chưa áp dụng các cơ chế phân tán (Distributed Scraping) hay vượt qua các hệ thống Captcha phức tạp.

## 1.5 Cấu trúc báo cáo
Báo cáo được cấu trúc thành 5 chương:
- Chương 1: Giới thiệu tổng quan về đề tài.
- Chương 2: Trình bày cơ sở lý thuyết, công nghệ sử dụng và các nghiên cứu liên quan.
- Chương 3: Phân tích, thiết kế hệ thống và giao diện phần mềm.
- Chương 4: Trình bày kết quả cài đặt, hiện thực hóa các chức năng và giao diện.
- Chương 5: Kết luận về kết quả đạt được và đề xuất hướng phát triển tương lai.

---

# CHƯƠNG 2: CƠ SỞ LÝ THUYẾT VÀ CÁC NGHIÊN CỨU LIÊN QUAN

## 2.1 Cơ sở lý thuyết
### 2.1.1 Ngôn ngữ Python và Thư viện
- **Python (3.10+):** Là ngôn ngữ lập trình bậc cao, dễ đọc, mạnh mẽ trong việc xử lý văn bản và tự động hóa.
- **BeautifulSoup4:** Một thư viện mạnh mẽ trong Python chuyên dùng để parse (phân tích) cú pháp các tài liệu HTML/XML, cho phép trích xuất dữ liệu một cách linh hoạt dựa trên cấu trúc DOM của trang web.
- **Requests:** Thư viện giúp gửi các HTTP/1.1 requests một cách đơn giản, dùng để tải mã nguồn trang web về hệ thống.
- **Pandas & Openpyxl:** Thư viện phục vụ cho việc xử lý cấu trúc dữ liệu dạng bảng (DataFrame) và xuất dữ liệu ra định dạng Excel phục vụ báo cáo.

### 2.1.2 Streamlit
Streamlit là một framework mã nguồn mở của Python chuyên dụng để xây dựng các ứng dụng web tương tác (Data Dashboard) một cách nhanh chóng mà không cần kiến thức chuyên sâu về Front-end (HTML/CSS/JS).

### 2.1.3 Lập trình Đa luồng (Multithreading)
Multithreading là kỹ thuật cho phép một chương trình chạy song song nhiều luồng thực thi trong cùng một tiến trình. Dự án sử dụng `concurrent.futures.ThreadPoolExecutor` để phân chia tác vụ gửi request và xử lý HTML cho nhiều công nhân (workers) cùng lúc, giúp rút ngắn đáng kể thời gian thu thập lượng lớn dữ liệu.

### 2.1.4 Cơ sở dữ liệu SQLite
SQLite là hệ quản trị cơ sở dữ liệu quan hệ nhỏ gọn, được tích hợp sẵn vào ngôn ngữ Python, không yêu cầu cấu hình server phức tạp, rất phù hợp cho các phần mềm thu thập dữ liệu cỡ nhỏ và vừa ở phạm vi cục bộ.

## 2.2 Các nghiên cứu liên quan
Trên thế giới và tại Việt Nam, bài toán Web Scraping đã có nhiều nghiên cứu và công cụ thương mại (như Octoparse, ParseHub) hỗ trợ. Tuy nhiên, các công cụ này thường có chi phí cao và hạn chế khả năng can thiệp sâu vào code. Trong môi trường học thuật, nhiều đồ án đã ứng dụng thư viện Scrapy hoặc Selenium. Khác với Selenium (nặng nề vì mô phỏng trình duyệt), dự án này lựa chọn Requests kết hợp BeautifulSoup kết hợp cơ chế Đa luồng nhằm tối ưu chi phí tài nguyên phần cứng trong khi vẫn đảm bảo được tốc độ cào dữ liệu tối đa.

---

# CHƯƠNG 3: PHÂN TÍCH VÀ THIẾT KẾ HỆ THỐNG

## 3.1 Yêu cầu hệ thống
- **Yêu cầu chức năng:**
  - Hệ thống cho phép chọn nguồn dữ liệu (VNExpress, VietNamNet).
  - Cho phép người dùng tùy chọn 1 trong 3 phương thức: Theo danh sách URL, Theo chuyên mục (Category), và Theo Từ khóa (Keyword).
  - Thiết lập số lượng luồng (workers) xử lý song song.
  - Tự động lưu trữ bài báo vào CSDL, loại bỏ trùng lặp (dựa trên URL).
  - Cung cấp tính năng xem trước dữ liệu và xuất báo cáo dưới dạng file Excel.
- **Yêu cầu phi chức năng:**
  - Giao diện trực quan, thân thiện, dễ sử dụng.
  - Hiệu suất ổn định, xử lý lỗi tốt (bỏ qua bài viết lỗi mà không dừng toàn bộ tiến trình).

## 3.2 Phân tích hệ thống
Sau khi tiếp nhận yêu cầu, hệ thống được thiết kế theo hướng module hóa (Modular Design). Lớp `BaseCrawler` định nghĩa các khuôn mẫu thu thập dữ liệu trừu tượng. Các lớp con `VNExpressCrawler` và `VietNamNetCrawler` kế thừa và cụ thể hóa các phương thức (method) bóc tách HTML đặc thù. Design Pattern Factory được áp dụng tại `get_crawler()` để khởi tạo đối tượng Crawler động dựa trên cấu hình do người dùng chọn trên giao diện.

## 3.3 Thiết kế phần mềm

### 3.3.1 Thiết kế CSDL (Database Design)
Hệ thống sử dụng duy nhất một bảng `articles` với cấu trúc sau:

[Chèn bảng: Bảng 2: Cấu trúc bảng articles]

- `id`: INTEGER (Khóa chính, tự động tăng).
- `url`: TEXT (UNIQUE, ngăn chặn dữ liệu trùng).
- `website`: TEXT (Tên nguồn báo).
- `category_or_keyword`: TEXT (Chuyên mục hoặc từ khóa tìm kiếm).
- `title`: TEXT (Tiêu đề bài báo).
- `description`: TEXT (Tóm tắt bài báo).
- `content`: TEXT (Nội dung chi tiết).
- `crawl_date`: TEXT (Thời gian thực hiện thu thập).

### 3.3.2 Lược đồ Use Case
Người dùng đóng vai trò là Actor duy nhất tương tác với phần mềm qua giao diện Web. Các Use Case chính bao gồm: Cấu hình thông số (Web, Workers); Khởi động thu thập dữ liệu; Xem thống kê và Xuất báo cáo.

[Chèn hình ảnh: Hình 2: Lược đồ Usecase tổng quát]

### 3.3.3 Lược đồ Lớp (Class Diagram)
[Chèn hình ảnh: Hình Lược đồ lớp (BaseCrawler, VNExpressCrawler, VietNamNetCrawler)]

## 3.4 Thiết kế giao diện
Giao diện được bố trí linh hoạt thông qua thành phần Sidebar và Tabs của Streamlit:
- **Sidebar:** Khu vực cố định để người dùng chọn nguồn báo và điều chỉnh số luồng (workers).
- **Tab 1 - Thu thập dữ liệu:** Form nhập liệu tương ứng với 3 lựa chọn (nhập danh sách text URL, chọn dropdown menu chuyên mục, nhập text từ khóa). Đi kèm là các thông báo spinner mô tả trạng thái tiến trình.
- **Tab 2 - Quản lý & Báo cáo:** Hiển thị dữ liệu dưới dạng DataFrame, vẽ các biểu đồ bar chart cơ bản thống kê bài viết theo nguồn/lĩnh vực và tích hợp nút Download Excel.

[Chèn hình ảnh: Hình Thiết kế giao diện Dashboard]

## 3.5 Yêu cầu phần cứng, phần mềm
- **Phần cứng:** CPU Core i3 hoặc tương đương, RAM tối thiểu 4GB, Dung lượng đĩa trống 500MB.
- **Phần mềm:** Hệ điều hành Windows 10/Linux/macOS, Python bản 3.10 trở lên, cài đặt đầy đủ các thư viện trong `requirements.txt`.

## 3.6 Sitemap / Liên kết giao diện
Hệ thống thiết kế theo mô hình Single Page Application (SPA) thông qua Streamlit, người dùng có thể di chuyển liền mạch giữa khu vực Thiết lập thu thập dữ liệu (Tab 1) và khu vực Xử lý, Báo cáo (Tab 2) trên cùng một trang màn hình duy nhất mà không bị gián đoạn.

---

# CHƯƠNG 4: HIỆN THỰC HỆ THỐNG

## 4.1 Hướng dẫn cài đặt
Sản phẩm được đóng gói mã nguồn và file yêu cầu, người dùng chỉ cần thiết lập môi trường Virtual Environment, cài đặt thư viện qua lệnh `pip install -r requirements.txt` và chạy file entry point với lệnh `streamlit run app.py`.

## 4.2 Hiện thực giao diện
Giao diện được viết hoàn toàn bằng Python thông qua Streamlit:
- Sử dụng `st.sidebar` để nhóm các tham số thiết lập kỹ thuật.
- Sử dụng `st.tabs` chia tách không gian làm việc.
- Sử dụng `st.dataframe` và `st.bar_chart` để trực quan hóa lượng dữ liệu từ SQLite sinh động. Các tín hiệu feedback như `st.spinner`, `st.success`, `st.warning` được sử dụng để tương tác thông báo trạng thái với người dùng.

[Chèn hình ảnh: Hình 3: Giao diện chính của ứng dụng trên Streamlit]

## 4.3 Hiện thực CSDL
File `database/db_manager.py` đảm nhận việc kết nối tới SQLite. Hàm `init_db()` được gọi lúc khởi chạy để đảm bảo bảng dữ liệu sẵn sàng. Sử dụng phương thức truy vấn có tham số (Parameterized Query) giúp bảo mật luồng dữ liệu truyền vào khỏi nguy cơ lỗi chuỗi hoặc tấn công SQL Injection. Hàm `save_article()` được bắt lỗi ngoại lệ `sqlite3.IntegrityError` khéo léo để lọc các bài viết đã có URL tồn tại trong hệ thống.

## 4.4 Hiện thực các báo cáo
Bằng cách truy vấn toàn bộ dữ liệu từ bảng `articles` đổ vào thư viện Pandas sinh ra đối tượng DataFrame. Đối tượng DataFrame này sau đó được sử dụng hàm `to_excel` cùng engine `openpyxl` ghi nội dung vào bộ nhớ ảo `io.BytesIO()`. File này sẽ được tải về trực tiếp từ trình duyệt khi người dùng nhấp vào nút Download do `st.download_button` tạo ra.

[Chèn hình ảnh: Hình 4: Giao diện chức năng xuất báo cáo]

## 4.5 Hiện thực code liên quan
Tại các file lõi như `crawler/vnexpress.py`, luồng trích xuất dữ liệu được hiện thực dựa trên việc gọi `requests.get()` để lấy HTML thuần. `BeautifulSoup` sử dụng các thẻ `class_` cụ thể ví dụ: thẻ tiêu đề thường là `h1` (title-detail), thẻ mô tả là `p` (description), các đoạn văn bản chính (paragraphs) là `p` (Normal). Logic lấy đa luồng danh sách phân trang được đóng gói trong hàm `get_urls_of_keyword_thread` kết hợp cùng `ThreadPoolExecutor` để duyệt nhanh dữ liệu các trang tìm kiếm.

---

# CHƯƠNG 5: KẾT LUẬN

## 5.1 Kết quả đạt được
Đề tài đã hoàn thành xuất sắc việc xây dựng phần mềm "Thu thập dữ liệu tin tức bằng Python". Hệ thống đã chuyển đổi thành công từ dạng mã nguồn mở chạy bằng lệnh CLI sang một ứng dụng giao diện Web hiện đại với Streamlit. Phần mềm hoạt động ổn định trong việc cào tin tức tự động dựa theo chuyên mục và từ khóa, phân tích chính xác mã nguồn HTML từ VNExpress và VietNamNet, lưu trữ bài bản vào CSDL SQLite và kết xuất báo cáo Excel theo đúng yêu cầu đã đặt ra.

## 5.2 Ưu và nhược điểm
- **Ưu điểm:** Hệ thống hoạt động nhanh nhờ kiến trúc đa luồng, loại bỏ triệt để vấn đề trùng lặp dữ liệu, kiến trúc lập trình tuân thủ nguyên tắc Clean Code dễ dàng bổ sung tính năng hoặc các trang báo mới (nhờ mô hình Factory). Giao diện Streamlit thân thiện.
- **Nhược điểm:** Phụ thuộc cứng vào cấu trúc thẻ HTML của các trang báo, nếu trang web thay đổi giao diện, bộ Crawler cần phải được cập nhật lại tương ứng. Hệ thống chưa mô phỏng người dùng bằng Headless Browser nên có thể gặp khó khăn nếu báo sử dụng nhiều kỹ thuật chặn cào dữ liệu qua Javascript Rendering mạnh.

## 5.3 Đóng góp của đồ án
Đồ án mang lại một công cụ hữu ích cho sinh viên, nhà nghiên cứu và phân tích dữ liệu cần tạo dựng nhanh một bộ dataset (tập dữ liệu) nội dung Tiếng Việt chất lượng. Đồng thời nó minh chứng cho việc kết hợp linh hoạt giữa kỹ thuật lập trình đa luồng (Threading), cơ sở dữ liệu quan hệ (SQLite) và các công nghệ phát triển giao diện Data App (Streamlit).

## 5.4 Hướng mở rộng tương lai
Trong tương lai, phần mềm có thể được nâng cấp với các tính năng:
- Bổ sung cấu hình Proxy chống bị chặn IP (IP Ban).
- Tích hợp thêm module Xử lý ngôn ngữ tự nhiên (NLP) trực tiếp trên giao diện để tự động phân tích cảm xúc (Sentiment Analysis) của bài báo.
- Mở rộng hỗ trợ cào nội dung bằng Selenium/Playwright để xử lý các trang web tải nội dung động bằng Javascript phức tạp.

---

# TÀI LIỆU THAM KHẢO
1. [Tác giả], *Tên tài liệu tham khảo 1 (Ví dụ: Python Documentation)*, Năm xuất bản.
2. [Tác giả], *Tài liệu hướng dẫn BeautifulSoup4*, Trực tuyến tại: https://www.crummy.com/software/BeautifulSoup/bs4/doc/, [Năm truy cập].
3. [Tác giả], *Tài liệu Streamlit API*, Trực tuyến tại: https://docs.streamlit.io/, [Năm truy cập].
4. [Tác giả], *Tài liệu Pandas Documentation*, Trực tuyến tại: https://pandas.pydata.org/docs/, [Năm truy cập].
5. [Tác giả], *Tài liệu lập trình đa luồng Concurrent Futures*, Trực tuyến: https://docs.python.org/3/library/concurrent.futures.html, [Năm truy cập].
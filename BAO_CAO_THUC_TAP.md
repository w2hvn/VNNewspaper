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

### TRANG BÌA LÓT
**TRƯỜNG ĐẠI HỌC CỬU LONG**
**KHOA CÔNG NGHỆ THÔNG TIN**

**BÁO CÁO THỰC TẬP TỐT NGHIỆP**
**Đề tài:** THU THẬP DỮ LIỆU TIN TỨC BẰNG PYTHON

**Cơ quan thực tập:** [Tên cơ quan/công ty thực tập]
**Người hướng dẫn tại cơ quan:** [Tên người hướng dẫn]
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
- Hình 1: Lược đồ Use Case tổng quát.
- Hình 2: Lược đồ Triển khai (Deployment Diagram).
- Hình 3: Lược đồ Trình tự (Sequence Diagram).
- Hình 4: Lược đồ Cộng tác (Collaboration Diagram).
- Hình 5: Lược đồ Trạng thái (State Diagram).
- Hình 6: Lược đồ Lớp (Class Diagram).
- Hình 7: Lược đồ Hoạt động (Activity Diagram).
- Hình 8: Giao diện tab Thu thập dữ liệu.
- Hình 9: Giao diện tab Quản lý và Báo cáo.

### DANH MỤC BẢNG
- Bảng 1: Bảng thu thập yêu cầu người dùng.
- Bảng 2: Cấu trúc cơ sở dữ liệu bảng `articles`.

### DANH MỤC TỪ VIẾT TẮT
- **CSDL:** Cơ sở dữ liệu.
- **UI:** User Interface (Giao diện người dùng).
- **URL:** Uniform Resource Locator (Trình định vị tài nguyên thống nhất).
- **HTML:** HyperText Markup Language (Ngôn ngữ đánh dấu siêu văn bản).
- **DOM:** Document Object Model (Mô hình Đối tượng Tài liệu).

### MỤC LỤC
[Tự động cập nhật dựa trên trình soạn thảo văn bản]

---

# CHƯƠNG 1: GIỚI THIỆU

## 1.1 Giới thiệu đề tài
Trong kỷ nguyên số hóa hiện nay, khối lượng thông tin trên Internet, đặc biệt là tin tức trực tuyến, đang gia tăng theo cấp số nhân. Việc theo dõi, tổng hợp và phân tích thông tin từ nhiều nguồn báo chí điện tử khác nhau một cách thủ công đòi hỏi nguồn nhân lực lớn và tốn rất nhiều thời gian. Nhu cầu về các công cụ khai thác dữ liệu web (web scraping) tự động đang trở nên cấp thiết. Nhận thức được tầm quan trọng này, đề tài "Thu thập dữ liệu tin tức bằng Python" được thực hiện nhằm xây dựng một phần mềm tự động hóa quá trình thu thập, phân loại và lưu trữ nội dung tin tức, giúp tiết kiệm thời gian và cung cấp nguồn dữ liệu thô chất lượng.

## 1.2 Mục tiêu đề tài
Mục tiêu cốt lõi của đề tài là nghiên cứu và xây dựng một phần mềm thu thập tin tức tự động hoạt động đa luồng (MultiThreading) với giao diện trực quan, dễ sử dụng. Hệ thống cho phép người dùng cấu hình linh hoạt việc trích xuất tin tức từ các tờ báo điện tử hàng đầu như VNExpress, VietNamNet, sau đó tự động xử lý và lưu trữ dữ liệu vào cơ sở dữ liệu cục bộ.

## 1.3 Nội dung đề tài
Đề tài tiến hành xây dựng một hệ thống phần mềm hoàn chỉnh bao gồm các thành phần chính:
- Hệ thống thu thập (Crawler): Bóc tách nội dung HTML (tiêu đề, tóm tắt, nội dung chính) bằng Python.
- Cơ sở dữ liệu: Thiết kế CSDL SQLite để lưu trữ, đảm bảo không trùng lặp (dựa trên URL).
- Giao diện và Báo cáo: Xây dựng Dashboard bằng Streamlit để quản lý các luồng cào dữ liệu, hiển thị biểu đồ thống kê và tính năng xuất file báo cáo định dạng Excel (.xlsx).

## 1.4 Giới hạn đề tài
- Hệ thống tập trung xử lý dữ liệu dạng văn bản (text), chưa hỗ trợ tải video, hình ảnh.
- Hiện tại mới chỉ hỗ trợ định dạng cấu trúc của 2 tờ báo điện tử: VNExpress và VietNamNet.
- Phần mềm chạy trên môi trường Web cục bộ (Localhost) và chưa tích hợp khả năng vượt qua các cơ chế chống cào dữ liệu nâng cao (như CAPTCHA, Cloudflare).

## 1.5 Cấu trúc báo cáo
Báo cáo được cấu trúc thành 5 chương:
- Chương 1: Giới thiệu tổng quan về đề tài.
- Chương 2: Cơ sở lý thuyết và các nghiên cứu liên quan.
- Chương 3: Phân tích và thiết kế hệ thống.
- Chương 4: Hiện thực hệ thống.
- Chương 5: Kết luận.

---

# CHƯƠNG 2: CƠ SỞ LÝ THUYẾT VÀ CÁC NGHIÊN CỨU LIÊN QUAN

## 2.1 Cơ sở lý thuyết
- **Python (3.10+):** Ngôn ngữ lập trình thông dịch phổ biến, mạnh mẽ cho xử lý dữ liệu và tự động hóa.
- **BeautifulSoup4 & Requests:** Các thư viện Python cốt lõi chuyên dụng cho việc gửi yêu cầu mạng (HTTP requests) và phân tích cấu trúc DOM để trích xuất thẻ HTML cần thiết.
- **Lập trình Đa luồng (Multithreading):** Việc sử dụng `concurrent.futures.ThreadPoolExecutor` cho phép xử lý song song các tác vụ tải trang web, tăng hiệu năng một cách rõ rệt.
- **SQLite:** Hệ quản trị CSDL quan hệ siêu nhẹ được tích hợp sẵn, giúp dễ dàng lưu trữ và truy vấn dữ liệu theo cấu trúc bảng.
- **Streamlit:** Framework Python hỗ trợ xây dựng giao diện Data Web App một cách nhanh chóng với các component UI phong phú như Tabs, Sidebar, DataFrame.

## 2.2 Các nghiên cứu liên quan (trong và ngoài nước)
Các nghiên cứu về thu thập dữ liệu tự động (Web Scraping) trên thế giới đã đạt được nhiều thành tựu lớn với các framework như Scrapy, Selenium, hay Puppeteer. Tại Việt Nam, sinh viên thường sử dụng Selenium trong các đồ án để tự động hóa trình duyệt. Tuy nhiên, điểm mạnh của dự án này so với việc dùng Selenium là sử dụng kết hợp Requests + BeautifulSoup + ThreadPool, tạo nên một crawler "nhẹ" (lightweight), tiêu tốn rất ít tài nguyên máy tính (RAM, CPU) mà mang lại tốc độ bóc tách nhanh gấp nhiều lần do không phải kết xuất (render) hình ảnh trang web.

---

# CHƯƠNG 3: PHÂN TÍCH VÀ THIẾT KẾ HỆ THỐNG

## 3.1 Yêu cầu hệ thống
- Người dùng có thể thao tác hoàn toàn qua giao diện web.
- Cho phép lựa chọn nguồn thu thập, số lượng tiến trình song song (workers).
- Cho phép lưu lại dữ liệu đã cào vào CSDL, xuất được ra file báo cáo Excel.

## 3.2 Phân tích hệ thống
### 3.2.1 Thu thập yêu cầu người dùng
- Yêu cầu chức năng:
  - Cần lấy được nội dung văn bản (title, description, content) từ bài viết.
  - Cần 3 tuỳ chọn thu thập: qua 1 list danh sách URL, qua chuyên mục (Kinh doanh, Thể thao,...) và qua Từ khóa tìm kiếm tự do.
- Yêu cầu phi chức năng:
  - Ứng dụng phải trực quan, dễ hiểu, thao tác trong dưới 3 cú click.
  - Phải hiển thị trạng thái đang xử lý để người dùng biết.

### 3.2.2 Phân tích yêu cầu người dùng
Dựa vào các yêu cầu trên, hệ thống cần có kiến trúc phân lớp: Lớp UI (Streamlit), Lớp Business Logic (Controller/Crawler đa luồng), và Lớp Database (SQLite db_manager). Lớp UI sẽ nhận cấu hình, đẩy xuống Business Logic xử lý, kết quả trả về sẽ được Lớp Database ghi nhận.

### 3.2.3 Yêu cầu phải đạt được khi thiết kế/ hiện thực web/phần mềm
Hệ thống web nội bộ (Local Web App) phải đáp ứng tốt việc chạy đa luồng mà không làm treo giao diện (UI blocking). CSDL phải đảm bảo tính toàn vẹn, URL bài viết là duy nhất (Unique) để ngăn việc thu thập một bài báo nhiều lần.

## 3.3 Thiết kế website/phần mềm

### 3.3.1 Thiết kế CSDL
Hệ thống sử dụng SQLite với 1 bảng duy nhất là `articles`.

[Chèn bảng: Bảng 2: Cấu trúc cơ sở dữ liệu bảng articles]
- `id`: Khóa chính (INTEGER AUTOINCREMENT).
- `url`: Địa chỉ trang báo (TEXT UNIQUE).
- `website`: Nguồn báo (VNExpress / VietNamNet).
- `category_or_keyword`: Phân loại.
- `title`: Tiêu đề bài viết.
- `description`: Tóm tắt mở đầu.
- `content`: Nội dung các đoạn văn bản.
- `crawl_date`: Ngày giờ hệ thống thực hiện crawl.

### 3.3.2 Thiết kế các usecase
Hệ thống có một Actor chính là Người dùng (User).
Các Usecase chính: Cấu hình thông số cài đặt; Cào dữ liệu theo URL; Cào dữ liệu theo chuyên mục; Cào dữ liệu theo từ khóa; Xem báo cáo CSDL; Xuất báo cáo Excel.

[Chèn hình ảnh: Hình 1: Lược đồ Use Case tổng quát]

### 3.3.3 Lược đồ triển khai
Lược đồ mô tả cách hệ thống cài đặt trên thiết bị cá nhân: Hệ điều hành (Host OS) chạy môi trường Python, thực thi Streamlit App trên cổng 8501, giao tiếp với CSDL SQLite được lưu ở dạng file vật lý `newspaper.db` trên ổ cứng.

[Chèn hình ảnh: Hình 2: Lược đồ Triển khai (Deployment Diagram)]

### 3.3.4 Lược đồ trình tự
Quá trình "Thu thập dữ liệu theo từ khóa": Người dùng nhập từ khóa -> Lớp UI (App) gọi Controller -> Controller khởi tạo `ThreadPoolExecutor` -> Các thread lấy danh sách URLs từ trang search -> Các thread tải chi tiết HTML từng bài -> Bóc tách dữ liệu -> Trả về kết quả và lưu vào Database.

[Chèn hình ảnh: Hình 3: Lược đồ Trình tự (Sequence Diagram)]

### 3.3.5 Lược đồ cộng tác
Mô tả sự tương tác qua lại thông điệp giữa các đối tượng UI, Factory Crawler, BaseCrawler và DBManager khi cùng thực hiện một tác vụ Crawl dữ liệu.

[Chèn hình ảnh: Hình 4: Lược đồ Cộng tác (Collaboration Diagram)]

### 3.3.6 Lược đồ trạng thái
Các trạng thái chính của hệ thống trong vòng đời thu thập dữ liệu: `IDLE` (Chờ thao tác) -> `CONFIGURING` (Đang cấu hình thông số) -> `CRAWLING` (Đang đa luồng lấy dữ liệu) -> `SAVING` (Ghi CSDL) -> `FINISHED` (Hiển thị kết quả thành công / Lỗi).

[Chèn hình ảnh: Hình 5: Lược đồ Trạng thái (State Diagram)]

### 3.3.7 Lược đồ lớp
Các lớp chính trong kiến trúc:
- `BaseCrawler`: Lớp cha định nghĩa abstract methods (`extract_content`, `get_urls_of_type_thread`, `get_urls_of_keyword_thread`).
- `VNExpressCrawler`, `VietNamNetCrawler`: Các lớp kế thừa triển khai chi tiết phương thức bóc tách HTML.
- `Factory`: Lớp sinh đối tượng tự động.

[Chèn hình ảnh: Hình 6: Lược đồ Lớp (Class Diagram)]

### 3.3.8 Lược đồ hoạt động
Miêu tả logic nhánh của hàm `write_content`: Bắt đầu -> Request HTML -> Tìm thẻ `title` -> Nếu rỗng (Bài lỗi/Video) thì return False -> Bóc tách `description`, `content` -> Gọi hàm `save_to_db` -> Kết thúc chu trình bài viết.

[Chèn hình ảnh: Hình 7: Lược đồ Hoạt động (Activity Diagram)]

## 3.4 Thiết kế giao diện
Ứng dụng Web Dashboard được thiết kế theo dạng sidebar điều hướng tĩnh.
- Màn hình chính phân mảnh bằng 2 Tabs.
- Tab 1: Layout chia các Radio Button để chọn phương thức, cùng các input text, slider rõ ràng.
- Tab 2: Hiển thị một DataFrame bao quát toàn bộ CSDL và các biểu đồ cột (Bar Chart) mô tả trực quan tỷ lệ dữ liệu của các trang báo.

## 3.5 Yêu cầu phần cứng, phần mềm
- **Phần cứng:** CPU Intel Core i3 / AMD Ryzen 3 trở lên, RAM 4GB (Khuyến nghị 8GB để chạy đa luồng ổn định), 500MB ổ cứng.
- **Phần mềm:** Môi trường Python 3.10 trở lên, cài đặt các module trong `requirements.txt` (Streamlit, BeautifulSoup4, Pandas, v.v.).

## 3.6 Sitemap (nếu là website)/ Liên kết giao diện (nếu là phần mềm)
Do phần mềm sử dụng Streamlit dưới dạng Single-Page Application (SPA) với Tab layout:
- `Trang chủ (localhost:8501)`
  - `Sidebar` (Cấu hình)
  - `Tab 1` (Chức năng Crawl)
  - `Tab 2` (Chức năng Thống kê & Báo cáo)

---

# CHƯƠNG 4: HIỆN THỰC HỆ THỐNG

## 4.1 Hướng dẫn cài đặt
Sản phẩm là một dự án Python chuẩn mực.
Bước 1: Cài đặt thư viện: `pip install -r requirements.txt`
Bước 2: Khởi chạy phần mềm giao diện web bằng lệnh Terminal: `streamlit run app.py`

## 4.2 Hiện thực giao diện
Giao diện ứng dụng được hiện thực thông qua các hàm có sẵn của thư viện Streamlit. Các thông báo spinner giúp giao diện trực quan hơn khi các ThreadPool đang chạy ngầm phía sau mà không làm đơ trình duyệt của người dùng.

[Chèn hình ảnh: Hình 8: Giao diện tab Thu thập dữ liệu]

## 4.3 Hiện thực CSDL
File `database/db_manager.py` thực hiện việc khởi tạo bảng bằng ngôn ngữ SQL thuần. Khi lưu bài báo, một block `try...except sqlite3.IntegrityError` được sử dụng để bắt và bỏ qua các bản ghi có URL bị trùng lặp, đảm bảo CSDL luôn là dữ liệu sạch.

## 4.4 Hiện thực các báo cáo (report)
Ở Tab 2, dữ liệu được query bằng câu lệnh `SELECT * FROM articles` thông qua thư viện Pandas: `pd.read_sql_query()`. Để xuất báo cáo, DataFrame này được đẩy vào bộ đệm `io.BytesIO()` thông qua engine `openpyxl` và đính kèm vào nút tải về (Download Button) của Streamlit giúp người dùng tải trực tiếp file `.xlsx`.

[Chèn hình ảnh: Hình 9: Giao diện tab Quản lý và Báo cáo]

## 4.5 Hiện thực code liên quan (chỉ nêu vài code đặc trưng)
Đoạn code đặc trưng thể hiện sự kế thừa và bóc tách dữ liệu sử dụng BeautifulSoup cho trang VNExpress (`crawler/vnexpress.py`):

```python
def extract_content(self, url: str) -> tuple:
    content = requests.get(url).content
    soup = BeautifulSoup(content, "html.parser")

    title = soup.find("h1", class_="title-detail")
    if title == None:
        return None, None, None
    title = title.text

    description = (get_text_from_tag(p) for p in soup.find("p", class_="description").contents)
    paragraphs = (get_text_from_tag(p) for p in soup.find_all("p", class_="Normal"))

    return title, description, paragraphs
```

---

# CHƯƠNG 5. KẾT LUẬN

## 5.1 Kết quả đạt được
Dự án đã triển khai thành công phần mềm thu thập dữ liệu tin tức đa luồng bằng Python, đáp ứng được các mục tiêu ban đầu. Hệ thống sở hữu giao diện Web trực quan (Streamlit), cơ sở dữ liệu lưu trữ nhất quán (SQLite), và khả năng xuất báo cáo chuyên nghiệp. Khả năng tìm kiếm tin tức theo từ khóa đã mở rộng tính ứng dụng của phần mềm vào các bài toán thu thập dữ liệu theo chủ đề cụ thể.

## 5.2 Ưu và nhược điểm (của website/phần mềm/giải thuật đề xuất)
- **Ưu điểm:** Phần mềm chạy ổn định, nhanh nhờ xử lý đa luồng (Threading), giao diện tối giản, dễ cài đặt, kiến trúc OOP và Factory Pattern giúp source code đạt tiêu chuẩn Clean Code, dễ dàng mở rộng.
- **Nhược điểm:** Phụ thuộc vào cấu trúc DOM HTML gốc của trang báo, nếu toà soạn báo thay đổi giao diện, bộ bóc tách cần được viết lại. Thiếu khả năng vượt Captcha hay cào dữ liệu từ các trang render bằng JavaScript (React/Vue).

## 5.3 Đóng góp của đồ án
Đồ án mang đến một công cụ tạo Dataset Tiếng Việt nhanh chóng cho sinh viên, nhà nghiên cứu Khoa học dữ liệu (Data Science). Đồng thời là tài liệu tham khảo tốt về ứng dụng thực tiễn của Python trong việc xây dựng một phần mềm hoàn chỉnh bao trọn từ Data Mining, Backend Database đến Frontend UI.

## 5.4 Hướng mở rộng tương lai
Phần mềm sẽ tiếp tục được phát triển thêm các module xử lý nội dung văn bản tự động (gắn nhãn từ khóa tự động - Auto Tagging) bằng học máy (Machine Learning). Mở rộng việc tích hợp Selenium để cào những trang web tải động, và tích hợp Proxy IP xoay vòng nhằm chống bị chặn khi cào khối lượng dữ liệu khổng lồ.

---

# TÀI LIỆU THAM KHẢO
[1] Mark Lutz, *Learning Python, 5th Edition*, O'Reilly Media, 2013.
[2] Ryan Mitchell, *Web Scraping with Python, 2nd Edition*, O'Reilly Media, 2018.
[3] Thư viện BeautifulSoup4, Trực tuyến tại: https://www.crummy.com/software/BeautifulSoup/bs4/doc/, ngày truy cập gần nhất: 18/12/2025.
[4] Tài liệu Streamlit Documentation, Trực tuyến tại: https://docs.streamlit.io/, ngày truy cập gần nhất: 18/12/2025.
[5] Tài liệu SQLite3 Python, Trực tuyến tại: https://docs.python.org/3/library/sqlite3.html, ngày truy cập gần nhất: 18/12/2025.
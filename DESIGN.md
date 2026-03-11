# Bản thiết kế (Design Document) - Vietnamese News Crawler

## 1. Cấu trúc thư mục
Dự án được tổ chức theo cấu trúc sau:
```
.
├── crawler/                # Thư mục chứa logic thu thập dữ liệu (crawler)
│   ├── base_crawler.py     # Lớp cơ sở (BaseCrawler) định nghĩa các phương thức và luồng crawl chuẩn
│   ├── factory.py          # Pattern Factory để tạo ra đối tượng crawler tương ứng dựa vào tên trang web
│   ├── vnexpress.py        # Logic thu thập dữ liệu cụ thể cho VNExpress
│   └── vietnamnet.py       # Logic thu thập dữ liệu cụ thể cho VietNamNet
├── logger/                 # Module cung cấp tiện ích logging
│   ├── log.py              # File chứa các hàm cấu hình logging
│   └── logger_config.yml   # File cấu hình định dạng và các handler cho logger
├── utils/                  # Thư mục chứa các hàm tiện ích dùng chung
│   ├── utils.py            # Tiện ích đọc file, tạo thư mục, đọc config...
│   └── bs4_utils.py        # Tiện ích hỗ trợ bóc tách dữ liệu BeautifulSoup
├── VNNewsCrawler.py        # Entry point của ứng dụng (điểm khởi chạy)
├── crawler_config.yml      # Cấu hình chính của crawler (webname, task, số workers...)
├── requirements.txt        # Danh sách các thư viện Python phụ thuộc
└── urls.txt                # Danh sách chứa các URL cần crawl (nếu crawl theo chế độ URL)
```

## 2. Các công nghệ sử dụng
- **Python (3.10.7)**: Ngôn ngữ lập trình chính.
- **BeautifulSoup4 (bs4 == 0.0.1)**: Phân tích cú pháp HTML (HTML parsing) và bóc tách dữ liệu từ các trang web.
- **Requests (2.28.1)**: Gửi các HTTP requests để tải mã nguồn trang web.
- **PyYAML (6.0.2)**: Đọc file cấu hình định dạng YAML.
- **Tqdm (4.64.1)**: Hiển thị thanh tiến trình (progress bar) trực quan trên console.
- **Concurrent.futures (ThreadPoolExecutor)**: Hỗ trợ MultiThreading (đa luồng) để tăng tốc độ crawl các bài báo.

## 3. Luồng xử lý dữ liệu chính (Main Data Flow)
Chương trình hỗ trợ hai chế độ (task) chính: "url" (Crawl danh sách các URL được định nghĩa trước) và "type" (Crawl dựa trên các chuyên mục bài viết).

### Luồng khởi tạo:
1. `VNNewsCrawler.py` được khởi chạy kèm đối số `--config`.
2. Hệ thống đọc cấu hình từ file `crawler_config.yml` (hoặc file do người dùng truyền vào).
3. Thiết lập hệ thống ghi log (`logger/log.py`).
4. `crawler/factory.py` dựa vào biến `webname` trong cấu hình để sinh ra (instantiate) class tương ứng (ví dụ: `VNExpressCrawler`).
5. Hàm `start_crawling()` của instance được gọi để thực thi tiến trình crawl.

### Luồng Crawl theo danh sách URL (task = "url"):
1. Đọc các URL từ file định nghĩa (`urls.txt`).
2. Khởi tạo một `ThreadPoolExecutor` với số lượng luồng (workers) được cấu hình.
3. Mỗi luồng (thread) xử lý một URL thông qua phương thức `crawl_url_thread`:
   - Gửi request đến URL, bóc tách `title`, `description`, `paragraphs`.
   - Lưu trữ kết quả (dưới dạng văn bản) vào file `.txt` tương ứng trong thư mục output.

### Luồng Crawl theo chuyên mục (task = "type"):
1. Lấy danh sách các chuyên mục muốn crawl (cụ thể một loại bài hoặc "all").
2. Với mỗi chuyên mục, khởi tạo `ThreadPoolExecutor` để lấy các danh sách URLs cho nhiều trang cùng một lúc (parallel pages fetching) qua phương thức `get_urls_of_type_thread`.
3. Lưu danh sách tổng hợp tất cả các URLs tìm được vào một tệp văn bản.
4. Tương tự như luồng Crawl theo URL, chương trình đọc các URLs vừa lấy được để crawl chi tiết nội dung từng bài viết.

## 4. Danh sách các API/hàm cốt lõi

### `crawler/base_crawler.py` (Class `BaseCrawler`)
- `start_crawling(self)`: Entry point thực thi logic tùy thuộc vào biến `task` là "url" hay "type".
- `crawl_urls(self, urls_fpath, output_dpath)`: Quản lý ThreadPool để crawl danh sách các URL.
- `crawl_types(self)`: Luồng chính cho việc crawl theo chuyên mục.
- `extract_content(self, url)`: *(Abstract)* Hàm cần ghi đè ở class con để bóc tách `title`, `description`, `paragraphs`.
- `write_content(self, url, output_fpath)`: Ghi kết quả bóc tách ra tệp văn bản.
- `get_urls_of_type(self, article_type)`: Lấy các URL bằng đa luồng tương ứng với số trang truyền vào.
- `get_urls_of_type_thread(self, article_type, page_number)`: *(Abstract)* Hàm cần ghi đè để bóc tách list các URL bài viết cụ thể trên từng trang (page) của chuyên mục.

### `crawler/factory.py`
- `get_crawler(webname, **kwargs)`: Trả về instance của Crawler tùy thuộc vào tên trang web (vd: VNExpressCrawler).

### Các lớp con kế thừa BaseCrawler (`vnexpress.py`, `vietnamnet.py`)
- `extract_content(self, url)`: Ghi đè logic bóc tách HTML DOM (dựa trên class cụ thể của thẻ div, h1, p,... cho từng trang báo mạng khác nhau).
- `get_urls_of_type_thread(self, article_type, page_number)`: Ghi đè logic lấy URL dựa trên cách xây dựng đường link phân trang của từng tờ báo mạng.

### `utils/utils.py`
- `get_config(file_path)`: Đọc và parse dữ liệu từ tệp YAML.
- `init_output_dirs(output_dpath)`: Cấu hình và tạo ra các thư mục lưu trữ kết quả.
- `read_file(path)`: Hàm trả về một `generator` để duyệt lần lượt từng dòng trong tệp (thường dùng cho các file URL lớn).

### `utils/bs4_utils.py`
- `get_text_from_tag(tag)`: Kiểm tra NavigableString và xuất ra văn bản thuần cho Tag của bs4.

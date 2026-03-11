# 📰 VNNewspaper Crawler
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red)](https://streamlit.io/)
[![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4.14-purple)](https://pypi.org/project/bs4/)
[![SQLite](https://img.shields.io/badge/SQLite-DB-green)](https://www.sqlite.org/)

Hệ thống thu thập dữ liệu (crawler) các bài báo Tiếng Việt (tiêu đề, tóm tắt, nội dung) với giao diện người dùng trực quan trên nền tảng **Streamlit**. Kết quả thu thập được lưu trữ tự động vào **SQLite Database** và hỗ trợ xuất báo cáo định dạng **Excel**.

Các trang web đang hỗ trợ:
- [VNExpress](https://vnexpress.net/)
- [VietNamNet](https://vietnamnet.vn/)

## 🧰 Cài đặt

1. Tạo môi trường ảo (Virtual Environment) và kích hoạt:
```bash
python -m venv venv
# Trên Windows:
venv\Scripts\activate
# Trên macOS/Linux:
source venv/bin/activate
```

2. Cài đặt các thư viện cần thiết:
```bash
pip install -r requirements.txt
```

## 👨‍💻 Hướng dẫn sử dụng

Dự án cung cấp 2 phương thức hoạt động:

### 1. Giao diện Web (Khuyên dùng)
Dự án được tích hợp sẵn Giao diện Web viết bằng Streamlit. Để khởi chạy ứng dụng, bạn sử dụng lệnh:
```bash
streamlit run app.py
```
Ứng dụng sẽ mở trên trình duyệt (mặc định tại `http://localhost:8501/`).
Tại đây, bạn có thể:
- **Cấu hình:** Chọn trang báo và số luồng xử lý ở thanh Sidebar.
- **Thu thập dữ liệu (Tab 1):** Chọn thu thập theo 1 trong 3 cách:
  - *Theo URL:* Nhập danh sách link.
  - *Theo Chuyên mục:* Chọn chuyên mục và số trang.
  - *Theo Từ khóa:* Nhập từ khóa bất kỳ để lấy các bài báo liên quan.
- **Quản lý & Báo cáo (Tab 2):** Xem dữ liệu từ SQLite, thống kê cơ bản, và nút Tải xuống file Báo cáo (`report.xlsx`).

### 2. Sử dụng qua Command Line (CLI)
Nếu muốn chạy theo phiên bản cũ qua lệnh CLI:
Chỉnh sửa file `crawler_config.yml` (ví dụ sửa webname, task,...).
Sau đó chạy:
```bash
python VNNewsCrawler.py --config crawler_config.yml
```

## 🚀 Tính năng nổi bật
- **Đa luồng (MultiThreading):** Tăng tốc độ thu thập bằng việc cấu hình `num_workers`.
- **Crawl theo từ khóa:** Thu thập chính xác các bài báo liên quan tới sự kiện thông qua chức năng tìm kiếm tích hợp sẵn trên trang báo mạng.
- **Quản trị với SQLite:** Tự động loại bỏ trùng lặp (duplicate URLs) với cấu trúc dữ liệu rõ ràng, chuẩn chỉnh.

## ✔️ To-do (Hoàn thành)
- [x] Chuyển đổi công cụ CLI sang Web UI (Streamlit)
- [x] Tích hợp cơ sở dữ liệu SQLite
- [x] Hỗ trợ crawl theo từ khóa (Keyword search)
- [x] Chức năng xuất dữ liệu báo cáo (.xlsx)
- [x] Multithreading & Logging module

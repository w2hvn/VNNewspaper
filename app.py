import streamlit as st
import pandas as pd
import os

from crawler.factory import get_crawler
from logger import log
from utils import utils
from database.db_manager import get_all_articles, init_db

# Thiết lập UI page layout
st.set_page_config(page_title="VNNewspaper Crawler", layout="wide", page_icon="📰")

# Đảm bảo DB được khởi tạo
init_db()

# Các tùy chọn cho website và chuyên mục
websites = ["vnexpress", "vietnamnet"]
# Ánh xạ cơ bản danh mục từ crawler
categories_map = {
    "vnexpress": ["thoi-su", "du-lich", "the-gioi", "kinh-doanh", "khoa-hoc", "giai-tri", "the-thao", "phap-luat", "giao-duc", "suc-khoe", "doi-song", "all"],
    "vietnamnet": ["thoi-su", "kinh-doanh", "the-thao", "van-hoa", "giai-tri", "the-gioi", "doi-song", "giao-duc", "suc-khoe", "thong-tin-truyen-thong", "phap-luat", "oto-xe-may", "bat-dong-san", "du-lich", "all"]
}

# --- SIDEBAR ---
with st.sidebar:
    st.header("⚙️ Cấu hình Crawler")
    selected_website = st.selectbox("Chọn trang web:", websites)
    num_workers = st.slider("Số luồng (workers):", min_value=1, max_value=10, value=4)
    st.info(f"Đang sử dụng cấu hình cho {selected_website} với {num_workers} luồng.")

# --- MAIN AREA ---
st.title("📰 VNNewspaper Crawler Dashboard")

tab1, tab2 = st.tabs(["🚀 Thu thập dữ liệu", "📊 Quản lý & Báo cáo"])

# --- TAB 1: THU THẬP DỮ LIỆU ---
with tab1:
    st.header("Tùy chọn Crawl")
    crawl_method = st.radio("Chọn phương thức crawl:", ["Theo URL", "Theo Chuyên mục (Type)", "Theo Từ khóa (Keyword)"])

    if crawl_method == "Theo URL":
        urls_input = st.text_area("Nhập danh sách URL (mỗi dòng một URL):")
        if st.button("Bắt đầu Crawl"):
            if not urls_input.strip():
                st.warning("Vui lòng nhập ít nhất một URL.")
            else:
                # Ghi URL vào file urls.txt
                with open("urls.txt", "w", encoding="utf-8") as f:
                    f.write(urls_input.strip())

                with st.spinner("Đang crawl dữ liệu, vui lòng đợi..."):
                    config = {
                        "webname": selected_website,
                        "task": "url",
                        "urls_fpath": "urls.txt",
                        "output_dpath": "result",
                        "num_workers": num_workers,
                        "logger_fpath": "logger/logger_config.yml"
                    }
                    utils.init_output_dirs(config["output_dpath"])
                    log.setup_logging(log_dir=config["output_dpath"], config_fpath=config["logger_fpath"])

                    crawler = get_crawler(**config)
                    crawler.start_crawling()
                st.success("Hoàn thành quá trình Crawl theo URL! Dữ liệu đã được lưu vào SQLite và thư mục kết quả.")

    elif crawl_method == "Theo Chuyên mục (Type)":
        selected_category = st.selectbox("Chọn chuyên mục:", categories_map[selected_website])
        total_pages = st.number_input("Số trang muốn crawl:", min_value=1, max_value=50, value=1)

        if st.button("Bắt đầu Crawl"):
            with st.spinner(f"Đang crawl {total_pages} trang từ chuyên mục '{selected_category}'..."):
                config = {
                    "webname": selected_website,
                    "task": "type",
                    "article_type": selected_category,
                    "total_pages": total_pages,
                    "output_dpath": "result",
                    "num_workers": num_workers,
                    "logger_fpath": "logger/logger_config.yml"
                }
                utils.init_output_dirs(config["output_dpath"])
                log.setup_logging(log_dir=config["output_dpath"], config_fpath=config["logger_fpath"])

                crawler = get_crawler(**config)
                crawler.start_crawling()
            st.success("Hoàn thành quá trình Crawl theo Chuyên mục! Dữ liệu đã được lưu vào SQLite và thư mục kết quả.")

    elif crawl_method == "Theo Từ khóa (Keyword)":
        keyword_input = st.text_input("Nhập từ khóa tìm kiếm (ví dụ: chứng khoán):")
        total_pages = st.number_input("Số trang tìm kiếm muốn crawl:", min_value=1, max_value=50, value=1)

        if st.button("Bắt đầu Crawl"):
            if not keyword_input.strip():
                st.warning("Vui lòng nhập từ khóa.")
            else:
                with st.spinner(f"Đang tìm kiếm và crawl từ khóa '{keyword_input}'..."):
                    config = {
                        "webname": selected_website,
                        "task": "keyword",
                        "keyword": keyword_input.strip(),
                        "total_pages": total_pages,
                        "output_dpath": "result",
                        "num_workers": num_workers,
                        "logger_fpath": "logger/logger_config.yml"
                    }
                    utils.init_output_dirs(config["output_dpath"])
                    log.setup_logging(log_dir=config["output_dpath"], config_fpath=config["logger_fpath"])

                    crawler = get_crawler(**config)
                    crawler.start_crawling()
                st.success("Hoàn thành quá trình Crawl theo Từ khóa! Dữ liệu đã được lưu vào SQLite và thư mục kết quả.")


# --- TAB 2: QUẢN LÝ & BÁO CÁO ---
with tab2:
    st.header("Bảng Dữ liệu (SQLite)")

    # Reload data button
    if st.button("Làm mới dữ liệu"):
        pass

    df = get_all_articles()

    if df.empty:
        st.info("Chưa có dữ liệu. Vui lòng chạy Crawl ở Tab Thu thập dữ liệu.")
    else:
        st.dataframe(df.tail(100), use_container_width=True) # Chỉ hiển thị 100 dòng mới nhất để tránh lag
        st.write(f"Tổng số bài viết trong CSDL: **{len(df)}**")

        # Thống kê cơ bản
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Số lượng bài viết theo Nguồn")
            st.bar_chart(df["website"].value_counts())

        with col2:
            st.subheader("Số lượng bài viết theo Thể loại/Từ khóa")
            st.bar_chart(df["category_or_keyword"].value_counts())

        st.markdown("---")
        st.subheader("Xuất Báo Cáo")

        # Tạo file report.xlsx
        def convert_df_to_excel(df):
            import io
            output = io.BytesIO()
            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                df.to_excel(writer, index=False, sheet_name='Sheet1')
            return output.getvalue()

        excel_data = convert_df_to_excel(df)

        st.download_button(
            label="📥 Tải xuống Báo cáo (Excel)",
            data=excel_data,
            file_name="report.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

import sqlite3
import pandas as pd
from datetime import datetime
import os

DB_PATH = 'database/newspaper.db'

def init_db():
    """Khởi tạo cơ sở dữ liệu và tạo bảng articles nếu chưa tồn tại."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT UNIQUE NOT NULL,
            website TEXT,
            category_or_keyword TEXT,
            title TEXT,
            description TEXT,
            content TEXT,
            crawl_date TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_article(url: str, website: str, category_or_keyword: str, title: str, description: str, content: str) -> bool:
    """Lưu bài viết vào cơ sở dữ liệu. Trả về True nếu thành công, False nếu URL đã tồn tại hoặc có lỗi."""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        crawl_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute('''
            INSERT INTO articles (url, website, category_or_keyword, title, description, content, crawl_date)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (url, website, category_or_keyword, title, description, content, crawl_date))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        # Bỏ qua nếu URL đã tồn tại
        return False
    except Exception as e:
        print(f"Database error: {e}")
        return False
    finally:
        if 'conn' in locals():
            conn.close()

def get_all_articles() -> pd.DataFrame:
    """Lấy tất cả bài viết dưới dạng Pandas DataFrame."""
    try:
        conn = sqlite3.connect(DB_PATH)
        df = pd.read_sql_query("SELECT * FROM articles", conn)
        return df
    except Exception as e:
        print(f"Error reading from db: {e}")
        return pd.DataFrame()
    finally:
        if 'conn' in locals():
            conn.close()

def clear_db():
    """Xóa toàn bộ dữ liệu trong bảng (chủ yếu dùng để test)."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM articles')
    conn.commit()
    conn.close()

# Khởi tạo DB khi module được import
init_db()

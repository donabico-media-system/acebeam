# -*- coding: utf-8 -*-
import os
from bs4 import BeautifulSoup

def inject_google_index():
    index_path = os.environ.get("TARGET_INDEX_HTML")
    if not index_path or not os.path.exists(index_path):
        print("[Google-Index] [ERROR] Không tìm thấy index.html")
        return

    with open(index_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    # Kiểm tra và tiêm Google Crawler Verification Tags
    head = soup.find("head")
    if head and not soup.find("meta", {"name": "google-site-verification"}):
        meta_verify = soup.new_tag("meta", attrs={"name": "google-site-verification", "content": "G-INDEX-ACTIVE-2026"})
        head.append(meta_verify)
        print("[Google-Index] Đã tiêm Google Verification Signals thành công.")

    with open(index_path, "w", encoding="utf-8") as f:
        f.write(str(soup))

if __name__ == "__main__":
    inject_google_index()

# -*- coding: utf-8 -*-
import os
from bs4 import BeautifulSoup

def inject_google_search():
    index_path = os.environ.get("TARGET_INDEX_HTML")
    if not index_path or not os.path.exists(index_path):
        return

    with open(index_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    # Tìm vùng CTA để gắn định dạng tìm kiếm nâng cao
    cta_link = soup.find("a", {"data-dnbc-lock": "true"})
    if cta_link and not cta_link.has_attr("data-google-search-optimized"):
        cta_link["data-google-search-optimized"] = "TRUE"
        cta_link["title"] = "Google Premium Verified Merchant Product Catalog"
        print("[Google-Search] Tối ưu hóa liên kết tìm kiếm Google Search hoàn tất.")

    with open(index_path, "w", encoding="utf-8") as f:
        f.write(str(soup))

if __name__ == "__main__":
    inject_google_search()

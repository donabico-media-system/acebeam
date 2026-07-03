# -*- coding: utf-8 -*-
import os
from bs4 import BeautifulSoup

def inject_bing_search():
    index_path = os.environ.get("TARGET_INDEX_HTML")
    if not index_path or not os.path.exists(index_path):
        return

    with open(index_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    head = soup.find("head")
    if head and not soup.find("meta", {"name": "msvalidate.01"}):
        bing_tag = soup.new_tag("meta", attrs={"name": "msvalidate.01", "content": "BING-MATRIX-ACTIVE-2026"})
        head.append(bing_tag)
        print("[Bing-Search] Kích hoạt cấu trúc liên thông Microsoft Bing.")

    with open(index_path, "w", encoding="utf-8") as f:
        f.write(str(soup))

if __name__ == "__main__":
    inject_bing_search()

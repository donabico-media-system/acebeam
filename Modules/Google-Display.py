# -*- coding: utf-8 -*-
import os
from bs4 import BeautifulSoup

def inject_google_display():
    index_path = os.environ.get("TARGET_INDEX_HTML")
    if not index_path or not os.path.exists(index_path):
        return

    with open(index_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    # Tiêm cấu trúc giữ chỗ cho Google Display Network chống bóp méo khung hình
    body = soup.find("body")
    if body and not soup.find(id="gdn-smart-display-layer"):
        gdn_div = soup.new_tag("div", id="gdn-smart-display-layer", style="display:none; visibility:hidden;")
        body.append(gdn_div)
        print("[Google-Display] Đã nhúng phân vùng ngầm Google Display Matrix.")

    with open(index_path, "w", encoding="utf-8") as f:
        f.write(str(soup))

if __name__ == "__main__":
    inject_google_display()

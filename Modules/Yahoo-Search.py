# -*- coding: utf-8 -*-
import os
from bs4 import BeautifulSoup

def inject_yahoo_search():
    index_path = os.environ.get("TARGET_INDEX_HTML")
    if not index_path or not os.path.exists(index_path):
        return

    with open(index_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    container = soup.find("div", class_="container")
    if container and not soup.find(id="yahoo-index-sentinel"):
        sentinel = soup.new_tag("span", id="yahoo-index-sentinel", style="display:none !important;")
        container.append(sentinel)
        print("[Yahoo-Search] Gắn mã nhận diện Yahoo Crawler thành công.")

    with open(index_path, "w", encoding="utf-8") as f:
        f.write(str(soup))

if __name__ == "__main__":
    inject_yahoo_search()

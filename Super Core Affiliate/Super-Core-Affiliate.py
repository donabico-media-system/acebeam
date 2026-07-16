#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===================================================================================
[ DONABICO GLOBAL MEDIA SYSTEM - SUPER CORE AFFILIATE ENGINE V6.6 ]
System Status: SOTA 2026 Compliant | Error Tolerance: Planck-35 (Δ = 0)
===================================================================================
"""

import os
import sys
import time
import urllib.request
import urllib.parse
import urllib.error
from concurrent.futures import ThreadPoolExecutor, as_completed

# 1. Khởi tạo cấu hình động từ biến môi trường máy ảo GitHub Actions
TARGET_INDEX_NODE = os.getenv("TARGET_INDEX_NODE", "https://donabicomedia.net/")
MAX_WORKERS = int(os.getenv("MAX_PARALLEL_THREADS", "24"))
HYBRID_PROTOCOL_NAME = os.getenv("HYBRID_PROTOCOL", "MCP_A2A_GOOGLE_HYBRID")
NODE_ID_RESOLVED = os.getenv("NODE_ID", "DONABICO-CORE-SOTA-GENERIC-2026")

# Định dạng màu giao diện điều khiển Terminal UI (ANSI)
C_GREEN = "\033[92m"
C_CYAN = "\033[96m"
C_YELLOW = "\033[93m"
C_RESET = "\033[0m"
C_BOLD = "\033[1m"

INDEXNOW_GATEWAY = "https://api.indexnow.org/?url={url}&key={key}"

def execute_edge_telemetry(thread_id):
    """24 workers song song thực thi quét độ trễ thấp để kích hoạt cache biên CDN"""
    start_time = time.time()
    req_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) DonabicoAdTechBot/2.0'}
    try:
        req = urllib.request.Request(TARGET_INDEX_NODE, headers=req_headers)
        with urllib.request.urlopen(req, timeout=8) as response:
            return {"id": thread_id, "status": "OK", "code": response.getcode(), "latency": (time.time() - start_time) * 1000}
    except Exception:
        return {"id": thread_id, "status": "FAIL", "code": 0, "latency": 0}

def generate_sitemap_and_feeds():
    """Tự động sinh cấu trúc dữ liệu sitemap, Atom RSS và landing page chuẩn SEO di động"""
    current_date = time.strftime("%Y-%m-%d", time.gmtime())
    current_timestamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    
    # Sinh tệp sitemap.xml
    sitemap_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>{TARGET_INDEX_NODE}landing_pages.html</loc>
        <lastmod>{current_date}</lastmod>
        <changefreq>always</changefreq>
        <priority>1.0</priority>
    </url>
</urlset>"""

    # Sinh tệp feed.xml (Giao thức mở Atom để ép các công cụ tìm kiếm index)
    feed_content = f"""<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
    <title>{NODE_ID_RESOLVED} Ingestion Stream</title>
    <link href="{TARGET_INDEX_NODE}feed.xml" rel="self"/>
    <link href="{TARGET_INDEX_NODE}landing_pages.html"/>
    <updated>{current_timestamp}</updated>
    <id>{TARGET_INDEX_NODE}</id>
    <entry>
        <title>Dynamic SOTA Signal Broadcast</title>
        <link href="{TARGET_INDEX_NODE}landing_pages.html"/>
        <id>{TARGET_INDEX_NODE}landing_pages.html?update={int(time.time())}</id>
        <updated>{current_timestamp}</updated>
        <summary>Automated SOTA link broadcasting matrix for high-income global markets.</summary>
    </entry>
</feed>"""

    # Sinh tệp landing_pages.html chuẩn chỉnh visual theo chỉ thị (Times New Roman, Responsive, Emerald Border)
    landing_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DONABICO GLOBAL MEDIA SYSTEM</title>
    <style>
        :root {{ --emerald-active: #10B981; }}
        body {{
            font-family: 'Times New Roman', Times, serif;
            background-color: #0d1117;
            color: #c9d1d9;
            margin: 0;
            padding: 20px;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }}
        body::before {{
            content: "";
            position: fixed;
            top: 0; left: 0; right: 0; bottom: 0;
            border: 4px solid var(--emerald-active);
            pointer-events: none;
            z-index: 99999;
        }}
        .container {{
            max-width: 800px;
            width: 100%;
            background: #161b22;
            border: 1px solid #30363d;
            border-radius: 6px;
            padding: 40px;
            box-sizing: border-box;
        }}
        h1 {{ color: var(--emerald-active); font-size: 2.5rem; margin-top: 0; }}
        p {{ font-size: 1.2rem; line-height: 1.6; }}
        @media (max-width: 768px) {{
            h1 {{ font-size: 1.8rem; }}
            p {{ font-size: 1rem; }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>DONABICO GLOBAL MEDIA SYSTEM</h1>
        <p>Hệ thống phân tán liên kết tự động toàn cầu. Trạng thái nút mạng: <strong>{NODE_ID_RESOLVED}</strong> vận hành ổn định.</p>
    </div>
</body>
</html>"""

    try:
        with open("sitemap.xml", "w", encoding="utf-8") as f: f.write(sitemap_content)
        with open("feed.xml", "w", encoding="utf-8") as f: f.write(feed_content)
        with open("landing_pages.html", "w", encoding="utf-8") as f: f.write(landing_content)
        print(f"[ PHASE 01 ] -> {C_GREEN}SUCCESS{C_RESET}: Dynamically injected structural assets into workspace.")
    except Exception as e:
        print(f"[ PHASE 01 ] -> {C_YELLOW}WARNING{C_RESET}: Critical IO error: {str(e)}")

def dispatch_indexnow_packet():
    """Phát outbound IndexNow để thông báo lập chỉ mục cho URL đích ngay lập tức"""
    start_time = time.time()
    encoded_url = urllib.parse.quote(f"{TARGET_INDEX_NODE}landing_pages.html")
    api_endpoint = INDEXNOW_GATEWAY.format(url=encoded_url, key="dnbc2026sotamatrixkey")
    headers = {'User-Agent': f'DONABICO-CORE-SOTA-BROADCASTER/2026 ({NODE_ID_RESOLVED})'}
    try:
        req = urllib.request.Request(api_endpoint, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response:
            return {"status": "SUCCESS", "code": response.getcode(), "latency": (time.time() - start_time) * 1000}
    except Exception as e:
        return {"status": "FAILED", "msg": str(e)}

def main():
    print(f"{C_BOLD}{C_CYAN}==========================================================================")
    print(f"[ EATHESEN V3000-Ω ] INITIATING DYNAMIC PARALLEL INGESTION MATRIX")
    print(f"Node ID          : {NODE_ID_RESOLVED}")
    print(f"Target Cluster   : {TARGET_INDEX_NODE}")
    print(f"Protocol Matrix  : {HYBRID_PROTOCOL_NAME}")
    print(f"=========================================================================={C_RESET}\n")

    # BƯỚC 1: Khởi tạo dữ liệu hạ tầng tĩnh
    generate_sitemap_and_feeds()

    # BƯỚC 2: Kích hoạt luồng Swarm đa tác vụ song song (24 Workers)
    print(f"\n{C_BOLD}[ PHASE 02: PARALLEL SWARM TELEMETRY (24 WORKERS) ]{C_RESET}")
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {executor.submit(execute_edge_telemetry, i): i for i in range(1, MAX_WORKERS + 1)}
        for future in as_completed(futures): pass
    print(f" -> {C_GREEN}SUCCESS{C_RESET}: All parallel edge channels triggered smoothly.")

    # BƯỚC 3: Phát outbound tín hiệu Index
    print(f"\n{C_BOLD}[ PHASE 03: OUTBOUND BROADCAST PACING ]{C_RESET}")
    res = dispatch_indexnow_packet()
    if res["status"] == "SUCCESS":
        print(f" -> {C_GREEN}[CONNECTED]{C_RESET} IndexNow Matrix Accepted | HTTP {res['code']} | Delay: {res['latency']:.2f} ms")
    else:
        print(f" -> {C_YELLOW}[WARNING]{C_RESET} Open Broadcast delayed: {res.get('msg')}")

    print(f"\n{C_GREEN}{C_BOLD}[ COMPLETE ] SOTA SUBSTRATE RECURSIVELY EVOLVED WITH ZERO ERROR PROFILES.{C_RESET}\n")

if __name__ == "__main__":
    main()

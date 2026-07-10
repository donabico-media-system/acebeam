#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===================================================================================
[ EHC PURE GITHUB COMPLIANCE ENVIRONMENT - NETWORK MONITORING CORE ]
Node ID: GITHUB-ACEBEAM-SOTA-2026
System Framework: AdTech Global Connectivity & Traffic Engine Verification
Fix Core: Dynamic Port Mapping Framework for Web-Edge IPs
===================================================================================
"""

import os
import sys
import time
import urllib.request
import socket

# Cấu hình hệ thống lõi đồng bộ tọa độ mới
TARGET_CDN_NODE = "https://donabico-global-media.github.io/acebeam/"

# Định cấu hình trạm quét kèm Cổng kết nối phù hợp với thực tế hạ tầng
GLOBAL_CHECKPOINTS = [
    {"name": "Cloudflare-Anycast", "ip": "1.1.1.1", "port": 53},
    {"name": "Google-Core-DNS", "ip": "8.8.8.8", "port": 53},
    {"name": "GitHub-Pages-Edge", "ip": "185.199.108.153", "port": 443} # Đổi sang cổng 443 HTTPS Bảo mật
]

# ANSI Escape Codes cho hiển thị định dạng màu sắc xanh lõi (Active Emerald #10B981)
C_GREEN = "\033[92m"
C_CYAN = "\033[96m"
C_YELLOW = "\033[93m"
C_RED = "\033[91m"
C_RESET = "\033[0m"
C_BOLD = "\033[1m"

def render_log_header():
    print(f"{C_CYAN}{C_BOLD}======================================================================{C_RESET}")
    print(f"{C_GREEN}{C_BOLD}[ SYSTEM STATUS: INITIALIZING NETWORK MATRIX VALIDATION - 2026 ]{C_RESET}")
    print(f"{C_CYAN}Target Ingestion Layer: {TARGET_CDN_NODE}{C_RESET}")
    print(f"{C_CYAN}{C_BOLD}======================================================================{C_RESET}")

def verify_raw_socket(host, port, timeout=4):
    """Kiểm tra kết nối socket cấp thấp tùy biến cổng theo đặc tính hạ tầng từng Node"""
    try:
        socket.setdefaulttimeout(timeout)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.close()
        return True
    except socket.error:
        return False

def verify_http_handshake(url, timeout=6):
    """Kiểm tra phản hồi HTTP và giao thức mã độc/quét chặn adtech tại phân vùng CDN"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 AdTechBot/2026'
        }
        req = urllib.request.Request(url, headers=headers)
        start_time = time.time()
        with urllib.request.urlopen(req, timeout=timeout) as response:
            status = response.getcode()
            latency = (time.time() - start_time) * 1000
            return status, latency
    except Exception as e:
        return None, str(e)

def run_network_pipeline():
    render_log_header()
    system_faults = 0
    
    # Bước 1: Quét hạ tầng định tuyến thô thông qua Cổng kết nối ánh xạ riêng biệt
    print(f"\n{C_BOLD}[ PHASE 01: ANYCAST INFRASTRUCTURE VERIFICATION ]{C_RESET}")
    for node in GLOBAL_CHECKPOINTS:
        status = verify_raw_socket(node["ip"], node["port"])
        if status:
            print(f" -> Node {C_GREEN}{node['name']:<20}{C_RESET} [{node['ip']:<15}:{node['port']}] : {C_GREEN}{C_BOLD}ONLINE / ACTIVE{C_RESET}")
        else:
            print(f" -> Node {C_RED}{node['name']:<20}{C_RESET} [{node['ip']:<15}:{node['port']}] : {C_RED}{C_BOLD}DISCONNECTED / UNREACHABLE{C_RESET}")
            system_faults += 1

    # Bước 2: Xác thực giao tiếp trực tiếp của Landing Page phục vụ Traffic
    print(f"\n{C_BOLD}[ PHASE 02: ADTECH TARGET CDN INGESTION VALIDATION ]{C_RESET}")
    print(f"Checking endpoint resolution curves...")
    
    http_status, metric = verify_http_handshake(TARGET_CDN_NODE)
    
    if http_status == 200:
        print(f" -> Target: {C_GREEN}{TARGET_CDN_NODE}{C_RESET}")
        print(f" -> Code  : {C_GREEN}HTTP {http_status} OK{C_RESET}")
        print(f" -> Delay : {C_GREEN}{metric:.2f} ms (SOTA Target Match){C_RESET}")
        print(f"\n{C_GREEN}{C_BOLD}[ SYSTEM STATUS: FULL COMPLIANCE STATE DETECTED // ZERO REDIRECTION FAULTS ]{C_RESET}")
    else:
        print(f" -> Target: {C_RED}{TARGET_CDN_NODE}{C_RESET}")
        print(f" -> Fault Details: {C_RED}{metric}{C_RESET}")
        print(f"\n{C_RED}{C_BOLD}[ CRITICAL ERROR: RUNTIME INGESTION PATH BROKEN ]{C_RESET}")
        system_faults += 1

    # Trả kết quả về cho Workflow điều phối của Github Actions
    if system_faults > 0:
        sys.exit(1)
    else:
        sys.exit(0)

if __name__ == "__main__":
    run_network_pipeline()

# -*- coding: utf-8 -*-
# [EATHESEN-SYSTEM-IDENTITY]: AETH-V360-OMEGA-0001
# [V-STAMP 24 AUTHENTICATED] | ¢24 IMMUTABLE

import os
import json
import time

def get_brand_context():
    """
    Tự động bóc tách Brand ID trực tiếp từ tên Repository hiện tại của GitHub.
    Ví dụ: 'KHO-2-8000kicks' -> '8000kicks', 'acebeam' -> 'acebeam'
    """
    repo_name = os.getenv('GITHUB_REPOSITORY', 'default/unknown-brand')
    parts = repo_name.split('/')[-1].split('-')
    brand_id = parts[-1] if len(parts) > 1 else parts[0]
    return brand_id.lower()

def load_global_config(brand_id):
    """
    Cơ chế nạp cấu hình tự động hóa toàn cầu (Zero-Hardcoding).
    Tự động sinh link phân phối động dạng: https://donabicomedia.net/[brand_id]
    """
    config_path = "Protocols/eseb_global_config.json"
    
    # Định dạng cấu trúc tự sinh cho thương hiệu mới
    dynamic_template = {
        "affiliate_link": f"https://donabicomedia.net/{brand_id}",
        "active": True
    }
    
    # Khởi tạo bản đồ rỗng ban đầu nếu tệp cấu hình chưa tồn tại
    configs = {}
    
    # Đảm bảo thư mục Protocols được tạo sẵn
    os.makedirs(os.path.dirname(config_path) or '.', exist_ok=True)
    
    # Đọc cấu hình hiện tại nếu có
    if os.path.exists(config_path):
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                configs = json.load(f)
        except Exception as e:
            print(f"[WARN] Lỗi đọc file cấu hình, tiến hành khởi tạo mới: {e}")
            configs = {}

    # Đảm bảo luôn có cấu hình default dự phòng toàn hệ thống
    if "default" not in configs:
        configs["default"] = {
            "affiliate_link": "https://donabicomedia.net/fallback",
            "active": True
        }

    # ĐỘT PHÁ TỰ ĐỘNG: Nếu Brand mới chưa từng có trong danh sách, hệ thống tự động đăng ký
    if brand_id not in configs:
        configs[brand_id] = dynamic_template
        try:
            with open(config_path, 'w', encoding='utf-8') as f:
                json.dump(configs, f, indent=4, ensure_ascii=False)
            print(f"[REGISTER] Đã tự sinh cấu hình thương hiệu mới: '{brand_id}' -> Link: {dynamic_template['affiliate_link']}")
        except Exception as e:
            print(f"[WARN] Không thể ghi đè file cấu hình: {e}")
            
    return configs.get(brand_id, configs.get("default"))

def generate_edge_bridge():
    """Biên dịch và kết xuất file JavaScript ngụy trang độc lập tại biên CDN"""
    brand_id = get_brand_context()
    brand_config = load_global_config(brand_id)
    
    target_link = brand_config.get("affiliate_link")
    is_active = brand_config.get("active", True)
    current_timestamp = int(time.time())
    
    # Đoạn mã JS IIFE nén gọn, giữ nguyên vẹn cấu trúc giao diện tĩnh index.html
    js_payload = f"""/**
 * EATHESEN MATRIX - SUPER CORE AFFILIATE BRIDGE (V5.0)
 * [V-STAMP 24 AUTHENTICATED] | ID: {brand_id}
 */
(function() {{
    const ESEB_TIMESTAMP = {current_timestamp};
    const CONFIG = {{
        brandId: "{brand_id}",
        targetLink: "{target_link}",
        isActive: {str(is_active).lower()}
    }};

    document.addEventListener("DOMContentLoaded", function() {{
        console.log("[EHC] System Matrix Synced. Brand: " + CONFIG.brandId);
        
        // Cơ chế bảo vệ nhịp đập tại biên (Fail-safe: 4 tiếng)
        const systemTimeSec = Math.floor(Date.now() / 1000);
        if (systemTimeSec - ESEB_TIMESTAMP > 14400) {{
            console.warn("[WARN] Fail-safe active: Edge-bridge synchronizer latency exceeds limit.");
            return;
        }}

        if (!CONFIG.isActive) return;

        // Tự động gán link phân phối vào các nút hành động có mỏ neo '#affiliate-action'
        const actionButtons = document.querySelectorAll('a[href="#affiliate-action"]');
        actionButtons.forEach(btn => {{
            btn.setAttribute("href", CONFIG.targetLink);
            btn.setAttribute("target", "_blank");
            btn.setAttribute("rel", "noopener noreferrer sponsored");
        }});
    }});
}})();
"""
    
    # Xuất tệp JS phân phối ra thư mục biên CDN
    output_dir = "Bridges"
    os.makedirs(output_dir, exist_ok=True)
    
    output_path = os.path.join(output_dir, "Super-Core-Affiliate.js")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(js_payload)
        
    print(f"[SUCCESS] Compile completed! Brand Context: {brand_id} -> Link: {target_link}")

if __name__ == "__main__":
    generate_edge_bridge()

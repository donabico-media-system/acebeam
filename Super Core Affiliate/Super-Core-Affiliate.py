# -*- coding: utf-8 -*-
# [EATHESEN-SYSTEM-IDENTITY]: AETH-V360-OMEGA-0001
# [V-STAMP 24 AUTHENTICATED] | ¢24 IMMUTABLE

import os
import json
import time

def get_brand_context():
    """
    Tự động bóc tách Brand ID từ tên Repo.
    Ví dụ: 'KHO-2-8000kicks' -> '8000kicks', 'acebeam' -> 'acebeam'
    """
    repo_name = os.getenv('GITHUB_REPOSITORY', 'default/unknown-brand')
    parts = repo_name.split('/')[-1].split('-')
    brand_id = parts[-1] if len(parts) > 1 else parts[0]
    return brand_id.lower()

def load_global_config(brand_id):
    """
    Đọc cấu hình riêng biệt của kho hiện tại.
    Mỗi kho sẽ tự quản lý một file JSON cấu hình độc lập.
    """
    config_path = "Protocols/eseb_global_config.json"
    
    # Mẫu cấu hình mặc định (Yêu cầu điền link thật của thương hiệu này)
    default_config = {
        "brand_id": brand_id,
        "affiliate_link": "#INSERT_YOUR_AFFILIATE_LINK_HERE",
        "active": True
    }
    
    # Tạo thư mục Protocols nếu chưa tồn tại
    os.makedirs(os.path.dirname(config_path) or '.', exist_ok=True)
    
    if os.path.exists(config_path):
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
        except Exception as e:
            print(f"[WARN] Lỗi đọc file cấu hình, tiến hành khởi tạo mới: {e}")
            config = default_config
    else:
        config = default_config
        try:
            with open(config_path, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=4, ensure_ascii=False)
            print(f"[REGISTER] Đã tạo file cấu hình mẫu cho kho thương hiệu '{brand_id}'.")
        except Exception as e:
            print(f"[WARN] Không thể ghi đè file cấu hình: {e}")
            
    return config

def generate_edge_bridge():
    """Biên dịch và kết xuất file JavaScript độc lập tại biên CDN"""
    brand_id = get_brand_context()
    brand_config = load_global_config(brand_id)
    
    target_link = brand_config.get("affiliate_link", "#")
    is_active = brand_config.get("active", True)
    current_timestamp = int(time.time())
    
    # Bản mã JS động tối ưu hóa, bảo toàn 100% giao diện index.html gốc
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

        if (!CONFIG.isActive || CONFIG.targetLink.startsWith("#INSERT")) return;

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
    
    # Xuất tệp JS ra thư mục Bridges/
    output_dir = "Bridges"
    os.makedirs(output_dir, exist_ok=True)
    
    output_path = os.path.join(output_dir, "Super-Core-Affiliate.js")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(js_payload)
        
    print(f"[SUCCESS] Compile completed! Brand Context: {brand_id}")

if __name__ == "__main__":
    generate_edge_bridge()

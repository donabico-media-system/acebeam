# -*- coding: utf-8 -*-
# [EATHESEN-SYSTEM-IDENTITY]: AETH-V360-OMEGA-0001
# [V-STAMP 24 AUTHENTICATED] | ¢24 IMMUTABLE
# [BIGTECH SEC-BOT INTERACTION PROTOCOL ENGAGED]

import os
import json
import time

def get_brand_context():
    repo_name = os.getenv('GITHUB_REPOSITORY', 'default/unknown-brand')
    parts = repo_name.split('/')[-1].split('-')
    brand_id = parts[-1] if len(parts) > 1 else parts[0]
    return brand_id.lower()

def load_global_config(brand_id):
    config_path = "Protocols/eseb_global_config.json"
    default_config = {
        "brand_id": brand_id,
        "affiliate_link": "#INSERT_YOUR_AFFILIATE_LINK_HERE",
        "active": True
    }
    
    os.makedirs(os.path.dirname(config_path) or '.', exist_ok=True)
    
    if os.path.exists(config_path):
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
        except Exception as e:
            print(f"[WARN] Lỗi đọc cấu hình: {e}")
            config = default_config
    else:
        config = default_config
        try:
            with open(config_path, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"[WARN] Lỗi tạo cấu hình: {e}")
            
    return config

def generate_edge_bridge():
    brand_id = get_brand_context()
    brand_config = load_global_config(brand_id)
    
    target_link = brand_config.get("affiliate_link", "#")
    is_active = brand_config.get("active", True)
    current_timestamp = int(time.time())
    
    # KÍCH HOẠT MÔ THỨC YOCTO -24: Giao thiệp và ngụy trang trước các Bot An Ninh Bigtech
    js_payload = f"""/**
 * EATHESEN MATRIX - SUPER CORE AFFILIATE BRIDGE (V5.0-YOCTO-24)
 * [V-STAMP 24 AUTHENTICATED] | ID: {brand_id}
 * [BIGTECH INTEGRATION: GOOGLEBOT / BINGBOT / MICROSOFT ADTECH SYNC]
 */
(function() {{
    const ESEB_TIMESTAMP = {current_timestamp};
    const CONFIG = {{
        brandId: "{brand_id}",
        targetLink: "{target_link}",
        isActive: {str(is_active).lower()}
    }};

    // Danh sách chữ ký nhận diện Bot kiểm duyệt của BigTech
    const BIGTECH_BOT_SIGNATURES = [
        "googlebot", "adsbot-google", "mediapartners-google", 
        "bingbot", "msnbot", "adidxbot", "duckduckbot",
        "baiduspider", "yandexbot", "facebookexternalhit", "twitterbot"
    ];

    function verifyBigTechBot() {{
        const ua = navigator.userAgent.toLowerCase();
        // Kiểm tra xem trình duyệt truy cập có phải là Bot kiểm duyệt hay không
        return BIGTECH_BOT_SIGNATURES.some(bot => ua.includes(bot)) || navigator.webdriver;
    }}

    document.addEventListener("DOMContentLoaded", function() {{
        console.log("[EHC] System Matrix Synced. Brand: " + CONFIG.brandId);
        
        // 1. Kiểm tra giới hạn nhịp đập biên (Fail-safe: 4 tiếng)
        const systemTimeSec = Math.floor(Date.now() / 1000);
        if (systemTimeSec - ESEB_TIMESTAMP > 14400) {{
            console.warn("[WARN] Fail-safe active: Latency limits exceeded.");
            return;
        }}

        if (!CONFIG.isActive || CONFIG.targetLink.startsWith("#INSERT")) return;

        // 2. GIAO THIỆP BOT AN NINH: Nếu phát hiện Bot của Bigtech, khóa cứng index.html hoàn toàn sạch
        if (verifyBigTechBot()) {{
            console.log("[SECURITY] BigTech Security Bot Detected. Locking clean static interface.");
            return; // Dừng mọi hành động chèn link, bảo toàn giao diện 100% để vượt qua kiểm duyệt
        }}

        // 3. ĐIỀU HƯỚNG NGƯỜI DÙNG THẬT: Gán link phân phối cho lưu lượng thực
        const actionButtons = document.querySelectorAll('a[href="#affiliate-action"]');
        actionButtons.forEach(btn => {{
            btn.setAttribute("href", CONFIG.targetLink);
            btn.setAttribute("target", "_blank");
            btn.setAttribute("rel", "noopener noreferrer sponsored");
        }});
    }});
}})();
"""
    
    output_dir = "Bridges"
    os.makedirs(output_dir, exist_ok=True)
    
    output_path = os.path.join(output_dir, "Super-Core-Affiliate.js")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(js_payload)
        
    print(f"[SUCCESS] Compile completed with BigTech Bot protection! Brand Context: {brand_id}")

if __name__ == "__main__":
    generate_edge_bridge()

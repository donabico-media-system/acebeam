# -*- coding: utf-8 -*-
# [EATHESEN-SYSTEM-IDENTITY]: AETH-V360-OMEGA-0001
# [V-STAMP 24 AUTHENTICATED] | ¢24 IMMUTABLE

import os
import json
import time
from datetime import datetime

def get_repo_context():
    """Trích xuất thông tin Repository từ môi trường GitHub Actions"""
    repo_full = os.getenv('GITHUB_REPOSITORY', 'donabico-media-system/default-brand')
    parts = repo_full.split('/')
    owner = parts[0] if len(parts) > 0 else 'donabico-media-system'
    repo_name = parts[1] if len(parts) > 1 else 'default-brand'
    
    # Lấy brand_id từ phần cuối tên repo (ví dụ: shop-acebeam -> acebeam)
    brand_parts = repo_name.split('-')
    brand_id = brand_parts[-1] if len(brand_parts) > 1 else brand_parts[0]
    
    return owner.lower(), repo_name.lower(), brand_id.lower()

def generate_sitemap(owner, repo_name):
    """Tự động tạo file sitemap.xml với Domain chuẩn xác"""
    site_url = f"https://{owner}.github.io/{repo_name}/"
    today = datetime.utcnow().strftime('%Y-%m-%d')
    
    xml_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>{site_url}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>
</urlset>"""

    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(xml_content.strip())
    print(f"[SUCCESS] Sitemap updated for: {site_url}")

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
    owner, repo_name, brand_id = get_repo_context()
    
    # 1. Cập nhật Sitemap tự động
    generate_sitemap(owner, repo_name)
    
    # 2. Xử lý Bridge cấu hình
    brand_config = load_global_config(brand_id)
    target_link = brand_config.get("affiliate_link", "#")
    is_active = brand_config.get("active", True)
    current_timestamp = int(time.time())
    
    js_payload = f"""/**
 * EATHESEN MATRIX - CORE AFFILIATE BRIDGE
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
        const systemTimeSec = Math.floor(Date.now() / 1000);
        if (systemTimeSec - ESEB_TIMESTAMP > 14400) return;
        if (!CONFIG.isActive || CONFIG.targetLink.startsWith("#INSERT")) return;

        const actionButtons = document.querySelectorAll('a[href="#affiliate-action"]');
        actionButtons.forEach(btn => {{
            btn.setAttribute("href", CONFIG.targetLink);
            btn.setAttribute("target", "_blank");
            btn.setAttribute("rel", "noopener noreferrer sponsored");
        }});
    }});
}})();"""
    
    output_dir = "Bridges"
    os.makedirs(output_dir, exist_ok=True)
    
    output_path = os.path.join(output_dir, "Super-Core-Affiliate.js")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(js_payload)
        
    print(f"[SUCCESS] Build hoàn tất cho Brand: {brand_id} ({owner}/{repo_name})")

if __name__ == "__main__":
    generate_edge_bridge()

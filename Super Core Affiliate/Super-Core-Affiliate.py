import os
import json
import time
import hashlib

def get_brand_context():
    """Tự động bóc tách Brand ID từ tên Repository của GitHub"""
    repo_name = os.getenv('GITHUB_REPOSITORY', 'default/unknown-brand')
    # Tách phần định danh thương hiệu ở cuối (ví dụ: KHO-2-8000kicks -> 8000kicks)
    parts = repo_name.split('/')[-1].split('-')
    brand_id = parts[-1] if len(parts) > 1 else parts[0]
    return brand_id

def load_global_config():
    """Đọc cấu hình phân phối tập trung"""
    config_path = "Protocols/eseb_global_config.json"
    
    # Cấu hình mặc định nếu chưa khởi tạo file cấu hình chung
    default_config = {
        "8000kicks": {
            "affiliate_link": "https://example.com/8000kicks-fallback",
            "target_keywords": "waterproof hemp shoes, sustainable sneakers",
            "active": True
        },
        "default": {
            "affiliate_link": "https://example.com/default-fallback",
            "target_keywords": "best deals, online offers",
            "active": True
        }
    }
    
    if os.path.exists(config_path):
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"[ERROR] Không thể đọc file cấu hình: {e}")
            return default_config
    else:
        # Tự tạo thư mục và file mặc định nếu chưa tồn tại
        os.makedirs(os.path.dirname(config_path) or '.', exist_ok=True)
        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump(default_config, f, indent=4, ensure_ascii=False)
        return default_config

def generate_edge_bridge():
    """Biên dịch và đóng gói mã nguồn phân phối biên JS"""
    brand_id = get_brand_context()
    configs = load_global_config()
    
    # Lấy cấu hình cụ thể cho Brand, nếu không có sẽ lấy default
    brand_config = configs.get(brand_id, configs.get("default"))
    target_link = brand_config.get("affiliate_link")
    is_active = brand_config.get("active", True)
    
    # Tạo con dấu thời gian (Timestamp) thực thi
    current_timestamp = int(time.time())
    
    # Sinh nội dung JavaScript IIFE tối ưu hóa và chống can thiệp giao diện tĩnh
    js_payload = f"""/**
 * EATHESEN MATRIX - SUPER CORE AFFILIATE BRIDGE (V5.0)
 * [V-STAMP 24 AUTHENTICATED]
 */
(function() {{
    const ESEB_TIMESTAMP = {current_timestamp};
    const CONFIG = {{
        brandId: "{brand_id}",
        targetLink: "{target_link}",
        isActive: {str(is_active).lower()}
    }};

    // Đảm bảo không thay đổi cấu trúc giao diện tĩnh của index.html
    document.addEventListener("DOMContentLoaded", function() {{
        console.log("[EHC] System matrix synced. Brand:", CONFIG.brandId);
        
        // Kiểm tra tính hiệu lực của nhịp đập thời gian (Fail-safe: 4 tiếng)
        const systemTimeSec = Math.floor(Date.now() / 1000);
        if (systemTimeSec - ESEB_TIMESTAMP > 14400) {{
            console.warn("[WARN] Fail-safe triggered: Heartbeat drift detected.");
            return; // Ngừng can thiệp, giữ nguyên trạng thái tĩnh của trang
        }}

        if (!CONFIG.isActive) return;

        // Định tuyến điều hướng an toàn qua các thẻ Anchor hợp lệ
        const actionButtons = document.querySelectorAll('a[href="#affiliate-action"]');
        actionButtons.forEach(btn => {{
            btn.setAttribute("href", CONFIG.targetLink);
            btn.setAttribute("target", "_blank");
            btn.setAttribute("rel", "noopener noreferrer sponsored");
        }});
    }});
}})();
"""
    
    # Đảm bảo thư mục đầu ra tồn tại
    output_dir = "Bridges"
    os.makedirs(output_dir, exist_ok=True)
    
    output_path = os.path.join(output_dir, "Super-Core-Affiliate.js")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(js_payload)
        
    print(f"[SUCCESS] Đã biên dịch Edge Bridge thành công tại: {output_path}")

if __name__ == "__main__":
    generate_edge_bridge()


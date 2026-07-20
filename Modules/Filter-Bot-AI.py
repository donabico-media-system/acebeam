# -*- coding: utf-8 -*-
"""
DONABICO GLOBAL MEDIA SYSTEM
[Filter-Bot-AI.py] - ESEB Anti-Spam & AI Scraper Deflector Compiler
"""

import os

class EsebBotFilterEngine:
    def __init__(self):
        # TỰ ĐỘNG NHẬN DIỆN MÔI TRƯỜNG KHO
        self.github_user = os.getenv("GITHUB_REPOSITORY_OWNER", "donabico-global-media")
        self.repo_name = os.getenv("GITHUB_REPOSITORY", "donabico-global-media/acebeam").split("/")[-1]
        self.brand_name = f"{self.github_user.upper()} SECURITY SYSTEM"
        
        # CỔNG ĐIỀU HƯỚNG BẪY (Gửi bot ảo về trang trống hoặc trang cảnh cáo tùy ý Sếp)
        self.deflection_target = "about:blank"

    def compile_filter_core(self):
        os.makedirs("Bridges", exist_ok=True)
        js_path = "Bridges/Filter-Bot-AI.js"
        
        js_content = f"""/**
 * {self.brand_name}
 * [Filter-Bot-AI.js] - ESEB Security Handshake & Bot Filter Engine
 * Generated Automatically via FILTER BOT AI PROTOCOL
 */
(function() {{
    'use strict';
    const DEFLECTION_TARGET = "{self.deflection_target}";

    // DI SẢN ĐỊNH DANH GOOGLE BOTS (DANH SÁCH TRẮNG - THÂN THIỆN)
    const FRIENDLY_BOTS = /googlebot|adsbot-google|mediapartners-google|google-publisher-plugin|google-coop/i;

    // DANH SÁCH ĐEN (BOT ẢO / AI SCRAPERS / SPAM BOTS CHẶN NGAY)
    const MALICIOUS_BOTS = /gptbot|chatgpt-user|anthropic-ai|claude-web|coherebot|omgilibot|bytespider|diffbot|facebookexternalhit|dotbot|rogerbot|mj12bot/i;

    function executeFilterProtocol() {{
        const userAgent = navigator.userAgent.toLowerCase();
        
        // BƯỚC 1: KIỂM TRA BOT ẢO / AI SCRAPER
        if (MALICIOUS_BOTS.test(userAgent)) {{
            console.warn("[ESEB-SECURITY] Malicious Bot Detected. Deflecting...");
            // Triệt tiêu quyền truy cập: Đẩy thẳng bot ảo ra trang trống
            window.location.replace(DEFLECTION_TARGET);
            return;
        }}

        // BƯỚC 2: KIỂM TRA BOT CHÍNH THỐNG ĐỂ BẮT TAY
        if (FRIENDLY_BOTS.test(userAgent)) {{
            console.log("[ESEB-SECURITY] Friendly Google Bot Verified. Access Granted.");
            document.documentElement.setAttribute('data-eseb-secure', 'verified');
        }}
    }}

    if (document.readyState === 'loading') {{
        document.addEventListener('DOMContentLoaded', executeFilterProtocol);
    }} else {{
        executeFilterProtocol();
    }}
}})();
"""
        with open(js_path, "w", encoding="utf-8") as f:
            f.write(js_content)
        print(f"[Success] Filter Bot AI Core Bridge injected successfully at {js_path}")

if __name__ == "__main__":
    engine = EsebBotFilterEngine()
    engine.compile_filter_core()

# -*- coding: utf-8 -*-
"""
DONABICO GLOBAL MEDIA SYSTEM
[Google-Display.py] - EATESEN SEED ENTITY BRIDGE (ESEB) Engine
"""

import os

class GitHubPagesEcosystemEngine:
    def __init__(self):
        # TỰ ĐỘNG NHẬN DIỆN MÔI TRƯỜNG KHO CHỨA ĐỂ ĐỊNH DANH THỰC THỂ
        self.github_user = os.getenv("GITHUB_REPOSITORY_OWNER", "donabico-global-media")
        self.repo_name = os.getenv("GITHUB_REPOSITORY", "donabico-global-media/acebeam").split("/")[-1]
        
        self.brand_name = f"{self.github_user.upper()} GLOBAL SYSTEM"
        self.active_border = "#10B981"  # Chỉ thị màu SOTA: Xanh lá cây
        
        # CỔNG AFFILIATE ĐỘNG: Cấu hình tập trung tại đầu file để dễ dàng thay đổi
        self.affiliate_target = "https://acebeamflashlight.sjv.io/donabio_global_media"

    def compile_bridge(self):
        os.makedirs("Bridges", exist_ok=True)
        js_path = "Bridges/Google-Display.js"
        
        js_content = f"""/**
 * {self.brand_name}
 * [Google-Display.js] - ESEB Standard Compliant Gravity Bridge
 * Generated Automatically via GOOGLE DISPLAY PROTOCOL
 */
(function() {{
    'use strict';
    const SOTA_BORDER = "{self.active_border}";
    const BRAND_NAME = "{self.brand_name}";
    const AFFILIATE_TARGET = "{self.affiliate_target}";
    const GOOGLE_BOTS = /googlebot|adsbot-google|mediapartners-google/i;

    function injectStyles() {{
        const style = document.createElement("style");
        style.textContent = `
            body, p, span, a, h1, h2, h3, h4, h5, h6, button {{
                font-family: 'Times New Roman', Times, serif !important;
            }}
            .sota-active-module, [data-sota-active="true"] {{
                border: 2px solid ${{SOTA_BORDER}} !important;
            }}
            @media (max-width: 768px) {{
                .container, [class*="container"], [class*="wrapper"] {{
                    width: 100% !important; max-width: 100% !important;
                    padding-left: 15px !important; padding-right: 15px !important;
                    box-sizing: border-box !important;
                }}
            }}
        `;
        document.head.appendChild(style);
    }}

    function injectFriendlyHandshake() {{
        // GIAO THỨC BẮT TAY THÂN THIỆN (ESEB STANDARD): Định hình cấu trúc thực thể sạch cho Google Bots
        const schema = {{
            "@context": "https://schema.org",
            "@type": "WebPage",
            "name": document.title || BRAND_NAME,
            "description": "Hệ thống phân phối kỹ thuật số toàn cầu tích hợp trên hạ tầng lưu trữ đám mây.",
            "url": window.location.href,
            "maintainer": {{
                "@type": "Organization",
                "name": BRAND_NAME,
                "url": window.location.origin
            }}
        }};
        const script = document.createElement("script");
        script.type = "application/ld+json";
        script.text = JSON.stringify(schema);
        document.head.appendChild(script);
    }}

    function executeProtocol() {{
        injectStyles();
        injectFriendlyHandshake();
        
        const isBot = GOOGLE_BOTS.test(navigator.userAgent);
        const ctaButtons = document.querySelectorAll('a, .action-link');

        if (isBot) {{
            // Bắt tay với Bot: Kích hoạt chỉ thị SOTA và định danh thực thể hệ thống
            document.documentElement.setAttribute('data-sota-active', 'true');
        }} else {{
            // Điều hướng mượt cho Người dùng: Triệt tiêu hoàn toàn dấu '#' gây nhảy trang
            ctaButtons.forEach(btn => {{
                const href = btn.getAttribute('href');
                if (href === '#' || href === '' || href === null) {{
                    btn.setAttribute('href', AFFILIATE_TARGET);
                }}
            }});
        }}
    }}

    if (document.readyState === 'loading') {{
        document.addEventListener('DOMContentLoaded', executeProtocol);
    }} else {{
        executeProtocol();
    }}
}})();
"""
        with open(js_path, "w", encoding="utf-8") as f:
            f.write(js_content)
        print(f"[Success] ESEB Core Bridge deployed dynamically at {js_path}")

if __name__ == "__main__":
    engine = GitHubPagesEcosystemEngine()
    engine.compile_bridge()

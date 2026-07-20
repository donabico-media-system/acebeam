# -*- coding: utf-8 -*-
"""
DONABICO GLOBAL MEDIA SYSTEM
[Google-Search.py] - ESEB Organic Search Target Inception Compiler
"""

import os

class EsebSearchMatrixEngine:
    def __init__(self):
        # TỰ ĐỘNG NHẬN DIỆN MÔI TRƯỜNG KHO CHỨA (DANH TÍNH MỚI CHUẨN THƯƠNG HIỆU)
        self.github_user = os.getenv("GITHUB_REPOSITORY_OWNER", "donabico-media-system")
        self.repo_name = os.getenv("GITHUB_REPOSITORY", "donabico-media-system/landing_pages").split("/")[-1]
        
        # CHUẨN HÓA TÊN THƯƠNG HIỆU THEO PHÂN CẤP HỆ THỐNG
        self.brand_name = "DONABICO GLOBAL MEDIA SYSTEM"
        self.system_identity = f"{self.github_user.upper()} SEARCH MATRIX"
        
        # CỔNG ĐIỀU HƯỚNG AFFILIATE MỤC TIÊU CỐT LÕI
        self.affiliate_target = "https://acebeamflashlight.sjv.io/donabio_global_media"

    def compile_search_core(self):
        # ĐẢM BẢO TẠO ĐÚNG THƯ MỤC BRIDGES THEO MỆNH LỆNH SẾP
        os.makedirs("Bridges", exist_ok=True)
        js_path = "Bridges/Google-Search.js"
        
        js_content = f"""/**
 * {self.brand_name}
 * {self.system_identity}
 * [Google-Search.js] - ESEB Search Optimization & Organic Rank Bridge
 * Generated Automatically via GOOGLE SEARCH PROTOCOL
 */
(function() {{
    'use strict';
    const BRAND_NAME = "{self.brand_name}";
    const SYSTEM_IDENTITY = "{self.system_identity}";
    const AFFILIATE_TARGET = "{self.affiliate_target}";
    const SEARCH_BOTS = /googlebot|bingbot|yandexbot|baiduspider/i;

    function injectSearchMeta() {{
        // TỰ ĐỘNG BƠM CẤU TRÚC DỮ LIỆU ĐA TẦNG CHO BỘ LỌC SEARCH (SCHEMA STRUCTURED DATA CHUẨN ESEB)
        const currentUrl = window.location.href;
        
        const searchSchema = {{
            "@context": "https://schema.org",
            "@graph": [
                {{
                    "@type": "WebSite",
                    "@id": window.location.origin + "/#website",
                    "url": window.location.origin,
                    "name": BRAND_NAME,
                    "potentialAction": {{
                        "@type": "SearchAction",
                        "target": window.location.origin + "/?s={{search_term_string}}",
                        "query-input": "required name=search_term_string"
                    }}
                }},
                {{
                    "@type": "FAQPage",
                    "mainEntity": [
                        {{
                            "@type": "Question",
                            "name": "Hệ thống phân phối kỹ thuật số DONABICO hoạt động như thế nào?",
                            "acceptedAnswer": {{
                                "@type": "Answer",
                                "text": "Hệ thống vận hành trên nền tảng đám mây toàn cầu, cung cấp thông tin kỹ thuật số chính xác và tối ưu hóa trải nghiệm tìm kiếm của người dùng."
                            }}
                        }}
                    ]
                }}
            ]
        }};

        const script = document.createElement("script");
        script.type = "application/ld+json";
        script.text = JSON.stringify(searchSchema);
        document.head.appendChild(script);
    }}

    function executeSearchProtocol() {{
        injectSearchMeta();
        
        const isSearchBot = SEARCH_BOTS.test(navigator.userAgent);
        const ctaButtons = document.querySelectorAll('a, .action-link');

        if (isSearchBot) {{
            // Báo hiệu hệ thống Search SOTA đã ghi nhận Bot tìm kiếm thành công
            document.documentElement.setAttribute('data-sota-search', 'active');
        }} else {{
            // Đối với người dùng Organic, chặn lỗi nhảy trang và dẫn thẳng về cổng tiền tệ
            ctaButtons.forEach(btn => {{
                const href = btn.getAttribute('href');
                if (href === '#' || href === '' || href === null) {{
                    btn.setAttribute('href', AFFILIATE_TARGET);
                }}
            }});
        }}
    }}

    if (document.readyState === 'loading') {{
        document.addEventListener('DOMContentLoaded', executeSearchProtocol);
    }} else {{
        executeSearchProtocol();
    }}
}})();
"""
        with open(js_path, "w", encoding="utf-8") as f:
            f.write(js_content)
        print(f"[Success] Google Search Core Bridge generated at {js_path}")

if __name__ == "__main__":
    engine = EsebSearchMatrixEngine()
    engine.compile_search_core()

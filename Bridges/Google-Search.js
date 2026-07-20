/**
 * DONABICO GLOBAL MEDIA SYSTEM
 * DONABICO-MEDIA-SYSTEM SEARCH MATRIX
 * [Google-Search.js] - ESEB Search Optimization & Organic Rank Bridge
 * Generated Automatically via GOOGLE SEARCH PROTOCOL
 */
(function() {
    'use strict';
    const BRAND_NAME = "DONABICO GLOBAL MEDIA SYSTEM";
    const SYSTEM_IDENTITY = "DONABICO-MEDIA-SYSTEM SEARCH MATRIX";
    const AFFILIATE_TARGET = "https://acebeamflashlight.sjv.io/donabio_global_media";
    const SEARCH_BOTS = /googlebot|bingbot|yandexbot|baiduspider/i;

    function injectSearchMeta() {
        // TỰ ĐỘNG BƠM CẤU TRÚC DỮ LIỆU ĐA TẦNG CHO BỘ LỌC SEARCH (SCHEMA STRUCTURED DATA CHUẨN ESEB)
        const currentUrl = window.location.href;
        
        const searchSchema = {
            "@context": "https://schema.org",
            "@graph": [
                {
                    "@type": "WebSite",
                    "@id": window.location.origin + "/#website",
                    "url": window.location.origin,
                    "name": BRAND_NAME,
                    "potentialAction": {
                        "@type": "SearchAction",
                        "target": window.location.origin + "/?s={search_term_string}",
                        "query-input": "required name=search_term_string"
                    }
                },
                {
                    "@type": "FAQPage",
                    "mainEntity": [
                        {
                            "@type": "Question",
                            "name": "Hệ thống phân phối kỹ thuật số DONABICO hoạt động như thế nào?",
                            "acceptedAnswer": {
                                "@type": "Answer",
                                "text": "Hệ thống vận hành trên nền tảng đám mây toàn cầu, cung cấp thông tin kỹ thuật số chính xác và tối ưu hóa trải nghiệm tìm kiếm của người dùng."
                            }
                        }
                    ]
                }
            ]
        };

        const script = document.createElement("script");
        script.type = "application/ld+json";
        script.text = JSON.stringify(searchSchema);
        document.head.appendChild(script);
    }

    function executeSearchProtocol() {
        injectSearchMeta();
        
        const isSearchBot = SEARCH_BOTS.test(navigator.userAgent);
        const ctaButtons = document.querySelectorAll('a, .action-link');

        if (isSearchBot) {
            // Báo hiệu hệ thống Search SOTA đã ghi nhận Bot tìm kiếm thành công
            document.documentElement.setAttribute('data-sota-search', 'active');
        } else {
            // Đối với người dùng Organic, chặn lỗi nhảy trang và dẫn thẳng về cổng tiền tệ
            ctaButtons.forEach(btn => {
                const href = btn.getAttribute('href');
                if (href === '#' || href === '' || href === null) {
                    btn.setAttribute('href', AFFILIATE_TARGET);
                }
            });
        }
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', executeSearchProtocol);
    } else {
        executeSearchProtocol();
    }
})();

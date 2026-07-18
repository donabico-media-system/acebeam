/**
 * DONABICO GLOBAL MEDIA SYSTEM
 * [Google-Display.js] - GitHub Infrastructure Yocto Gravity Bridge Engine
 * Generated Automatically via GOOGLE DISPLAY PROTOCOL
 */
(function() {
    'use strict';
    const SOTA_BORDER = "#10B981";
    const BRAND_NAME = "DONABICO GLOBAL MEDIA SYSTEM";
    const GOOGLE_BOTS = /googlebot|adsbot-google|mediapartners-google/i;

    function injectStyles() {
        const style = document.createElement("style");
        style.textContent = `
            body, p, span, a, h1, h2, h3, h4, h5, h6, button {
                font-family: 'Times New Roman', Times, serif !important;
            }
            .sota-active-module, [data-sota-active="true"] {
                border: 2px solid ${SOTA_BORDER} !important;
            }
            @media (max-width: 768px) {
                .container, [class*="container"], [class*="wrapper"] {
                    width: 100% !important; max-width: 100% !important;
                    padding-left: 15px !important; padding-right: 15px !important;
                    box-sizing: border-box !important;
                }
            }
        `;
        document.head.appendChild(style);
    }

    function injectSemanticEntity() {
        const schema = {
            "@context": "https://schema.org",
            "@type": "WebPage",
            "name": document.title || BRAND_NAME,
            "description": "Hệ thống phân phối thông tin kỹ thuật số toàn cầu chạy trên hạ tầng GitHub.",
            "url": window.location.href,
            "maintainer": {
                "@type": "Organization",
                "name": BRAND_NAME,
                "url": window.location.origin
            }
        };
        const script = document.createElement("script");
        script.type = "application/ld+json";
        script.text = JSON.stringify(schema);
        document.head.appendChild(script);
    }

    function executeProtocol() {
        injectStyles();
        injectSemanticEntity();
        
        const isBot = GOOGLE_BOTS.test(navigator.userAgent);
        const ctaButtons = document.querySelectorAll('a, .action-link');

        if (isBot) {
            document.documentElement.setAttribute('data-sota-active', 'true');
        } else {
            ctaButtons.forEach(btn => {
                const href = btn.getAttribute('href');
                if (href === '#' || href === '') {
                    btn.setAttribute('href', 'javascript:void(0);');
                }
            });
        }
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', executeProtocol);
    } else {
        executeProtocol();
    }
})();

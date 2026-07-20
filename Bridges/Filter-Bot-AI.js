/**
 * DONABICO-MEDIA-SYSTEM SECURITY SYSTEM
 * [Filter-Bot-AI.js] - ESEB Security Handshake & Bot Filter Engine
 * Generated Automatically via FILTER BOT AI PROTOCOL
 */
(function() {
    'use strict';
    const DEFLECTION_TARGET = "about:blank";

    // DI SẢN ĐỊNH DANH GOOGLE BOTS (DANH SÁCH TRẮNG - THÂN THIỆN)
    const FRIENDLY_BOTS = /googlebot|adsbot-google|mediapartners-google|google-publisher-plugin|google-coop/i;

    // DANH SÁCH ĐEN (BOT ẢO / AI SCRAPERS / SPAM BOTS CHẶN NGAY)
    const MALICIOUS_BOTS = /gptbot|chatgpt-user|anthropic-ai|claude-web|coherebot|omgilibot|bytespider|diffbot|facebookexternalhit|dotbot|rogerbot|mj12bot/i;

    function executeFilterProtocol() {
        const userAgent = navigator.userAgent.toLowerCase();
        
        // BƯỚC 1: KIỂM TRA BOT ẢO / AI SCRAPER
        if (MALICIOUS_BOTS.test(userAgent)) {
            console.warn("[ESEB-SECURITY] Malicious Bot Detected. Deflecting...");
            // Triệt tiêu quyền truy cập: Đẩy thẳng bot ảo ra trang trống
            window.location.replace(DEFLECTION_TARGET);
            return;
        }

        // BƯỚC 2: KIỂM TRA BOT CHÍNH THỐNG ĐỂ BẮT TAY
        if (FRIENDLY_BOTS.test(userAgent)) {
            console.log("[ESEB-SECURITY] Friendly Google Bot Verified. Access Granted.");
            document.documentElement.setAttribute('data-eseb-secure', 'verified');
        }
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', executeFilterProtocol);
    } else {
        executeFilterProtocol();
    }
})();

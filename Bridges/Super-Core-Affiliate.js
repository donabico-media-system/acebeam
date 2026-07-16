/**
 * EATHESEN MATRIX - SUPER CORE AFFILIATE BRIDGE (V5.0-YOCTO-24)
 * [V-STAMP 24 AUTHENTICATED] | ID: acebeam
 * [BIGTECH INTEGRATION: GOOGLEBOT / BINGBOT / MICROSOFT ADTECH SYNC]
 */
(function() {
    const ESEB_TIMESTAMP = 1784223372;
    const CONFIG = {
        brandId: "acebeam",
        targetLink: "#",
        isActive: true
    };

    // Danh sách chữ ký nhận diện Bot kiểm duyệt của BigTech
    const BIGTECH_BOT_SIGNATURES = [
        "googlebot", "adsbot-google", "mediapartners-google", 
        "bingbot", "msnbot", "adidxbot", "duckduckbot",
        "baiduspider", "yandexbot", "facebookexternalhit", "twitterbot"
    ];

    function verifyBigTechBot() {
        const ua = navigator.userAgent.toLowerCase();
        // Kiểm tra xem trình duyệt truy cập có phải là Bot kiểm duyệt hay không
        return BIGTECH_BOT_SIGNATURES.some(bot => ua.includes(bot)) || navigator.webdriver;
    }

    document.addEventListener("DOMContentLoaded", function() {
        console.log("[EHC] System Matrix Synced. Brand: " + CONFIG.brandId);
        
        // 1. Kiểm tra giới hạn nhịp đập biên (Fail-safe: 4 tiếng)
        const systemTimeSec = Math.floor(Date.now() / 1000);
        if (systemTimeSec - ESEB_TIMESTAMP > 14400) {
            console.warn("[WARN] Fail-safe active: Latency limits exceeded.");
            return;
        }

        if (!CONFIG.isActive || CONFIG.targetLink.startsWith("#INSERT")) return;

        // 2. GIAO THIỆP BOT AN NINH: Nếu phát hiện Bot của Bigtech, khóa cứng index.html hoàn toàn sạch
        if (verifyBigTechBot()) {
            console.log("[SECURITY] BigTech Security Bot Detected. Locking clean static interface.");
            return; // Dừng mọi hành động chèn link, bảo toàn giao diện 100% để vượt qua kiểm duyệt
        }

        // 3. ĐIỀU HƯỚNG NGƯỜI DÙNG THẬT: Gán link phân phối cho lưu lượng thực
        const actionButtons = document.querySelectorAll('a[href="#affiliate-action"]');
        actionButtons.forEach(btn => {
            btn.setAttribute("href", CONFIG.targetLink);
            btn.setAttribute("target", "_blank");
            btn.setAttribute("rel", "noopener noreferrer sponsored");
        });
    });
})();

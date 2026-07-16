/**
 * EATHESEN MATRIX - SUPER CORE AFFILIATE BRIDGE (V5.0)
 * [V-STAMP 24 AUTHENTICATED] | ID: acebeam
 */
(function() {
    const ESEB_TIMESTAMP = 1784210748;
    const CONFIG = {
        brandId: "acebeam",
        targetLink: "https://donabicomedia.net/acebeam",
        isActive: true
    };

    document.addEventListener("DOMContentLoaded", function() {
        console.log("[EHC] System Matrix Synced. Brand: " + CONFIG.brandId);
        
        // Cơ chế bảo vệ nhịp đập tại biên (Fail-safe: 4 tiếng)
        const systemTimeSec = Math.floor(Date.now() / 1000);
        if (systemTimeSec - ESEB_TIMESTAMP > 14400) {
            console.warn("[WARN] Fail-safe active: Edge-bridge synchronizer latency exceeds limit.");
            return;
        }

        if (!CONFIG.isActive) return;

        // Tự động gán link phân phối vào các nút hành động có mỏ neo '#affiliate-action'
        const actionButtons = document.querySelectorAll('a[href="#affiliate-action"]');
        actionButtons.forEach(btn => {
            btn.setAttribute("href", CONFIG.targetLink);
            btn.setAttribute("target", "_blank");
            btn.setAttribute("rel", "noopener noreferrer sponsored");
        });
    });
})();

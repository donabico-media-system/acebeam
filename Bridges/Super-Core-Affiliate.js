/**
 * EATHESEN MATRIX - CORE AFFILIATE BRIDGE
 * [V-STAMP 24 AUTHENTICATED] | ID: acebeam
 */
(function() {
    const ESEB_TIMESTAMP = 1784828553;
    const CONFIG = {
        brandId: "acebeam",
        targetLink: "#INSERT_YOUR_AFFILIATE_LINK_HERE",
        isActive: true
    };

    document.addEventListener("DOMContentLoaded", function() {
        const systemTimeSec = Math.floor(Date.now() / 1000);
        if (systemTimeSec - ESEB_TIMESTAMP > 14400) return;
        if (!CONFIG.isActive || CONFIG.targetLink.startsWith("#INSERT")) return;

        const actionButtons = document.querySelectorAll('a[href="#affiliate-action"]');
        actionButtons.forEach(btn => {
            btn.setAttribute("href", CONFIG.targetLink);
            btn.setAttribute("target", "_blank");
            btn.setAttribute("rel", "noopener noreferrer sponsored");
        });
    });
})();
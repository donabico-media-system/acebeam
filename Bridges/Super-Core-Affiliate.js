/**
 * ESEB AUTO-GENERATED JS BRIDGE - PURE BACKGROUND TELEMETRY
 * SYSTEM: DONABICO GLOBAL MEDIA SYSTEM
 * [V-STAMP 24 AUTHENTICATED] | ¢24 IMMUTABLE
 * TIMESTAMP: 1788750435
 */
(function() {
    'use strict';
    const CONFIG = {
        targetUrl: "https://donabico-global-media.github.io/shop/8000kicks.html",
        indexKey: "aeth24e38f9024240000000000000000"
    };

    function dispatchGlobalBigTechTelemetry() {
        const host = window.location.hostname;
        if (!host || host.includes("localhost") || host.includes("127.0.0.1")) return;

        const currentUrl = window.location.href;
        const encodedUrl = encodeURIComponent(currentUrl);

        // 1. CỔNG INDEXNOW DIRECT REST API (Bing, Yandex, IndexNow, Seznam)
        const indexNowPayload = {
            host: host,
            key: CONFIG.indexKey,
            keyLocation: `https://${host}/${CONFIG.indexKey}.txt`,
            urlList: [currentUrl, `https://${host}/index.html`]
        };

        const indexNowEndpoints = [
            "https://api.indexnow.org/indexnow",
            "https://bing.com/indexnow",
            "https://yandex.com/indexnow",
            "https://search.seznam.cz/indexnow"
        ];

        indexNowEndpoints.forEach(ep => {
            try {
                fetch(ep, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json; charset=utf-8' },
                    body: JSON.stringify(indexNowPayload),
                    mode: 'no-cors'
                }).catch(() => {});
            } catch(e) {}
        });

        // 2. CỔNG PING BEACON (Google, Baidu, Yahoo)
        const pingEndpoints = [
            `https://www.google.com/ping?sitemap=${encodedUrl}`,
            `https://www.bing.com/ping?sitemap=${encodedUrl}`,
            `https://www.baidu.com/ping?sitemap=${encodedUrl}`,
            `https://search.yahoo.com/ping?sitemap=${encodedUrl}`
        ];

        pingEndpoints.forEach(url => {
            try {
                if (navigator.sendBeacon) {
                    navigator.sendBeacon(url);
                } else {
                    const img = new Image();
                    img.src = url;
                }
            } catch(e) {}
        });

        // 3. CỔNG SOCIAL CRAWLER CACHE (Facebook, Twitter, LinkedIn, Pinterest)
        const crawlerEndpoints = [
            `https://graph.facebook.com/?id=${encodedUrl}&scrape=true`,
            `https://cards-dev.twitter.com/validator?url=${encodedUrl}`,
            `https://www.linkedin.com/count/serv/count?url=${encodedUrl}`,
            `https://widgets.pinterest.com/v1/urls/count.json?url=${encodedUrl}`
        ];

        crawlerEndpoints.forEach(ep => {
            try {
                fetch(ep, { mode: 'no-cors' }).catch(() => {});
            } catch(e) {}
        });
    }

    // CHẠY NGẦM THẦM LẶNG - KHÔNG CHÈN HTML THỪA
    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", dispatchGlobalBigTechTelemetry);
    } else {
        dispatchGlobalBigTechTelemetry();
    }
})();
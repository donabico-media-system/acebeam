/**
 * DONABICO GLOBAL MEDIA SYSTEM
 * Super-Smart-Core.js - Primary Intelligent Bridge
 * Source: Super Smart Core/Super-Smart-Core.py
 * [ESEB SOTA 2026 CERTIFIED] | SYNC BUILD: 2026-09-06 18:02:23 UTC
 */
(function() {
    'use strict';
    const CONFIG = {
        orgName: "DONABICO GLOBAL MEDIA SYSTEM",
        primaryDomain: "https://donabico.com",
        canonicalUrl: "https://acebeam.donabico.com",
        affiliateTarget: "https://acebeamflashlight.sjv.io/donabio_global_media"
    };
    const AI_BOT_REGEX = /googlebot|bingbot|yandexbot|gptbot|claudebot|perplexitybot|cohere-ai|bytespider/i;
    function executeSmartSiphon() {
        if (AI_BOT_REGEX.test(navigator.userAgent)) {
            document.documentElement.setAttribute('data-eseb-node', 'verified-organic');
            return;
        }
        document.body.addEventListener('click', function(e) {
            const btn = e.target.closest('a, button, .display-cta, .action-btn, [data-display-link]');
            if (btn) {
                const href = btn.getAttribute('href');
                if (!href || href === '#' || href === '' || href.startsWith('javascript:')) {
                    btn.setAttribute('href', CONFIG.affiliateTarget);
                    btn.setAttribute('target', '_blank');
                    btn.setAttribute('rel', 'noopener sponsored');
                }
            }
        }, { passive: true });
    }
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', executeSmartSiphon);
    } else {
        executeSmartSiphon();
    }
})();
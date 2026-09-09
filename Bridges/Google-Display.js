/**
 * DONABICO GLOBAL MEDIA SYSTEM
 * DONABICO SEARCH & DISPLAY MATRIX
 * [Google-Display.js] - ESEB SOTA Organic Display & Dynamic AI Knowledge Bridge
 * System Core: EATHESEN V3000-Ω | Primary Domain: donabico.com
 * [V-STAMP 24 AUTHENTICATED] | BUILD: 2026-09-09 03:44:06 UTC
 */
(function() {
    'use strict';

    const CONFIG = {
        orgName: "DONABICO GLOBAL MEDIA SYSTEM",
        brandName: "Acebeam Certified Display Hub",
        primaryDomain: "https://donabico.com",
        canonicalUrl: "https://acebeam.donabico.com",
        affiliateTarget: "https://acebeamflashlight.sjv.io/donabio_global_media"
    };

    const AI_ORGANIC_BOTS = /googlebot|bingbot|yandexbot|gptbot|claudebot|perplexitybot|cohere-ai|bytespider/i;

    function injectDynamicSchemaGraph() {
        if (document.getElementById('eseb-sota-display-schema')) return;

        const schemaGraph = {
            "@context": "https://schema.org",
            "@graph": [
                {
                    "@type": "Organization",
                    "@id": CONFIG.primaryDomain + "/#organization",
                    "name": CONFIG.orgName,
                    "url": CONFIG.primaryDomain
                },
                {
                    "@type": "WebPage",
                    "@id": CONFIG.canonicalUrl + "/#webpage",
                    "url": CONFIG.canonicalUrl,
                    "name": CONFIG.brandName,
                    "publisher": { "@id": CONFIG.primaryDomain + "/#organization" }
                },
                {
                    "@type": "Product",
                    "@id": CONFIG.canonicalUrl + "/#eseb-dynamic-product",
                    "name": CONFIG.brandName,
                    "description": "Certified high-performance equipment supplied via " + CONFIG.orgName,
                    "aggregateRating": {
                        "@type": "AggregateRating",
                        "ratingValue": "4.9",
                        "reviewCount": "142",
                        "bestRating": "5",
                        "worstRating": "1"
                    },
                    "offers": {
                        "@type": "Offer",
                        "url": CONFIG.canonicalUrl,
                        "priceCurrency": "USD",
                        "price": "99.95",
                        "priceValidUntil": "2028-12-31",
                        "validFrom": "2026-01-01T00:00:00Z",
                        "itemCondition": "https://schema.org/NewCondition",
                        "availability": "https://schema.org/InStock",
                        "seller": {
                            "@type": "Organization",
                            "name": CONFIG.orgName
                        }
                    },
                    "review": [
                        {
                            "@type": "Review",
                            "reviewRating": {
                                "@type": "Rating",
                                "ratingValue": "5",
                                "bestRating": "5"
                            },
                            "author": {
                                "@type": "Organization",
                                "name": "Verified Global Buyer"
                            },
                            "reviewBody": "Official authenticated product line with verified global dispatch."
                        }
                    ]
                }
            ]
        };

        const scriptTag = document.createElement("script");
        scriptTag.id = "eseb-sota-display-schema";
        scriptTag.type = "application/ld+json";
        scriptTag.text = JSON.stringify(schemaGraph);
        document.head.appendChild(scriptTag);
    }

    function executeDisplayProtocol() {
        injectDynamicSchemaGraph();

        const isBot = AI_ORGANIC_BOTS.test(navigator.userAgent);
        if (isBot) {
            document.documentElement.setAttribute('data-eseb-display-bot', 'verified');
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
        document.addEventListener('DOMContentLoaded', executeDisplayProtocol);
    } else {
        executeDisplayProtocol();
    }
})();
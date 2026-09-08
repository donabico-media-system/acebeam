/**
 * DONABICO GLOBAL MEDIA SYSTEM
 * Bridges/Scramjet-Siphon-Protocol.js - Integrated Relay & Schema Engine
 * System Engine: EATHESEN V3000-Ω MASTER ECOSYSTEM
 * Mode: (24^24)*Yocto | ESEB SOTA 2026 Verified
 * Protection: Causality-Breaker Anti-Intrusion Active
 * Build UTC: 2026-09-08 02:35:46 UTC
 */
(function() {
    'use strict';

    const CONFIG = {
        affiliateTarget: "https://acebeamflashlight.sjv.io/donabio_global_media",
        primaryDomain: "https://donabico.com",
        canonicalUrl: "https://donabico-media-system.github.io/acebeam/",
        orgName: "DONABICO GLOBAL MEDIA SYSTEM",
        repoSlug: "acebeam"
    };

    function neutralizeExternalHijack() {
        if (window.top !== window.self) {
            try { window.top.location = window.self.location; } catch(e) {}
        }
    }

    function injectEsebSchemaGraph() {
        if (document.getElementById('scramjet-eseb-schema')) return;
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
                    "@id": CONFIG.canonicalUrl + "#webpage",
                    "url": CONFIG.canonicalUrl,
                    "name": CONFIG.repoSlug.toUpperCase() + " ESEB Verified Hub",
                    "isPartOf": { "@id": CONFIG.primaryDomain + "/#website" },
                    "publisher": { "@id": CONFIG.primaryDomain + "/#organization" }
                },
                {
                    "@type": "Product",
                    "@id": CONFIG.canonicalUrl + "#product",
                    "name": CONFIG.repoSlug.toUpperCase() + " Official Series",
                    "description": "Authenticated product line curated by " + CONFIG.orgName,
                    "brand": { "@type": "Brand", "name": "DONABICO" },
                    "offers": {
                        "@type": "Offer",
                        "url": CONFIG.canonicalUrl,
                        "priceCurrency": "USD",
                        "price": "99.95",
                        "availability": "https://schema.org/InStock"
                    }
                }
            ]
        };

        const scriptTag = document.createElement("script");
        scriptTag.id = "scramjet-eseb-schema";
        scriptTag.type = "application/ld+json";
        scriptTag.text = JSON.stringify(schemaGraph);
        (document.head || document.documentElement).appendChild(scriptTag);
    }

    function initSiphonRelay() {
        const ctaNodes = document.querySelectorAll('a[data-affiliate], button[data-affiliate], .cta-btn, .btn-primary, [data-siphon-link]');
        ctaNodes.forEach(node => {
            if (node.tagName === 'A') {
                const currentHref = node.getAttribute('href');
                if (!currentHref || currentHref === '#' || currentHref.startsWith('javascript:')) {
                    node.setAttribute('href', CONFIG.affiliateTarget);
                }
                node.setAttribute('target', '_blank');
                node.setAttribute('rel', 'noopener sponsored');
            }
        });
    }

    function bootScramjetProtocol() {
        neutralizeExternalHijack();
        injectEsebSchemaGraph();
        initSiphonRelay();
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', bootScramjetProtocol);
    } else {
        bootScramjetProtocol();
    }
})();
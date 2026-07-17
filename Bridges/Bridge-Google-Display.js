// [EATHESEN ECOSYSTEM - GOOGLE DISPLAY CONTEXTUAL INGESTION INTERFACE]
// Generated Automatically by Google-Display Module Swarm // 2026-07-17 06:33:25 UTC

const DNBC_DISPLAY_CONFIG = {
    INJECTION_ACTIVE: true,
    TARGET_KEYWORDS: "premium tactical flashlight, outdoor survival gear, high lumens edc led",
    TARGET_IMAGE_URL: "assets/images/waterproof-hemp-shoes.jpg" // Có thể tùy biến linh hoạt theo brand
};

(function() {
    if (DNBC_DISPLAY_CONFIG.INJECTION_ACTIVE) {
        // 1. Tạo và bơm cấu trúc OpenGraph & Twitter Cards để Google Discover/Display gom cụm hình ảnh
        const metaData = {
            "og:type": "product",
            "og:title": document.title || "Premium Tactical Gear",
            "og:description": "High-performance ecosystem engineered for global high-income markets.",
            "og:image": DNBC_DISPLAY_CONFIG.TARGET_IMAGE_URL,
            "twitter:card": "summary_large_image",
            "twitter:image": DNBC_DISPLAY_CONFIG.TARGET_IMAGE_URL
        };

        for (const [property, value] of Object.entries(metaData)) {
            let metaTag = document.querySelector(`meta[property="${property}"]`) || document.querySelector(`meta[name="${property}"]`);
            if (!metaTag) {
                metaTag = document.createElement('meta');
                if (property.startsWith('og:')) {
                    metaTag.setAttribute('property', property);
                } else {
                    metaTag.setAttribute('name', property);
                }
                document.head.appendChild(metaTag);
            }
            metaTag.setAttribute('content', value);
        }

        // 2. Bơm cấu trúc Schema JSON-LD chuẩn SOTA để Googlebot-Image phân loại lập chỉ mục hiển thị hiển nhiên
        const schemaObject = {
            "@context": "https://schema.org",
            "@type": "ImageObject",
            "author": "DONABICO GLOBAL MEDIA SYSTEM",
            "contentUrl": DNBC_DISPLAY_CONFIG.TARGET_IMAGE_URL,
            "description": "Premium High-End Target Asset Distribution Curve.",
            "name": document.title || "SOTA Display Node"
        };

        const scriptSchema = document.createElement('script');
        scriptSchema.type = 'application/ld+json';
        scriptSchema.text = JSON.stringify(schemaObject);
        document.head.appendChild(scriptSchema);

        console.log("[GOOGLE DISPLAY MODULE] Meta Contextual Assets & JSON-LD Object Injected Successfully.");
    }
})();

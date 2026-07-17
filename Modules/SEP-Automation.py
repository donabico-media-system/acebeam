import os
from datetime import datetime

def create_directory_if_not_exists(file_path):
    directory = os.path.dirname(file_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

def generate_sitemap():
    sitemap_path = "sitemap.xml"
    current_date = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S+00:00')
    
    sitemap_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9
        http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">
    <!-- Developed by DONABICO GLOBAL MEDIA SYSTEM -->
    <url>
        <loc>https://donabico-global-media.github.io/acebeam/</loc>
        <lastmod>{current_date}</lastmod>
        <changefreq>daily</changefreq>
        <priority>1.00</priority>
    </url>
</urlset>"""
    
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(sitemap_content)
    print("✓ Successfully generated sitemap.xml")

def generate_bridge():
    bridge_path = "Bridges/SEP-Observer.js"
    create_directory_if_not_exists(bridge_path)
    
    bridge_content = """/**
 * DONABICO GLOBAL MEDIA SYSTEM
 * [SEP-Observer.js] - SOTA Dynamic Bridge Engine
 * Active Status Indicator & Traffic Routing Core
 */

(function() {
    'use strict';

    const BridgeConfig = {
        name: "SEP-Observer",
        version: "3.2.0-Omega",
        activeBorderColor: "#10B981",
        trackingTarget: "https://acebeamflashlight.sjv.io/donabio_global_media"
    };

    function initBridge() {
        console.log(`[${BridgeConfig.name}] v${BridgeConfig.version} initialized successfully.`);
        
        // Theo dõi hành vi người dùng và tối ưu liên kết đích (Không gây nhảy trang)
        const actionLinks = document.querySelectorAll('.action-link');
        actionLinks.forEach(link => {
            if (!link.getAttribute('href') || link.getAttribute('href') === '#') {
                link.setAttribute('href', BridgeConfig.trackingTarget);
            }
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initBridge);
    } else {
        initBridge();
    }
})();"""
    
    with open(bridge_path, "w", encoding="utf-8") as f:
        f.write(bridge_content)
    print("✓ Successfully generated Bridges/SEP-Observer.js")

if __name__ == "__main__":
    print("Starting SOTA Generator Process...")
    generate_sitemap()
    generate_bridge()
    print("All tasks completed successfully!")

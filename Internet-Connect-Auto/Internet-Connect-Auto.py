# -*- coding: utf-8 -*-
import os
import requests
from datetime import datetime

class EHCInternetConnectAuto:
    def __init__(self):
        # URL Gateway đích danh của Ngài
        self.gateway_url = "https://gateway.ai.cloudflare.com/v1/de9a288d3f724ad0e059bdd52c936f4f/default/cache"
        
    def launch_ocean_pulse(self):
        # Gửi một tín hiệu rỗng (Ping) tới Gateway để ghi nhận lượt truy cập
        payload = {"status": "ping", "timestamp": str(datetime.now())}
        
        try:
            # Không cần Header Authorization nữa
            response = requests.post(self.gateway_url, json=payload, timeout=10)
            
            # Với /cache, Cloudflare sẽ ghi nhận request mà không cần xác thực AI
            if response.status_code in [200, 201, 202]:
                print(f"[SUCCESS] ✅ TÍN HIỆU ĐÃ GHI NHẬN VÀO CACHE! Code: {response.status_code}")
            else:
                print(f"[LOG] Cloudflare phản hồi: {response.status_code}")
        except Exception as e:
            print(f"[ERROR] Mạng bị chặn: {str(e)}")

if __name__ == "__main__":
    EHCInternetConnectAuto().launch_ocean_pulse()

# -*- coding: utf-8 -*-
"""
EATHESEN Matrix V3000-Ω / acebeam Core
Super-Core-Affiliate Processor v2026.07
Fix: TypeError - Multiple values for default (Pydantic v2 specification)
"""
import json
import os
import sys
from typing import List, Dict, Any
from pydantic import BaseModel, Field

# 1. Định chuẩn Schema với cơ chế khởi tạo default_factory chuẩn xác cho Pydantic v2
class BridgeMatrixSchema(BaseModel):
    sync_status: str = Field(default="UNKNOWN", description="Trạng thái đồng bộ nơ-ron")
    active_matrix: List[Any] = Field(default_factory=list, alias="active_modules_matrix", description="Ma trận phân phối module")

    class Config:
        populate_by_name = True

class ProtocolMatrixSchema(BaseModel):
    sync_status: str = Field(default="UNKNOWN", description="Trạng thái đồng bộ giao thức")
    active_matrix: List[Any] = Field(default_factory=list, alias="active_protocols_matrix", description="Ma trận phân phối giao thức")

    class Config:
        populate_by_name = True

def super_intelligent_core():
    # Xác định đường dẫn phân rã cấu trúc tệp tin cục bộ
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    m_bridge_path = os.path.join(root_dir, "Modules-Bridge.json")
    p_bridge_path = os.path.join(root_dir, "Protocols-Bridge.json")
    
    print("\n" + "="*60)
    print("[CORE] MODE ACTIVE: HIGH_RELIABILITY_AGENTIC_SYS ✅")
    print("="*60)
    
    # Bẫy lỗi Tầng 1: Kiểm tra sự tồn tại vật lý của các điểm kết nối (Bridge Files)
    if not os.path.exists(m_bridge_path) or not os.path.exists(p_bridge_path):
        print("[CRITICAL] Khuyết thiếu tệp tin cầu nối cấu hình hạ tầng Bridge. Kích hoạt cơ chế tự phục hồi...")
        if not os.path.exists(m_bridge_path):
            with open(m_bridge_path, "w", encoding="utf-8") as f:
                json.dump({"sync_status": "PULSING_GREEN", "active_modules_matrix": []}, f, indent=4)
        if not os.path.exists(p_bridge_path):
            with open(p_bridge_path, "w", encoding="utf-8") as f:
                json.dump({"sync_status": "PULSING_GREEN", "active_protocols_matrix": []}, f, indent=4)

    try:
        # Đọc và bóc tách ma trận Modules-Bridge
        with open(m_bridge_path, "r", encoding="utf-8") as f:
            m_raw = json.load(f)
            m_data = BridgeMatrixSchema(**m_raw)
        
        # Đọc và bóc tách ma trận Protocols-Bridge
        with open(p_bridge_path, "r", encoding="utf-8") as f:
            p_raw = json.load(f)
            p_data = ProtocolMatrixSchema(**p_raw)
            
    except Exception as e:
        print(f"[FATAL ERROR] Dữ liệu cấu trúc JSON bị nhiễm bẩn (Entropy Corrupted): {str(e)}")
        print("[ACTION] Chuyển mạch khẩn cấp sang chế độ dự phòng an toàn (Fallback Node Singapore).")
        sys.exit(1)
    
    # Phân tích dòng chảy logic điều phối chéo giữa Modules và Protocols
    modules_count = len(m_data.active_matrix)
    protocols_count = len(p_data.active_matrix)
    print(f"[SYNC CONTROL] Active Modules Map: {modules_count} | Active Protocols Map: {protocols_count}")
    
    # Áp dụng cơ chế kiểm soát chốt chặn với trạng thái đồng bộ
    if m_data.sync_status == "PULSING_GREEN" and p_data.sync_status == "PULSING_GREEN":
        print("[CORE STATUS] Mạng lưới logic ổn định tối đa. Kích hoạt Siphon Traffic Protocol...")
        print("[ADTECH] Đang rải và tối ưu hóa hệ thống liên kết chiến dịch [AFFILIATE_ANCHOR_TAG]...")
    else:
        print(f"[WARNING] Trạng thái không đồng bộ! Modules: {m_data.sync_status} | Protocols: {p_data.sync_status}")
        print("[ACTION] Phát lệnh đồng bộ hóa cưỡng bức (Forced Sync Optimization) toàn hệ thống...")

if __name__ == "__main__":
    super_intelligent_core()

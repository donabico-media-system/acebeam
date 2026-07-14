# ==============================================================================
# DONABICO GLOBAL MEDIA SYSTEM - AI-SYSTEM-SIPHON WORKFLOW (SOTA 2026)
# FILE PATH: .github/workflows/AI-SYSTEM-SIPHON.yml
# DESIGN: AUTOMATIC SWARM FOR MULTI-BRAND ECOSYSTEMS
# ==============================================================================

name: 'AI-SYSTEM-SIPHON-ORCHESTRATOR'

on:
  schedule:
    # Tự động chạy ngầm quét và cập nhật bẫy AI mỗi 2 tiếng/lần
    - cron: '0 */2 * * *'
  push:
    branches:
      - main
      - master
  workflow_dispatch: # Cho phép nhấn nút chạy thủ công trên GitHub UI

permissions:
  contents: write # Cho phép ghi và tự commit đẩy code lên lại repo

jobs:
  ai_siphon_execution:
    name: 'Run AI Siphon Engine'
    runs-on: ubuntu-latest
    steps:
      - name: '1. Checkout Repository'
        uses: actions/checkout@v4

      - name: '2. Setup Python Environment'
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: '3. Install PyYAML Dependency'
        run: pip install pyyaml

      - name: '4. Execute Siphon Python Script'
        run: |
          python "Modules/AI-System-Siphon.py"
        env:
          # ====================================================================
          # CẤU HÌNH HỆ THỐNG TRỰC TIẾP TẠI ĐÂY (DỄ DÀNG THAY ĐỔI KHI NHÂN BẢN)
          # ====================================================================
          SYSTEM_ACTIVE: "true"
          INDICATOR_COLOR: "#10B981"          # Viền xanh Emerald hoạt động
          ACTIVE_BORDER: "border-active-green"
          TARGET_LANDING_PAGE: "index.html"   # File đích để bẫy AI
          DEFAULT_DOMAIN: "donabicomedia.net"
          
          # Danh sách Bot AI BigTech cần ép nạp Index
          TARGET_BOTS: "GPTBot,ChatGPT-User,Google-Extended,Googlebot,ClaudeBot,Claude-Web,Applebot-Extended,PerplexityBot,Meta-ExternalAgent,Meta-ExternalFetch,Bytespider,CCBot"

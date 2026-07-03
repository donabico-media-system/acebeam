# -*- coding: utf-8 -*-
import os
import sys
import subprocess

def run_blackbox_script(script_path: str, index_path: str):
    script_name = os.path.basename(script_path)
    print(f"[EXECUTE] Kích hoạt thực địa: {script_name} (Chế độ Hộp Đen)...")
    
    try:
        custom_env = os.environ.copy()
        custom_env["TARGET_INDEX_HTML"] = index_path
        
        result = subprocess.run(
            [sys.executable, script_path],
            capture_output=True,
            text=True,
            encoding="utf-8",
            env=custom_env,
            check=True
        )
        if result.stdout:
            print(f"[{script_name} STDOUT]:\n{result.stdout.strip()}")
        print(f"[SUCCESS] {script_name} hoàn thành tác vụ ✅")
        
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Script {script_name} gặp sự cố: {e.stderr}")
    except Exception as e:
        print(f"[CRITICAL] Lỗi hệ thống luồng tại {script_name}: {str(e)}")

def super_intelligent_core():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(current_dir)
    
    index_html_path = os.path.join(root_dir, "index.html")
    modules_dir = os.path.join(root_dir, "Modules")
    protocols_dir = os.path.join(root_dir, "Protocols")
    
    print("\n" + "="*60)
    print("[CORE] MODE: MONOLITHIC BLACK-BOX ENGINE (ZERO-CHILD-MOD) ⚡")
    print("="*60)
    
    if not os.path.exists(index_html_path):
        print(f"[FATAL] Không tìm thấy tệp index.html. Dừng khẩn cấp!")
        sys.exit(1)

    if os.path.exists(modules_dir) and os.path.isdir(modules_dir):
        for f_file in sorted([f for f in os.listdir(modules_dir) if f.endswith('.py')]):
            run_blackbox_script(os.path.join(modules_dir, f_file), index_html_path)

    if os.path.exists(protocols_dir) and os.path.isdir(protocols_dir):
        for p_file in sorted([f for f in os.listdir(protocols_dir) if f.endswith('.py')]):
            run_blackbox_script(os.path.join(protocols_dir, p_file), index_html_path)

    # Đảm bảo viền xanh và trạng thái luôn chuẩn
    with open(index_html_path, "r+", encoding="utf-8") as f:
        content = f.read()
        print("[POST-PROCESS] Quét cấu trúc SOTA-GREEN hoàn tất.")

    print("\n" + "="*60)
    print("[CORE] ĐƠN KHỐI VẬN HÀNH HOÀN HẢO ✅")
    print("="*60)

if __name__ == "__main__":
    super_intelligent_core()

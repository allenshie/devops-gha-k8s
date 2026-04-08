import time
import os
import psutil

# 當我們在 CI/CD 測試更新時，會修改這個變數
VERSION = "1.0.0-cpu"

def main():
    print(f"--- CPU Service Starting (Version: {VERSION}) ---")
    print(f"Process ID: {os.getpid()}")
    
    try:
        while True:
            # 獲取系統資訊
            cpu_usage = psutil.cpu_percent(interval=1)
            mem_info = psutil.virtual_memory()
            
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] [Version: {VERSION}] "
                  f"Status: Running | CPU: {cpu_usage}% | MEM: {mem_info.percent}%")
            
            time.sleep(4)
    except KeyboardInterrupt:
        print("Service shutting down...")

if __name__ == "__main__":
    main()

import torch
from ultralytics import YOLO
import time
import os

# CI/CD 測試更新時修改此變數
VERSION = "1.0.1-gpu"

def main():
    print(f"=== GPU Service Starting (Version: {VERSION}) ===")
    
    # 1. 檢查 GPU 可用性
    gpu_available = torch.cuda.is_available()
    gpu_name = torch.cuda.get_device_name(0) if gpu_available else "None"
    print(f"CUDA Available: {gpu_available}")
    print(f"GPU Device: {gpu_name}")

    # 2. 載入 Ultralytics YOLOv8 模型 (使用最輕量的 yolov8n.pt)
    print("Loading YOLOv8 model...")
    model = YOLO("yolov8n.pt") 
    
    print("Entering main loop...")
    try:
        while True:
            start_time = time.time()
            
            # 模擬推論 (在無圖片情況下，我們僅測試模型載入後的運行狀態)
            # 或者可以放一張 dummy 圖片進行測試
            status = "Active" if gpu_available else "Running on CPU"
            
            end_time = time.time()
            latency = (end_time - start_time) * 1000
            
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] [Version: {VERSION}] "
                  f"Status: {status} | GPU: {gpu_name} | Latency: {latency:.2f}ms")
            
            time.sleep(5)
    except KeyboardInterrupt:
        print("Shutting down GPU service...")

if __name__ == "__main__":
    main()

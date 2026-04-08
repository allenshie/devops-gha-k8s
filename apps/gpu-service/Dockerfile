# 使用官方 PyTorch 輕量級 CUDA 執行環境
FROM pytorch/pytorch:2.0.1-cuda11.7-cudnn8-runtime

WORKDIR /app

# 安裝系統依賴 (Ultralytics 需要 opencv-python 的一些 library)
RUN apt-get update && apt-get install -y libgl1-mesa-glx libglib2.0-0 && rm -rf /var/lib/apt/lists/*

# 安裝 Python 依賴
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 下載模型文件 (預先下載避免容器啟動時下載)
RUN python -c "from ultralytics import YOLO; YOLO('yolov8n.pt')"

COPY main.py .

CMD ["python", "main.py"]

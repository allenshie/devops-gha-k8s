FROM python:3.9-slim

WORKDIR /app

# 安裝系統依賴 (psutil 建置時可能需要)
RUN apt-get update && apt-get install -y gcc python3-dev && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .

CMD ["python", "main.py"]

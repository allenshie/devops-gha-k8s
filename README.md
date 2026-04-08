# DevOps GHA K8s Practice (Mono-repo)

這是一個完整的微服務 DevOps 實作專案，涵蓋了從 **本機開發循環 (Local Loop)** 到 **雲端持續整合與交付 (GitOps)** 的完整生命週期。

## 🏗 系統架構
本專案包含兩個核心微服務：
- **`cpu-service`**: 輕量級 Python 服務，監控 CPU 與記憶體使用率。
- **`gpu-service`**: AI 模擬服務，基於 PyTorch 與 YOLOv8，用於驗證 K8s GPU 資源調度。

## 🛠 本機開發 (Local Development)
我們使用 **Skaffold** 與 **MicroK8s** 打造極速的開發體驗。
- **一鍵啟動**：
  ```bash
  skaffold dev --default-repo=localhost:32000 --trigger=manual
  ```
- **部署策略**：
  - CPU 服務：`RollingUpdate` (零中斷更新)。
  - GPU 服務：`Recreate` (解決顯存資源競爭)。

## 🚀 CI/CD 與 GitOps 流程
1. **CI (GitHub Actions)**：
   - 偵測變動路徑，執行單元測試。
   - 建置 Docker 映像檔並推送到 Docker Hub。
   - **自動更新** `k8s/` 目錄下的 Deployment Manifest 版本號。
2. **CD (ArgoCD)**：
   - 伺服器上的 ArgoCD 偵測到 Manifest 變動，自動拉取新版本並部署到 K8s 叢集。

## 📂 目錄結構
- `apps/`: 微服務原始碼與 Dockerfile。
- `k8s/`: Kubernetes 部署清單 (Manifests)。
- `skaffold.yaml`: 總控配置，用於本機開發。
- `.github/workflows/`: GitHub Actions 自動化腳本。

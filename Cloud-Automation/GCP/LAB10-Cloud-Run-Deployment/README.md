# GCP LAB10 - Automate Cloud Run Deployment with Python

In this lab, you’ll learn to deploy a containerized web service to Google Cloud Run using Python and the Google Cloud SDK. Cloud Run provides a serverless platform to run containers.

---

## 🎯 Objectives

By the end of this lab, you will:
- Build a Docker container locally
- Push it to Google Container Registry (GCR)
- Deploy to Cloud Run using Python or `subprocess`

---

## 🧰 Prerequisites

- Docker installed and running
- GCP project with billing enabled
- Cloud Run and Container Registry APIs enabled
- Service account with Cloud Run Admin and Storage Admin roles

---

## 📁 Lab Files

```
Cloud-Automation/GCP/LAB10-Cloud-Run-Deployment/
├── app.py                 # Simple Flask app
├── Dockerfile
├── deploy_run.py         # Deployment script
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

1. Set credentials:
```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your-service-account.json"
```

2. Navigate to the lab folder:
```bash
cd Cloud-Automation/GCP/LAB10-Cloud-Run-Deployment/
```

3. Set up virtual environment and install:
```bash
python -m venv .venv
source .venv/bin/activate
pip install Flask google-api-python-client google-auth
pip freeze > requirements.txt
```

---

## ✍️ Your Task

### 1. Build and push Docker image:
```bash
docker build -t gcr.io/your-project-id/devops-cloudrun .
docker push gcr.io/your-project-id/devops-cloudrun
```

### 2. Deploy to Cloud Run:
```bash
gcloud run deploy devops-cloudrun \
  --image gcr.io/your-project-id/devops-cloudrun \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

### 3. Optional: Automate using Python subprocess module

---

## 🧪 Validation Checklist

✅ Image built and pushed to GCR  
✅ Cloud Run service deployed and accessible  
✅ Script/app runs cleanly:
```bash
python deploy_run.py
```

---

## 🧹 Cleanup
Delete the service:
```bash
gcloud run services delete devops-cloudrun
```

---

## 🎉 Congratulations!
You’ve completed all 10 GCP automation labs. You now have the skills to provision, monitor, deploy, and connect services across Google Cloud using Python!

---

## 🙏 Acknowledgments
Cloud Run is the final piece in your cloud-native journey — from source to service.

Code, container, deploy. 🐳☁️🚀


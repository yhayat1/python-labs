# GCP LAB04 - Automate Cloud Functions Deployment with Python

In this lab, you’ll learn how to deploy a Google Cloud Function using Python and the `google-cloud-functions` API. Serverless functions enable you to run event-driven code without managing infrastructure.

---

## 🎯 Objectives

By the end of this lab, you will:
- Package and deploy a cloud function using Python
- Configure runtime, trigger, and entry point
- Test deployment by calling the function

---

## 🧰 Prerequisites

- GCP project and billing enabled
- Cloud Functions API enabled
- Python 3.8+ installed
- Service account with Cloud Functions Developer role

---

## 📁 Lab Files

```
Cloud-Automation/GCP/LAB04-Cloud-Functions-Deployment/
├── main.py                   # Function source
├── deploy_function.py        # Deployment script
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
cd Cloud-Automation/GCP/LAB04-Cloud-Functions-Deployment/
```

3. Create virtual environment and install tools:
```bash
python -m venv .venv
source .venv/bin/activate
pip install google-cloud-functions google-api-python-client google-auth
pip freeze > requirements.txt
```

---

## ✍️ Your Task

### 1. Write a basic Cloud Function (`main.py`):
```python
def hello_world(request):
    return "Hello from your Cloud Function!"
```

### 2. Deploy with `gcloud` (triggered by HTTP):
```bash
gcloud functions deploy hello_world \
  --runtime python310 \
  --trigger-http \
  --allow-unauthenticated \
  --entry-point hello_world
```

### 3. Optional: Automate the same deployment via Python using `subprocess` or GCF API.

---

## 🧪 Validation Checklist

✅ Cloud Function deployed using Python/gcloud  
✅ Accessible via HTTP trigger  
✅ Script runs cleanly:
```bash
python deploy_function.py  # if automated
```

---

## 🧹 Cleanup
Delete the function after testing:
```bash
gcloud functions delete hello_world
```

---

## 💬 What's Next?
Next: [GCP LAB05 - Cloud Monitoring Metrics](../LAB05-Cloud-Monitoring-Metrics/) to monitor resources and retrieve metrics.

---

## 🙏 Acknowledgments
Cloud Functions let you deploy microservices with speed and simplicity. Automate the cloud with fewer servers, more code!

Happy triggering! ☁️⚡🐍


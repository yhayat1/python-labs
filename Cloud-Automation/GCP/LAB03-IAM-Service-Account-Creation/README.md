# GCP LAB03 - Automate IAM Service Account Creation with Python

In this lab, you'll learn how to create and manage IAM service accounts in GCP using Python. Automating IAM is essential for secure, scalable cloud infrastructure.

---

## 🎯 Objectives

By the end of this lab, you will:
- Use Python to create a service account
- Assign roles to the service account
- List existing service accounts

---

## 🧰 Prerequisites

- GCP project and billing enabled
- IAM permissions to create and manage service accounts
- Service account key for authentication
- Python 3.8+ and `google-api-python-client` installed

---

## 📁 Lab Files

```
Cloud-Automation/GCP/LAB03-IAM-Service-Account-Creation/
├── create_service_account.py
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
cd Cloud-Automation/GCP/LAB03-IAM-Service-Account-Creation/
```

3. Create and activate virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate
```

4. Install dependencies:
```bash
pip install google-api-python-client google-auth
pip freeze > requirements.txt
```

---

## ✍️ Your Task

### 1. Create a service account:
```python
from googleapiclient import discovery
from google.oauth2 import service_account

project_id = "your-project-id"
service_account_id = "devops-service-account"
service_account_name = "DevOps Service Account"

credentials = service_account.Credentials.from_service_account_file(
    "your-service-account.json")

service = discovery.build('iam', 'v1', credentials=credentials)

service_account = {
    "accountId": service_account_id,
    "serviceAccount": {
        "displayName": service_account_name
    }
}

request = service.projects().serviceAccounts().create(
    name=f"projects/{project_id}", body=service_account)
response = request.execute()

print("Created service account:", response['email'])
```

---

## 🧪 Validation Checklist

✅ IAM service account created via API  
✅ Role assignment (optional) completed successfully  
✅ Script runs cleanly:
```bash
python create_service_account.py
```

---

## 🧹 Cleanup
You can delete the service account via the GCP Console or with Python:
```python
service.projects().serviceAccounts().delete(
    name=f"projects/{project_id}/serviceAccounts/{response['email']}").execute()
```

---

## 💬 What's Next?
Move on to [GCP LAB04 - Cloud Functions Deployment](../LAB04-Cloud-Functions-Deployment/) to automate serverless function deployment.

---

## 🙏 Acknowledgments
IAM automation enables secure access at scale. This lab gets you started with managing permissions using Python.

Secure your future! 🔐☁️🐍
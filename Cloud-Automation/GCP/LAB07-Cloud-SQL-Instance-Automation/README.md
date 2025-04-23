# GCP LAB07 - Automate Cloud SQL Instance Creation with Python

In this lab, you'll use Python to create a Cloud SQL instance in GCP using the `google-api-python-client`. Cloud SQL provides fully managed relational databases.

---

## 🎯 Objectives

By the end of this lab, you will:
- Programmatically create a Cloud SQL instance
- Specify database type, version, and machine size
- List existing SQL instances in your project

---

## 🧰 Prerequisites

- GCP project with billing enabled
- Cloud SQL Admin API enabled
- Service account with SQL Admin role
- Python 3.8+ and `google-api-python-client` installed

---

## 📁 Lab Files

```
Cloud-Automation/GCP/LAB07-Cloud-SQL-Instance-Automation/
├── create_sql_instance.py
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

1. Set up credentials:
```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your-service-account.json"
```

2. Navigate to the lab folder:
```bash
cd Cloud-Automation/GCP/LAB07-Cloud-SQL-Instance-Automation/
```

3. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate
```

4. Install dependencies:
```bash
pip install google-api-python-client google-auth google-auth-httplib2
pip freeze > requirements.txt
```

---

## ✍️ Your Task

### 1. Create a Cloud SQL instance:
```python
from googleapiclient import discovery
from google.oauth2 import service_account

project_id = "your-project-id"
instance_id = "devops-sql"
credentials = service_account.Credentials.from_service_account_file(
    "your-service-account.json")

service = discovery.build('sqladmin', 'v1beta4', credentials=credentials)

instance_body = {
    "name": instance_id,
    "databaseVersion": "MYSQL_8_0",
    "settings": {
        "tier": "db-f1-micro",
        "backupConfiguration": {
            "enabled": True
        }
    }
}

request = service.instances().insert(project=project_id, body=instance_body)
response = request.execute()
print("Cloud SQL instance creation initiated:", response.get("targetLink"))
```

---

## 🧪 Validation Checklist

✅ SQL instance created using Python  
✅ Configuration includes machine type and version  
✅ Script runs successfully:
```bash
python create_sql_instance.py
```

---

## 🧹 Cleanup
Delete the SQL instance to avoid charges:
```bash
gcloud sql instances delete devops-sql
```

---

## 💬 What's Next?
Next: [GCP LAB08 - VPC Network Creation](../LAB08-VPC-Network-Creation/) to build private networks and subnets with Python.

---

## 🙏 Acknowledgments
Cloud SQL powers secure, scalable relational databases. Automate provisioning to ensure fast, repeatable deployments.

Scale your data, Pythonically! 🗄☁️🐍


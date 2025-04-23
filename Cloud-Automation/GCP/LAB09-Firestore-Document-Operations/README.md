# GCP LAB09 - Automate Firestore Document Operations with Python

In this lab, you’ll use Python to connect to Firestore, Google Cloud’s NoSQL document database. You’ll add, retrieve, and delete documents in a Firestore collection.

---

## 🎯 Objectives

By the end of this lab, you will:
- Initialize a connection to Firestore
- Create and retrieve documents
- Delete documents programmatically

---

## 🧰 Prerequisites

- GCP project with Firestore in Native mode
- Service account with Firestore Admin role
- Python 3.8+ and `google-cloud-firestore` installed

---

## 📁 Lab Files

```
Cloud-Automation/GCP/LAB09-Firestore-Document-Operations/
├── firestore_script.py
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
cd Cloud-Automation/GCP/LAB09-Firestore-Document-Operations/
```

3. Create virtual environment and install dependencies:
```bash
python -m venv .venv
source .venv/bin/activate
pip install google-cloud-firestore
pip freeze > requirements.txt
```

---

## ✍️ Your Task

### 1. Create and read a document:
```python
from google.cloud import firestore

client = firestore.Client()
collection = client.collection("devops-users")

# Add document
collection.document("alice").set({"role": "admin", "email": "alice@example.com"})
print("Document created.")

# Retrieve document
doc = collection.document("alice").get()
if doc.exists:
    print("Retrieved document:", doc.to_dict())
```

### 2. Delete the document:
```python
collection.document("alice").delete()
print("Document deleted.")
```

---

## 🧪 Validation Checklist

✅ Firestore collection and document created  
✅ Document fields retrieved and displayed  
✅ Script runs cleanly:
```bash
python firestore_script.py
```

---

## 🧹 Cleanup
No extra cleanup needed beyond document deletion.

---

## 💬 What's Next?
Complete your GCP series with [GCP LAB10 - Cloud Run Deployment](../LAB10-Cloud-Run-Deployment/) for containerized, fully managed services.

---

## 🙏 Acknowledgments
Firestore enables quick and flexible NoSQL automation for modern apps. Start simple, scale fast.

Write it. Query it. Automate it! 🧾☁️🐍


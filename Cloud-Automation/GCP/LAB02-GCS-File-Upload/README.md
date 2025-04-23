# GCP LAB02 - Automate File Upload to Google Cloud Storage (GCS) with Python

In this lab, you'll use Python and the `google-cloud-storage` library to upload files to a Google Cloud Storage (GCS) bucket — one of the most common automation tasks in the cloud.

---

## 🎯 Objectives

By the end of this lab, you will:
- Connect to GCS with a service account
- Upload a file to a GCS bucket using Python
- List objects in the bucket programmatically

---

## 🧰 Prerequisites

- Google Cloud account and project
- GCS bucket already created
- Service account key with Storage Admin role
- Python 3.8+ and `google-cloud-storage` installed

---

## 📁 Lab Files

```
Cloud-Automation/GCP/LAB02-GCS-File-Upload/
├── upload_file.py
├── sample.txt               # Sample file to upload
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
cd Cloud-Automation/GCP/LAB02-GCS-File-Upload/
```

3. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate
```

4. Install the required package:
```bash
pip install google-cloud-storage
pip freeze > requirements.txt
```

---

## ✍️ Your Task

### 1. Upload a file to GCS:
```python
from google.cloud import storage

bucket_name = "your-bucket-name"
file_path = "sample.txt"
blob_name = "uploads/sample.txt"

client = storage.Client()
bucket = client.bucket(bucket_name)
blob = bucket.blob(blob_name)
blob.upload_from_filename(file_path)

print(f"Uploaded {file_path} to gs://{bucket_name}/{blob_name}")
```

### 2. List files in the bucket:
```python
for blob in client.list_blobs(bucket_name):
    print("Found blob:", blob.name)
```

---

## 🧪 Validation Checklist

✅ File uploaded successfully to GCS  
✅ GCS bucket contents listed with Python  
✅ Script runs cleanly:
```bash
python upload_file.py
```

---

## 🧹 Cleanup
You can delete the uploaded file with:
```python
blob.delete()
```

---

## 💬 What's Next?
Advance to [GCP LAB03 - IAM Service Account Creation](../LAB03-IAM-Service-Account-Creation/) to manage access controls in GCP.

---

## 🙏 Acknowledgments
Google Cloud Storage is an essential component for storing and serving files at scale. Mastering it unlocks endless automation workflows.

Keep it cloud-native! 📂☁️🐍
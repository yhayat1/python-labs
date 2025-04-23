# AWS LAB02 - Automate File Upload to S3 with Python (boto3)

This lab will teach you how to upload files to an S3 bucket using Python and `boto3`. S3 is one of the most widely used cloud storage solutions, and automating uploads is useful for backups, reports, logs, and more.

---

## 🎯 Objectives

By the end of this lab, you will:
- Connect to AWS S3 using Python
- Upload a local file to a specific S3 bucket
- Set metadata and access control during the upload
- List objects in a bucket

---

## 🧰 Prerequisites

- AWS account and S3 permissions
- Python 3.8+ and `boto3` installed
- A pre-created S3 bucket (or automate it with `boto3`)

---

## 📁 Lab Files

```
Cloud-Automation/AWS/LAB02-S3-File-Upload/
├── upload_file.py
├── sample.txt              # Sample file to upload
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

1. Navigate to the lab folder:
```bash
cd Cloud-Automation/AWS/LAB02-S3-File-Upload/
```

2. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install `boto3`:
```bash
pip install boto3
pip freeze > requirements.txt
```

---

## ✍️ Your Task

### 1. Upload file to S3:
```python
import boto3

bucket_name = 'your-bucket-name'  # Replace this
file_name = 'sample.txt'
s3_key = 'uploads/sample.txt'

s3 = boto3.client('s3')
s3.upload_file(file_name, bucket_name, s3_key, ExtraArgs={'ACL': 'public-read'})

print(f"Uploaded {file_name} to s3://{bucket_name}/{s3_key}")
```

### 2. List objects in the bucket:
```python
response = s3.list_objects_v2(Bucket=bucket_name)
for obj in response.get('Contents', []):
    print("Found object:", obj['Key'])
```

---

## 🧪 Validation Checklist

✅ File is uploaded to your S3 bucket  
✅ Object is publicly accessible (if ACL is set)  
✅ Script lists all objects in the target bucket  
✅ Script runs cleanly:
```bash
python upload_file.py
```

---

## 🧹 Cleanup
Delete the object manually or use:
```python
s3.delete_object(Bucket=bucket_name, Key=s3_key)
```

---

## 💬 What's Next?
Move to [AWS LAB03 - IAM User and Policy Automation](../LAB03-IAM-User-and-Policy-Automation/) to start managing users and permissions with Python.

---

## 🙏 Acknowledgments
Automated S3 operations save time and reduce errors. Combine with cron jobs or CI pipelines for powerful workflows.

Happy scripting! 🪣🐍


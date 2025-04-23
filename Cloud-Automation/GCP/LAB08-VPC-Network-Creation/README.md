# GCP LAB08 - Automate VPC Network Creation with Python

In this lab, you’ll learn how to automate the creation of a VPC network and subnet in Google Cloud using Python and the `google-api-python-client`. Private networks are essential for organizing cloud infrastructure securely.

---

## 🎯 Objectives

By the end of this lab, you will:
- Create a custom VPC network
- Add a subnet with an IP CIDR range
- Understand network segmentation in GCP

---

## 🧰 Prerequisites

- GCP project with billing enabled
- Service account with Compute Network Admin role
- Python 3.8+ and `google-api-python-client` installed

---

## 📁 Lab Files

```
Cloud-Automation/GCP/LAB08-VPC-Network-Creation/
├── create_vpc.py
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

1. Set your credentials:
```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your-service-account.json"
```

2. Navigate to the lab folder:
```bash
cd Cloud-Automation/GCP/LAB08-VPC-Network-Creation/
```

3. Set up a virtual environment:
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

### 1. Create a VPC and subnet:
```python
from googleapiclient import discovery
from google.oauth2 import service_account

project_id = "your-project-id"
network_name = "devops-vpc"
region = "us-central1"
subnet_name = "devops-subnet"

credentials = service_account.Credentials.from_service_account_file(
    "your-service-account.json")

service = discovery.build('compute', 'v1', credentials=credentials)

# Create VPC network
network_body = {
    "name": network_name,
    "autoCreateSubnetworks": False
}
service.networks().insert(project=project_id, body=network_body).execute()
print("VPC network created.")

# Create subnet
subnet_body = {
    "name": subnet_name,
    "ipCidrRange": "10.0.0.0/24",
    "region": region,
    "network": f"projects/{project_id}/global/networks/{network_name}"
}
service.subnetworks().insert(project=project_id, region=region, body=subnet_body).execute()
print("Subnet created.")
```

---

## 🧪 Validation Checklist

✅ VPC network created with custom name  
✅ Subnet created in specific region with CIDR block  
✅ Script runs cleanly:
```bash
python create_vpc.py
```

---

## 🧹 Cleanup
Delete the subnet and network after testing:
```bash
gcloud compute networks subnets delete devops-subnet --region=us-central1
gcloud compute networks delete devops-vpc
```

---

## 💬 What's Next?
Next: [GCP LAB09 - Firestore Document Operations](../LAB09-Firestore-Document-Operations/) to automate NoSQL document creation and queries.

---

## 🙏 Acknowledgments
VPCs are the foundation of your cloud network. Learning to automate them helps enforce consistency and scalability.

Design smart networks! 🌐☁️🐍


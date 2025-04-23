# GCP LAB01 - Automate Compute Engine Instance Creation with Python (google-cloud-compute)

In this lab, you'll use Python and the Google Cloud SDK to programmatically create a virtual machine (VM) instance in Google Cloud Platform (GCP) using the `google-cloud-compute` library.

---

## 🎯 Objectives

By the end of this lab, you will:
- Authenticate to GCP using a service account
- Use Python to create a Compute Engine VM
- Understand how to configure machine type, zone, and image

---

## 🧰 Prerequisites

- Google Cloud account and project
- Service account key file with Compute Admin role
- Python 3.8+ installed

---

## 📁 Lab Files

```
Cloud-Automation/GCP/LAB01-Compute-Instance-Creation/
├── create_instance.py
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

1. Set up authentication:
```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your-service-account.json"
```

2. Navigate to the lab folder:
```bash
cd Cloud-Automation/GCP/LAB01-Compute-Instance-Creation/
```

3. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate
```

4. Install dependencies:
```bash
pip install google-cloud-compute
pip freeze > requirements.txt
```

---

## ✍️ Your Task

### 1. Write the script to create a VM:
```python
from google.cloud import compute_v1

project_id = "your-gcp-project-id"
zone = "us-central1-a"
instance_name = "devops-instance"

instance_client = compute_v1.InstancesClient()

instance = compute_v1.Instance()
instance.name = instance_name
instance.machine_type = f"zones/{zone}/machineTypes/e2-micro"
instance.disks = [compute_v1.AttachedDisk(
    auto_delete=True,
    boot=True,
    initialize_params=compute_v1.AttachedDiskInitializeParams(
        source_image="projects/debian-cloud/global/images/family/debian-11"
    )
)]
instance.network_interfaces = [compute_v1.NetworkInterface(
    name="global/networks/default"
)]

operation = instance_client.insert(
    project=project_id,
    zone=zone,
    instance_resource=instance
)
print(f"Instance creation started: {operation.name}")
```

---

## 🧪 Validation Checklist

✅ GCP credentials exported and service account configured  
✅ Instance created using Python SDK  
✅ Script runs cleanly:
```bash
python create_instance.py
```

---

## 🧹 Cleanup
To avoid charges, delete the instance after use:
```bash
gcloud compute instances delete devops-instance --zone=us-central1-a
```

---

## 💬 What's Next?
Move to [GCP LAB02 - GCS File Upload](../LAB02-GCS-File-Upload/) to automate file operations in Google Cloud Storage.

---

## 🙏 Acknowledgments
Compute Engine is the backbone of GCP. Automating VM creation is your first step toward infrastructure-as-code in Google Cloud.

Happy provisioning! 🖥️☁️🐍


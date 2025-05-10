# AWS LAB01 - Automate EC2 Instance Launch with Python (boto3)

In this lab, you'll learn how to launch an Amazon EC2 instance using Python and the `boto3` SDK. This is your first step into cloud automation using Python!

---

## 🎯 Objectives

By the end of this lab, you will:
- Understand how to configure AWS credentials for `boto3`
- Use Python to interact with EC2 APIs using the client interface
- Launch a t2.micro EC2 instance in your default VPC
- Print out the instance ID and public DNS

---

## 🧰 Prerequisites

- AWS account and IAM user with EC2 permissions
- `aws configure` run at least once (to store credentials)
- Python 3.8+ and `boto3` installed

---

## 📁 Lab Files

```
Cloud-Automation/AWS/LAB01-EC2-Automation/
├── launch_ec2.py
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

1. Navigate to the lab folder:
```bash
cd Cloud-Automation/AWS/LAB01-EC2-Automation/
```

2. Create and activate a virtual environment:
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

### Complete all TODOs in [launch_ec2.py](./launch_ec2.py)
### Solutions can be found in [solutions.md](./solutions.md)

---

## 🧪 Validation Checklist

✅ AWS credentials configured  
✅ Instance launched successfully (t2.micro)  
✅ Printed instance ID and public DNS  
✅ Script runs without error:
```bash
python launch_ec2.py
```

---

## 🧹 Cleanup
Terminate the instance manually in AWS Console or run:
```python
ec2_client.terminate_instances(InstanceIds=['i-your-instance-id'])
```

---

## 💬 What's Next?
Try [AWS LAB02 - S3 File Upload](../LAB02-S3-File-Upload/) to automate object storage tasks using Python.

---

## 🙏 Acknowledgments
Launching infrastructure with code is the essence of DevOps. Mastering `boto3` enables powerful automations across AWS.

Happy automating! ☁️🐍

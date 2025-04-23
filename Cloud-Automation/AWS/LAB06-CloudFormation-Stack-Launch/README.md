# AWS LAB06 - Automate CloudFormation Stack Launch with Python (boto3)

CloudFormation lets you define your infrastructure as code. In this lab, you'll use Python to programmatically deploy a CloudFormation template using `boto3`.

---

## 🎯 Objectives

By the end of this lab, you will:
- Use Python to launch a CloudFormation stack
- Deploy a simple EC2 instance using a template
- Monitor stack creation status

---

## 🧰 Prerequisites

- AWS account with CloudFormation and EC2 permissions
- Python 3.8+ and `boto3` installed

---

## 📁 Lab Files

```
Cloud-Automation/AWS/LAB06-CloudFormation-Stack-Launch/
├── launch_stack.py
├── ec2_template.yaml       # CloudFormation template file
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

1. Navigate to the lab folder:
```bash
cd Cloud-Automation/AWS/LAB06-CloudFormation-Stack-Launch/
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

### 1. Define a basic EC2 template in `ec2_template.yaml`:
```yaml
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  MyInstance:
    Type: AWS::EC2::Instance
    Properties:
      InstanceType: t2.micro
      ImageId: ami-0c02fb55956c7d316  # Update if needed
```

### 2. Launch the stack with `launch_stack.py`:
```python
import boto3

cf = boto3.client('cloudformation')

with open("ec2_template.yaml") as f:
    template_body = f.read()

response = cf.create_stack(
    StackName='DevOpsEC2Stack',
    TemplateBody=template_body,
    Capabilities=['CAPABILITY_IAM']
)

print("Stack creation started:", response['StackId'])
```

---

## 🧪 Validation Checklist

✅ Template created and valid YAML  
✅ Stack launched with `boto3`  
✅ Stack status viewable in AWS Console  
✅ Script runs cleanly:
```bash
python launch_stack.py
```

---

## 🧹 Cleanup
Delete the stack:
```python
cf.delete_stack(StackName='DevOpsEC2Stack')
```

---

## 💬 What's Next?
Next: [AWS LAB07 - DynamoDB Table Automation](../LAB07-DynamoDB-Table-Automation/) to learn how to automate NoSQL databases in the cloud.

---

## 🙏 Acknowledgments
Using CloudFormation with Python empowers you to scale infrastructure as code with precision and control.

Happy stacking! 🏗🐍
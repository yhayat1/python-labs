# AWS LAB05 - Deploy an AWS Lambda Function with Python (boto3)

In this lab, you'll deploy a basic AWS Lambda function using Python and the `boto3` SDK. Lambda is a powerful serverless compute service that enables you to run code without provisioning infrastructure.

---

## 🎯 Objectives

By the end of this lab, you will:
- Package and deploy a Lambda function using Python
- Assign an IAM role for Lambda execution
- Invoke the Lambda function from your script

---

## 🧰 Prerequisites

- AWS account with Lambda and IAM permissions
- Python 3.8+ and `boto3` installed

---

## 📁 Lab Files

```
Cloud-Automation/AWS/LAB05-Lambda-Deployment/
├── lambda_function.py       # Lambda function code
├── deploy_lambda.py         # Deployment script
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

1. Navigate to the lab folder:
```bash
cd Cloud-Automation/AWS/LAB05-Lambda-Deployment/
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

### 1. Create a simple Lambda function (`lambda_function.py`):
```python
def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': 'Hello from Lambda!'
    }
```

### 2. Package and deploy it:
```python
import boto3, zipfile, os

zip_name = "function.zip"
with zipfile.ZipFile(zip_name, 'w') as z:
    z.write("lambda_function.py")

client = boto3.client('lambda')
with open(zip_name, 'rb') as f:
    response = client.create_function(
        FunctionName='MyDevOpsLambda',
        Runtime='python3.8',
        Role='arn:aws:iam::your-account-id:role/lambda-execute-role',
        Handler='lambda_function.lambda_handler',
        Code={'ZipFile': f.read()},
        Timeout=10,
        MemorySize=128
    )
print("Lambda function deployed:", response['FunctionArn'])
```

### 3. Invoke the Lambda function:
```python
client.invoke(FunctionName='MyDevOpsLambda', InvocationType='RequestResponse')
```

---

## 🧪 Validation Checklist

✅ Lambda function zipped and deployed using `boto3`  
✅ Valid IAM role used for execution  
✅ Function invoked successfully  
✅ Script runs without error:
```bash
python deploy_lambda.py
```

---

## 🧹 Cleanup
Delete the Lambda function:
```python
client.delete_function(FunctionName='MyDevOpsLambda')
```

---

## 💬 What's Next?
Move on to [AWS LAB06 - CloudFormation Stack Launch](../LAB06-CloudFormation-Stack-Launch/) to automate infrastructure as code deployments.

---

## 🙏 Acknowledgments
Lambda lets you run code instantly in the cloud. Automating Lambda deployment is a great step toward fully serverless systems.

Happy deploying! ⚡🐍
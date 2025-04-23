# AWS LAB08 - Automate SNS Topic Creation and Subscription with Python (boto3)

In this lab, you will create an Amazon SNS topic, subscribe an email address, and publish messages — all using Python. SNS enables distributed messaging and notification for event-driven systems.

---

## 🎯 Objectives

By the end of this lab, you will:
- Create an SNS topic programmatically
- Subscribe an email address to the topic
- Publish a test message

---

## 🧰 Prerequisites

- AWS account with SNS permissions
- Python 3.8+ and `boto3` installed
- Valid email address to receive SNS confirmation

---

## 📁 Lab Files

```
Cloud-Automation/AWS/LAB08-SNS-Topic-and-Subscription/
├── sns_script.py
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

1. Navigate to the lab folder:
```bash
cd Cloud-Automation/AWS/LAB08-SNS-Topic-and-Subscription/
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

### 1. Create an SNS topic:
```python
import boto3

sns = boto3.client('sns')

response = sns.create_topic(Name='DevOpsAlerts')
topic_arn = response['TopicArn']
print("Created topic:", topic_arn)
```

### 2. Subscribe an email address:
```python
email = 'your-email@example.com'  # Replace with your actual email
sns.subscribe(
    TopicArn=topic_arn,
    Protocol='email',
    Endpoint=email
)
print("Subscription request sent. Confirm via email.")
```

### 3. Publish a message:
```python
sns.publish(
    TopicArn=topic_arn,
    Subject='Test Alert',
    Message='This is a test message from your Python script.'
)
```

---

## 🧪 Validation Checklist

✅ SNS topic created  
✅ Email subscription request received  
✅ Message sent to topic and received via email  
✅ Script runs cleanly:
```bash
python sns_script.py
```

---

## 🧹 Cleanup
Delete the topic using:
```python
sns.delete_topic(TopicArn=topic_arn)
```

---

## 💬 What's Next?
Next up: [AWS LAB09 - SQS Queue Automation](../LAB09-SQS-Queue-Automation/) to build reliable queues for message processing.

---

## 🙏 Acknowledgments
SNS is a core building block for notifications and integrations. Automating it keeps your infrastructure flexible and alert-ready.

Stay notified! 📬🐍
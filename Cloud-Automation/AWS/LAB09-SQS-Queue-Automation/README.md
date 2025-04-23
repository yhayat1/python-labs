# AWS LAB09 - Automate SQS Queue Creation and Messaging with Python (boto3)

Amazon SQS (Simple Queue Service) enables reliable and scalable message queuing. In this lab, you’ll create a queue, send messages to it, and receive them using Python.

---

## 🎯 Objectives

By the end of this lab, you will:
- Create an SQS queue programmatically
- Send and receive messages via the queue
- Understand how queues enable decoupled architecture

---

## 🧰 Prerequisites

- AWS account with SQS permissions
- Python 3.8+ and `boto3` installed

---

## 📁 Lab Files

```
Cloud-Automation/AWS/LAB09-SQS-Queue-Automation/
├── sqs_script.py
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

1. Navigate to the lab folder:
```bash
cd Cloud-Automation/AWS/LAB09-SQS-Queue-Automation/
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install boto3
pip freeze > requirements.txt
```

---

## ✍️ Your Task

### 1. Create a new queue:
```python
import boto3

sqs = boto3.client('sqs')
response = sqs.create_queue(QueueName='DevOpsQueue')
queue_url = response['QueueUrl']
print("Queue created:", queue_url)
```

### 2. Send a message:
```python
sqs.send_message(QueueUrl=queue_url, MessageBody='Hello from DevOps lab!')
print("Message sent.")
```

### 3. Receive messages:
```python
messages = sqs.receive_message(QueueUrl=queue_url, MaxNumberOfMessages=1)
for msg in messages.get('Messages', []):
    print("Received message:", msg['Body'])
    sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=msg['ReceiptHandle'])
```

---

## 🧪 Validation Checklist

✅ SQS queue created and URL printed  
✅ Message sent and received successfully  
✅ Messages deleted from the queue after receipt  
✅ Script runs cleanly:
```bash
python sqs_script.py
```

---

## 🧹 Cleanup
Delete the queue with:
```python
sqs.delete_queue(QueueUrl=queue_url)
```

---

## 💬 What's Next?
Try [AWS LAB10 - EventBridge Rule Trigger](../LAB10-EventBridge-Rule-Trigger/) to schedule or react to cloud events using rules.

---

## 🙏 Acknowledgments
SQS allows components to communicate reliably. Mastering queues is a step toward building resilient cloud applications.

Queue it up! 📨🐍
# AWS LAB08 - SNS Topic and Subscription Automation with Python (boto3)

This lab guides you through creating a Python script to automate Amazon Simple Notification Service (SNS) operations using the AWS SDK for Python (Boto3). You'll implement various SNS operations including topic creation, subscription management, and message publishing.

---

## 🎯 Objectives

By the end of this lab, you will:
- Create SNS topics programmatically using boto3
- Subscribe email endpoints to receive notifications
- Publish messages to SNS topics
- List and manage topic subscriptions
- Delete SNS topics and clean up resources
- Understand SNS messaging fundamentals

---

## 🧰 Prerequisites

- AWS account with appropriate permissions
- Python 3.8+ installed
- AWS CLI configured with appropriate credentials

---

## 📁 Lab Files

```
Cloud-Automation/AWS/LAB08-SNS-Topic-and-Subscription/
├── sns_script.py
├── requirements.txt
├── README.md
└── solution_reference.py (reference only)
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
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Verify your AWS credentials are configured:
```bash
aws configure list
```

---

## ✍️ Your Task

The script `sns_script.py` contains skeleton functions with TODOs that you need to implement:

1. Complete the `create_topic()` function to create an SNS topic
2. Implement `list_topics()` to retrieve all SNS topics in your account
3. Code the `subscribe_email()` function to add an email subscription to a topic
4. Fill in the `publish_message()` function to send notifications to a topic
5. Complete the `list_subscriptions()` function to view all subscriptions
6. Implement `delete_subscription()` to remove a subscription
7. Complete the `delete_topic()` function to clean up resources

---

## 🧪 Validation Checklist

✅ Run the script to test your implementation:
```bash
python sns_script.py --create-topic DevOpsNotifications
```

✅ The script should:
- Create an SNS topic named 'DevOpsNotifications'
- List all topics in your account
- Allow you to subscribe an email address:
```bash
python sns_script.py --topic-arn <your-topic-arn> --subscribe your.email@example.com
```
- Enable sending messages to subscribers:
```bash
python sns_script.py --topic-arn <your-topic-arn> --publish "Test message" --subject "Test Subject"
```

✅ Try listing subscriptions:
```bash
python sns_script.py --list-subscriptions --topic-arn <your-topic-arn>
```

---

## 🧹 Cleanup

When you're done with the lab, clean up resources to avoid charges:
```bash
python sns_script.py --delete-topic --topic-arn <your-topic-arn>
```

---

## 💬 What's Next?

Try [AWS LAB09 - SQS Queue Automation](../LAB09-SQS-Queue-Automation/) to learn about queue-based messaging services.

---

## 📚 SNS Key Concepts

- **Topic**: The communication channel to which publishers send messages and subscribers receive notifications
- **Subscription**: The endpoint (email, SMS, Lambda, etc.) that receives messages published to a topic
- **Publish/Subscribe Model**: Pattern where publishers send messages to topics without knowledge of subscribers
- **Fan-out Pattern**: Sending a single message to multiple recipients simultaneously
- **Subscription Confirmation**: Email subscribers must confirm subscription before receiving messages

---

## 🚀 Extension Tasks

If you complete the main tasks, try these additional challenges:
1. Add SMS subscription support (requires AWS account verification for production use)
2. Implement topic attributes management (DisplayName, DeliveryPolicy)
3. Add support for publishing structured messages in JSON format
4. Implement subscription filtering with filter policies
5. Create an HTTP/HTTPS endpoint subscription with a simple web server

---

## 🙏 Acknowledgments

Amazon SNS is a critical service for building event-driven architectures in AWS.

Happy messaging! 📨🐍
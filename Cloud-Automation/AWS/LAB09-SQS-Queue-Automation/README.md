# AWS LAB09 - SQS Queue Automation with Python (boto3)

This lab guides you through creating a Python script to automate Amazon Simple Queue Service (SQS) operations using the AWS SDK for Python (Boto3). You'll implement various SQS operations including queue creation, message sending, receiving, and queue deletion.

---

## 🎯 Objectives

By the end of this lab, you will:
- Create and manage SQS queues programmatically using boto3
- Send messages to SQS queues with custom attributes
- Receive and process messages from queues
- Understand queue types (standard vs. FIFO) and their use cases
- Implement message visibility timeout handling
- Delete messages and queues properly to avoid resource leaks

---

## 🧰 Prerequisites

- AWS account with appropriate permissions
- Python 3.8+ installed
- AWS CLI configured with appropriate credentials

---

## 📁 Lab Files

```
Cloud-Automation/AWS/LAB09-SQS-Queue-Automation/
├── sqs_script.py
├── requirements.txt
├── README.md
└── solutions.md (reference only)
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

The script `sqs_script.py` contains skeleton functions with TODOs that you need to implement:

1. Complete the `create_queue()` function to create an SQS queue
2. Implement `list_queues()` to retrieve all SQS queues in your account
3. Code the `send_message()` function to send a message to a queue
4. Fill in the `receive_messages()` function to retrieve messages from a queue
5. Complete the `delete_message()` function to remove a processed message
6. Implement `delete_queue()` to clean up resources

---

## 🧪 Validation Checklist

✅ Run the script to test your implementation:
```bash
python sqs_script.py --create-queue DevOpsQueue
```

✅ The script should:
- Create an SQS queue with the specified name
- List all queues in your account
- Allow you to send messages to the queue:
```bash
python sqs_script.py --queue-url <your-queue-url> --send-message "Test message"
```
- Enable receiving messages from the queue:
```bash
python sqs_script.py --queue-url <your-queue-url> --receive
```

✅ Try sending messages with attributes:
```bash
python sqs_script.py --queue-url <your-queue-url> --send-message "Priority message" --attributes '{"Priority":{"DataType":"String","StringValue":"High"}}'
```

---

## 🧹 Cleanup

When you're done with the lab, clean up resources to avoid charges:
```bash
python sqs_script.py --delete-queue --queue-url <your-queue-url>
```

---

## 💬 What's Next?

Try [AWS LAB10 - EventBridge Rule Trigger](../LAB10-EventBridge-Rule-Trigger/) to learn about event-driven automation.

---

## 📚 SQS Key Concepts

- **Queue Types**: Standard queues offer maximum throughput, while FIFO queues guarantee exactly-once processing
- **Message Visibility**: After a message is received, it becomes invisible to other consumers for a configurable period
- **Dead Letter Queues**: Queues where messages that can't be processed successfully are sent after a defined number of attempts
- **Long Polling**: A method to reduce empty responses by waiting for messages to arrive
- **Message Attributes**: Metadata stored with messages for additional context (up to 10 attributes per message)

---

## 🚀 Extension Tasks

If you complete the main tasks, try these additional challenges:
1. Create a FIFO queue with message deduplication
2. Implement a dead letter queue for handling failed message processing
3. Add long polling support to your message receiving function
4. Create a producer-consumer pattern with multiple scripts
5. Implement batch operations for sending and deleting messages

---

## 🙏 Acknowledgments

Amazon SQS is a fundamental building block for creating loosely coupled, distributed systems in AWS.

Happy queueing! 📩🐍
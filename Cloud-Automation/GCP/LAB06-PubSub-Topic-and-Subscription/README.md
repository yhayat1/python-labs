# GCP LAB06 - Automate Pub/Sub Topic and Subscription with Python

In this lab, you'll use Python to create a Pub/Sub topic and a subscription, publish messages, and pull them from the queue — all using the `google-cloud-pubsub` library.

---

## 🎯 Objectives

By the end of this lab, you will:
- Create a Pub/Sub topic using Python
- Subscribe to the topic with a pull subscription
- Publish and retrieve messages

---

## 🧰 Prerequisites

- GCP project with billing enabled
- Pub/Sub API enabled
- Service account with Pub/Sub Editor role
- Python 3.8+ and `google-cloud-pubsub` installed

---

## 📁 Lab Files

```
Cloud-Automation/GCP/LAB06-PubSub-Topic-and-Subscription/
├── pubsub_script.py
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

1. Set your service account credentials:
```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your-service-account.json"
```

2. Navigate to the lab folder:
```bash
cd Cloud-Automation/GCP/LAB06-PubSub-Topic-and-Subscription/
```

3. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate
```

4. Install dependencies:
```bash
pip install google-cloud-pubsub
pip freeze > requirements.txt
```

---

## ✍️ Your Task

### 1. Create a topic and subscription:
```python
from google.cloud import pubsub_v1

project_id = "your-project-id"
topic_id = "devops-topic"
sub_id = "devops-subscription"

publisher = pubsub_v1.PublisherClient()
subscriber = pubsub_v1.SubscriberClient()\n
topic_path = publisher.topic_path(project_id, topic_id)
publisher.create_topic(request={"name": topic_path})
print(f"Topic created: {topic_path}")

sub_path = subscriber.subscription_path(project_id, sub_id)
subscriber.create_subscription(request={"name": sub_path, "topic": topic_path})
print(f"Subscription created: {sub_path}")
```

### 2. Publish and pull messages:
```python
publisher.publish(topic_path, b"Hello from Pub/Sub")
response = subscriber.pull(request={"subscription": sub_path, "max_messages": 1})
for msg in response.received_messages:
    print("Received:", msg.message.data.decode())
    subscriber.acknowledge(request={"subscription": sub_path, "ack_ids": [msg.ack_id]})
```

---

## 🧪 Validation Checklist

✅ Topic and subscription created  
✅ Message published and pulled successfully  
✅ Script runs without error:
```bash
python pubsub_script.py
```

---

## 🧹 Cleanup
Delete the subscription and topic after testing:
```python
subscriber.delete_subscription(request={"subscription": sub_path})
publisher.delete_topic(request={"topic": topic_path})
```

---

## 💬 What's Next?
Advance to [GCP LAB07 - Cloud SQL Instance Automation](../LAB07-Cloud-SQL-Instance-Automation/) to provision and interact with relational databases.

---

## 🙏 Acknowledgments
Pub/Sub is the backbone of event-driven architecture in GCP. Automating it brings your applications one step closer to full cloud integration.

Push, pull, and automate! ☁️📨🐍


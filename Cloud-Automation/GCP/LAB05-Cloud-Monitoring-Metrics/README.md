# GCP LAB05 - Retrieve Cloud Monitoring Metrics with Python

In this lab, you'll use Python and the Google Cloud Monitoring API to access real-time metrics from your GCP services. This is a key skill for visibility, alerting, and health monitoring in cloud-native environments.

---

## 🎯 Objectives

By the end of this lab, you will:
- Authenticate with the Cloud Monitoring API
- Query metrics for a specific GCP service (e.g., Compute Engine)
- Display time series data in a readable format

---

## 🧰 Prerequisites

- GCP project with Compute Engine or another monitored resource
- Cloud Monitoring API enabled
- Service account with Monitoring Viewer role
- Python 3.8+ and `google-cloud-monitoring` installed

---

## 📁 Lab Files

```
Cloud-Automation/GCP/LAB05-Cloud-Monitoring-Metrics/
├── fetch_metrics.py
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

1. Set credentials:
```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your-service-account.json"
```

2. Navigate to the lab folder:
```bash
cd Cloud-Automation/GCP/LAB05-Cloud-Monitoring-Metrics/
```

3. Create virtual environment and install:
```bash
python -m venv .venv
source .venv/bin/activate
pip install google-cloud-monitoring
pip freeze > requirements.txt
```

---

## ✍️ Your Task

### 1. Fetch metrics from Cloud Monitoring:
```python
from google.cloud import monitoring_v3
from datetime import datetime, timedelta

project_id = "your-project-id"
client = monitoring_v3.MetricServiceClient()
project_name = f"projects/{project_id}"

interval = monitoring_v3.TimeInterval()
interval.end_time.seconds = int(datetime.utcnow().timestamp())
interval.start_time.seconds = int((datetime.utcnow() - timedelta(minutes=10)).timestamp())

results = client.list_time_series(
    request={
        "name": project_name,
        "filter": 'metric.type="compute.googleapis.com/instance/cpu/utilization"',
        "interval": interval,
        "view": monitoring_v3.ListTimeSeriesRequest.TimeSeriesView.FULL
    }
)

for result in results:
    print(result.metric.labels, result.points[0].value)
```

---

## 🧪 Validation Checklist

✅ API authentication successful  
✅ Metric data retrieved for the last 10 minutes  
✅ Script displays data for CPU usage or other monitored metric  
✅ Script runs without error:
```bash
python fetch_metrics.py
```

---

## 🧹 Cleanup
No resources are created. No cleanup needed.

---

## 💬 What's Next?
Move to [GCP LAB06 - Pub/Sub Topic and Subscription](../LAB06-PubSub-Topic-and-Subscription/) to start working with event-driven messaging.

---

## 🙏 Acknowledgments
Cloud Monitoring ensures your cloud is healthy and observable. This lab brings metrics closer to your DevOps tools.

Monitor everything! 📊☁️🐍


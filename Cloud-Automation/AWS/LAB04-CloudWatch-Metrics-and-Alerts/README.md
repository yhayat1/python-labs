# AWS LAB04 - Monitor CloudWatch Metrics and Create Alerts with Python (boto3)

This lab guides you through collecting EC2 metrics and setting up an alarm using AWS CloudWatch via Python. Monitoring is a core DevOps skill, and automating it is even better.

---

## 🎯 Objectives

By the end of this lab, you will:
- Use Python and `boto3` to retrieve CloudWatch metrics
- Create a CloudWatch alarm for CPU usage on an EC2 instance
- List alarms and their statuses

---

## 🧰 Prerequisites

- AWS account with EC2 and CloudWatch permissions
- A running EC2 instance (or create one in LAB01)
- Python 3.8+ and `boto3` installed

---

## 📁 Lab Files

```
Cloud-Automation/AWS/LAB04-CloudWatch-Metrics-and-Alerts/
├── monitor.py
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

1. Navigate to the lab folder:
```bash
cd Cloud-Automation/AWS/LAB04-CloudWatch-Metrics-and-Alerts/
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

### 1. Get metrics for an instance:
```python
import boto3

client = boto3.client('cloudwatch')
instance_id = 'your-ec2-instance-id'

response = client.get_metric_statistics(
    Namespace='AWS/EC2',
    MetricName='CPUUtilization',
    Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
    StartTime=datetime.utcnow() - timedelta(minutes=60),
    EndTime=datetime.utcnow(),
    Period=300,
    Statistics=['Average']
)

for point in response['Datapoints']:
    print("CPU Usage:", point['Average'])
```

### 2. Create a CPU alarm:
```python
client.put_metric_alarm(
    AlarmName='HighCPUAlert',
    MetricName='CPUUtilization',
    Namespace='AWS/EC2',
    Statistic='Average',
    Period=300,
    EvaluationPeriods=1,
    Threshold=70.0,
    ComparisonOperator='GreaterThanThreshold',
    Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
    AlarmActions=[],  # Add ARN of SNS topic if needed
    ActionsEnabled=False  # Change to True if you add actions
)
print("Alarm created!")
```

---

## 🧪 Validation Checklist

✅ Metrics retrieved for a running EC2 instance  
✅ CloudWatch alarm created successfully  
✅ Alarm listed in CloudWatch console or via script  
✅ Script runs without error:
```bash
python monitor.py
```

---

## 🧹 Cleanup
Delete the alarm after testing:
```python
client.delete_alarms(AlarmNames=['HighCPUAlert'])
```

---

## 💬 What's Next?
Advance to [AWS LAB05 - Lambda Deployment](../LAB05-Lambda-Deployment/) to start working with serverless functions.

---

## 🙏 Acknowledgments
Automated monitoring ensures visibility and helps prevent downtime. DevOps teams rely on CloudWatch to alert before things break.

Happy monitoring! 📊🐍
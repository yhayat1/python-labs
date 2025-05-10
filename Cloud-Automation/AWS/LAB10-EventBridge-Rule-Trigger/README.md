# AWS LAB10 - Create EventBridge Rule and Trigger with Python (boto3)

Amazon EventBridge allows you to respond to events in your AWS environment. In this lab, you’ll create a scheduled rule that triggers a Lambda function using Python.

---

## 🎯 Objectives

By the end of this lab, you will:
- Create an EventBridge rule with a schedule expression
- Set up a target (e.g., Lambda function) for the rule
- Enable and manage rule configurations using Python

---

## 🧰 Prerequisites

- AWS account with EventBridge and Lambda permissions
- A deployed Lambda function (from LAB05 or create one manually)
- Python 3.8+ and `boto3` installed

---

## 📁 Lab Files

```
Cloud-Automation/AWS/LAB10-EventBridge-Rule-Trigger/
├── create_rule.py
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

1. Navigate to the lab folder:
```bash
cd Cloud-Automation/AWS/LAB10-EventBridge-Rule-Trigger/
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

### Complete all TODOs in [eventbridge_script.py](./eventbridge_script.py)
### Solutions can be found in [solutions.md](./solutions.md)

---

## 🧪 Validation Checklist

✅ Rule created and set to trigger every minute  
✅ Target Lambda function attached  
✅ Rule and target visible in AWS Console  
✅ Script runs without error:
```bash
python create_rule.py
```

---

## 🧹 Cleanup
Remove rule and target:
```python
eventbridge.remove_targets(Rule=rule_name, Ids=['1'])
eventbridge.delete_rule(Name=rule_name)
```

---

## 💬 Congratulations!
You've completed all 10 AWS labs. You're now ready to automate tasks, monitor systems, and respond to events — all with Python!

---

## 🙏 Acknowledgments
EventBridge enables event-driven automation. Mastering it with Python means you're thinking like a modern cloud-native engineer.

Happy triggering! 🕒🐍


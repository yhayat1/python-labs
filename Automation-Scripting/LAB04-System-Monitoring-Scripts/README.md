# LAB04 - System Monitoring Scripts with Python

System monitoring helps keep your infrastructure healthy and responsive. In this lab, you'll create a Python script that collects and displays key system metrics using the `psutil` library.

---

## 🎯 Objectives

By the end of this lab, you will:
- Use the `psutil` library to gather CPU, memory, and disk metrics
- Display real-time stats in a readable format
- Understand the value of lightweight monitoring tools

---

## 🧰 Prerequisites

- Completion of LAB03 (Process Logs and Reports)
- Python 3.8+ and `psutil` installed

---

## 📁 Lab Files

```
Automation-Scripting/LAB04-System-Monitoring-Scripts/
├── monitor.py
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

1. Navigate to the lab folder:
```bash
cd Automation-Scripting/LAB04-System-Monitoring-Scripts/
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install `psutil`:
```bash
pip install psutil
pip freeze > requirements.txt
```

---

## ✍️ Your Task

### 1. Collect system stats using `psutil`:
```python
import psutil

print("CPU Usage (%):", psutil.cpu_percent(interval=1))
print("Memory Usage (%):", psutil.virtual_memory().percent)
print("Disk Usage (%):", psutil.disk_usage('/').percent)
```

### 2. (Optional) Display metrics in a loop:
```python
import time

while True:
    print("--- System Metrics ---")
    print("CPU:", psutil.cpu_percent(), "%")
    print("RAM:", psutil.virtual_memory().percent, "%")
    print("Disk:", psutil.disk_usage('/').percent, "%")
    time.sleep(5)
```

---

## 🧪 Validation Checklist

✅ Metrics for CPU, RAM, and disk are shown  
✅ Output is user-friendly and updated periodically (if loop used)  
✅ Script runs cleanly:
```bash
python monitor.py
```

---

## 🧹 Cleanup
You can terminate the script with `Ctrl+C`.

---

## 💬 What's Next?
Ready to explore cloud automation? Head to the Cloud Automation section to begin working with AWS, Azure, or GCP via Python SDKs.

---

## 🙏 Acknowledgments
Simple monitoring scripts can provide immense value when setting up alerts or diagnosing issues quickly.

Keep your systems healthy! 💻🐍
# LAB06 - Task Scheduler Automation with Python

Automating recurring tasks is a core DevOps responsibility. In this lab, you'll create a Python script that can schedule and manage automated tasks without relying on external tools like cron or Windows Task Scheduler.

---

## 🎯 Objectives

By the end of this lab, you will:
- Create a Python-based task scheduler using `schedule` library
- Implement different scheduling patterns (daily, hourly, intervals)
- Run multiple tasks concurrently
- Create logs of task execution

---

## 🧰 Prerequisites

- Completion of LAB05 (API Integration Tool)
- Python 3.8+ and the required packages

---

## 📁 Lab Files

```
Automation-Scripting/LAB06-Task-Scheduler-Automation/
├── scheduler.py          # Main scheduler script
├── tasks.py              # Task definitions
├── requirements.txt      # Dependencies
└── README.md
```

---

## 🚀 Getting Started

1. Navigate to the lab folder:
```bash
cd Automation-Scripting/LAB06-Task-Scheduler-Automation/
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install schedule
pip freeze > requirements.txt
```

---

## ✍️ Your Task

### 1. Define some example tasks in tasks.py:
```python
import datetime
import time
import random

def log_event(message):
    """Log a message with timestamp."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")
    
    # Optionally write to a log file
    with open("task_log.txt", "a") as log_file:
        log_file.write(f"[{timestamp}] {message}\n")

def check_system():
    """Simulated system check task."""
    log_event("Performing system check...")
    # Simulate a task that takes some time
    time.sleep(2)
    status = random.choice(["All systems normal", "Warning: High load detected"])
    log_event(f"System check result: {status}")

def backup_data():
    """Simulated backup task."""
    log_event("Starting backup process...")
    # Simulate a time-consuming task
    time.sleep(5)
    log_event("Backup completed successfully")
```

### 2. Create the scheduler in scheduler.py:
```python
import time
import schedule
from tasks import check_system, backup_data, log_event

def setup_schedule():
    """Set up the task schedule."""
    log_event("Setting up task scheduler...")
    
    # Run the system check every hour
    schedule.every(1).hour.do(check_system)
    
    # Run the backup daily at 2 AM
    schedule.every().day.at("02:00").do(backup_data)
    
    # For testing, you might want more frequent runs
    schedule.every(20).seconds.do(lambda: log_event("Heartbeat check"))
    
    log_event("Scheduler initialized successfully")

if __name__ == "__main__":
    setup_schedule()
    
    log_event("Task scheduler started")
    
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        log_event("Task scheduler stopped by user")
```

---

## 🧪 Validation Checklist

✅ Tasks are defined and execute properly  
✅ Scheduler runs and triggers tasks at specified times  
✅ Task execution is properly logged  
✅ Script runs cleanly:
```bash
python scheduler.py
```

---

## 🧹 Cleanup
Press Ctrl+C to stop the scheduler and remove the task_log.txt file if desired.

---

## 💬 What's Next?
Ready to explore cloud automation? Head to the Cloud Automation section to begin working with AWS, Azure, or GCP via Python SDKs.

---

## 🙏 Acknowledgments
Task automation is the foundation of DevOps. Once you master scheduled automation, you can build increasingly sophisticated workflows and pipelines.

Happy scheduling! ⏰🐍 
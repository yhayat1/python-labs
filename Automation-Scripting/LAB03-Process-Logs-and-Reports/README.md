# LAB03 - Process Logs and Generate Reports with Python

Log files contain valuable operational data. In this lab, you'll write Python code to parse a sample log file, extract meaningful information, and generate a summary report.

---

## 🎯 Objectives

By the end of this lab, you will:
- Open and read a text-based log file
- Parse and filter log entries by keyword or pattern
- Summarize occurrences and generate basic metrics
- Write a report to a new file

---

## 🧰 Prerequisites

- Completion of LAB02 (Automate File Downloads)
- Python 3.8+ installed

---

## 📁 Lab Files

```
Automation-Scripting/LAB03-Process-Logs-and-Reports/
├── logs.txt               # Sample input log file
├── parser.py              # Main script
└── README.md
```

---

## 🚀 Getting Started

1. Navigate to the lab folder:
```bash
cd Automation-Scripting/LAB03-Process-Logs-and-Reports/
```

2. (Optional) Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate
```

---

## ✍️ Your Task

### 1. Read and analyze a log file:
```python
with open("logs.txt", "r") as file:
    lines = file.readlines()

error_count = 0
for line in lines:
    if "ERROR" in line:
        error_count += 1

with open("report.txt", "w") as report:
    report.write(f"Total errors found: {error_count}\n")
```

### 2. Extend: Count other log levels like INFO and WARNING

---

## 🧪 Validation Checklist

✅ Reads log file and parses content line-by-line  
✅ Counts error messages or patterns  
✅ Writes a result to `report.txt`  
✅ Script runs cleanly:
```bash
python parser.py
```

---

## 🧹 Cleanup
Remove `report.txt` if desired.

---

## 💬 What's Next?
Move on to [LAB04 - System Monitoring Scripts](../LAB04-System-Monitoring-Scripts/) to collect and display live system metrics.

---

## 🙏 Acknowledgments
Understanding logs is core to diagnosing system behavior and performance. Learn to let Python do the parsing for you!

Happy analyzing! 📊🐍
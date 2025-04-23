# LAB01 - Building a Simple CLI Tool with Python

Command-line interfaces (CLIs) are essential in DevOps. In this lab, you'll create your first CLI tool using Python's built-in `argparse` module. This tool will accept user input from the terminal and perform logic based on it.

---

## 🎯 Objectives

By the end of this lab, you will:
- Understand how to use `argparse` to build command-line tools
- Accept and validate input from the user
- Build a simple calculator CLI that performs actions based on input

---

## 🧰 Prerequisites

- Completion of Core-Python labs
- Python 3.8+ installed

---

## 📁 Lab Files

```
Automation-Scripting/LAB01-Simple-CLI-Tool/
├── cli_tool.py
└── README.md
```

---

## 🚀 Getting Started

1. Navigate to the lab folder:
```bash
cd Automation-Scripting/LAB01-Simple-CLI-Tool/
```

2. (Optional) Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate
```

---

## ✍️ Your Task

### 1. Use argparse to build a CLI:
```python
import argparse

parser = argparse.ArgumentParser(description="Simple CLI Calculator")
parser.add_argument("x", type=int, help="First number")
parser.add_argument("y", type=int, help="Second number")
parser.add_argument("--op", choices=["add", "sub"], default="add", help="Operation to perform")

args = parser.parse_args()

if args.op == "add":
    print("Result:", args.x + args.y)
else:
    print("Result:", args.x - args.y)
```

### 2. Run it from the command line:
```bash
python cli_tool.py 10 5 --op add
python cli_tool.py 10 5 --op sub
```

---

## 🧪 Validation Checklist

✅ CLI accepts and processes user arguments  
✅ Supports at least two operations (`add`, `sub`)  
✅ Script runs successfully from command line

---

## 🧹 Cleanup
No cleanup required.

---

## 💬 What's Next?
Advance to [LAB02 - Automate File Downloads](../LAB02-Automate-File-Downloads/) to write a script that interacts with the internet and saves data programmatically.

---

## 🙏 Acknowledgments
A great DevOps tool starts at the terminal. CLIs are powerful and can control anything from deployments to monitoring.

Happy scripting! 🖥🐍
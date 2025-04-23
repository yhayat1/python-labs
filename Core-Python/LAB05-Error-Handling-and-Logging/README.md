# LAB05 - Error Handling and Logging in Python

Robust automation scripts handle errors gracefully and log information clearly. In this lab, you'll learn how to catch exceptions and implement logging — essential for real-world DevOps tools.

---

## 🎯 Objectives

By the end of this lab, you will:
- Use `try`, `except`, `finally` blocks to handle errors
- Raise custom exceptions when needed
- Set up and write logs using Python’s `logging` module
- Understand logging levels: DEBUG, INFO, WARNING, ERROR, CRITICAL

---

## 🧰 Prerequisites

- Completion of LAB04 (File Handling)
- Python 3.8+ installed

---

## 📁 Lab Files

```
LAB05-Error-Handling-and-Logging/
├── main.py
├── app.log               # Will be created during execution
└── README.md
```

---

## 🚀 Getting Started

1. Navigate to the lab folder:
```bash
cd Core-Python/LAB05-Error-Handling-and-Logging/
```

2. (Optional) Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate
```

---

## ✍️ Your Task

### 1. Handle a division error:
```python
try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print("Result is:", result)
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input! Please enter a number.")
finally:
    print("Execution completed.")
```

### 2. Set up logging:
```python
import logging
logging.basicConfig(filename="app.log", level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
```

### 3. Log info and errors:
```python
logging.info("Starting the program")
try:
    with open("config.json", "r") as f:
        data = f.read()
except FileNotFoundError as e:
    logging.error(f"File not found: {e}")
```

---

## 🧪 Validation Checklist

✅ Used `try-except-finally` blocks correctly  
✅ Implemented logging and checked output in `app.log`  
✅ Script runs cleanly:
```bash
python main.py
```

---

## 🧹 Cleanup
You may delete `app.log` after testing if you wish.

---

## 💬 What's Next?
Advance to [LAB06 - Object-Oriented Programming](../LAB06-OOP-and-Classes/) to design reusable and structured code using classes.

---

## 🙏 Acknowledgments
Error handling and logging are your best friends when debugging or deploying reliable DevOps tools.

Happy debugging! 🛠🐍


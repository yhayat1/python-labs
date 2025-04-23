# LAB03 - Functions and Modules in Python

Functions and modules are essential to writing reusable and maintainable code. In this lab, you will learn how to define your own functions and organize code into modules — a critical step for DevOps scripting and automation.

---

## 🎯 Objectives

By the end of this lab, you will:
- Create and call custom Python functions
- Understand function parameters and return values
- Learn how to split your code across multiple files (modules)
- Use Python’s built-in and custom modules

---

## 🧰 Prerequisites

- Completion of LAB02 (Loops and Conditions)
- Python 3.8+ installed

---

## 📁 Lab Files

```
LAB03-Functions-and-Modules/
├── main.py
├── helper.py              # Your custom module
└── README.md
```

---

## 🚀 Getting Started

1. Navigate to the lab folder:
```bash
cd Core-Python/LAB03-Functions-and-Modules/
```

2. (Optional) Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate
```

---

## ✍️ Your Task

### 1. Define Functions in `helper.py`:
```python
def greet(name):
    return f"Hello, {name}!"

def add(x, y):
    return x + y
```

### 2. Use These Functions in `main.py`:
```python
from helper import greet, add

print(greet("DevOps Learner"))
print("Sum:", add(5, 3))
```

### 3. Bonus: Add a Utility Function
In `helper.py`, create a new function that returns the max of 3 numbers:
```python
def max_of_three(a, b, c):
    return max(a, b, c)
```

Then call it in `main.py`:
```python
print("Max value:", max_of_three(7, 14, 9))
```

---

## 🧪 Validation Checklist

✅ Functions are defined and used properly  
✅ `import` is used to access another file  
✅ Script runs without error using:
```bash
python main.py
```

---

## 🧹 Cleanup
No cleanup needed for this lab.

---

## 💬 What's Next?
Head over to [LAB04 - File Handling](../LAB04-File-Handling/) and learn how to read from and write to files — a key part of automation.

---

## 🙏 Acknowledgments
Reusable code saves time and effort. By organizing your functions and logic cleanly, you're setting up a strong foundation for DevOps tooling.

Happy modularizing! 🧩🐍


# LAB07 - Virtual Environments and Python Packaging

Virtual environments allow you to manage dependencies for your projects in isolation. In this lab, you'll learn how to use `venv` and `pip`, create a `requirements.txt`, and build a basic Python package.

---

## 🎯 Objectives

By the end of this lab, you will:
- Create and activate a Python virtual environment
- Install and freeze dependencies with `pip`
- Understand the structure of a basic Python package
- Generate and use `requirements.txt`

---

## 🧰 Prerequisites

- Completion of LAB06 (OOP and Classes)
- Python 3.8+ installed

---

## 📁 Lab Files

```
LAB07-Virtualenv-and-Packaging/
├── myproject/
│   ├── __init__.py
│   └── core.py
├── main.py
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

1. Navigate to the lab folder:
```bash
cd Core-Python/LAB07-Virtualenv-and-Packaging/
```

2. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install a third-party package (e.g., `requests`):
```bash
pip install requests
```

4. Freeze dependencies:
```bash
pip freeze > requirements.txt
```

---

## ✍️ Your Task

### 1. Create a reusable module:
In `myproject/core.py`:
```python
def say_hello(name):
    return f"Hello, {name}!"
```

### 2. Use it in `main.py`:
```python
from myproject.core import say_hello
print(say_hello("DevOps"))
```

---

## 🧪 Validation Checklist

✅ Created and activated a virtual environment  
✅ Installed and froze at least one dependency  
✅ Created a reusable Python module and imported it  
✅ Script runs cleanly:
```bash
python main.py
```

---

## 🧹 Cleanup
You may remove the `.venv` directory or `__pycache__` after testing.

---

## 💬 What's Next?
Check out [LAB08 - Unit Testing Basics](../LAB08-Unit-Testing-Basics/) to ensure your code is reliable and testable.

---

## 🙏 Acknowledgments
Isolated environments and packaging are fundamental for clean DevOps workflows, CI/CD pipelines, and reproducible automation.

Happy packaging! 📦🐍


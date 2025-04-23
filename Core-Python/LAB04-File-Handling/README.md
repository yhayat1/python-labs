# LAB04 - File Handling in Python

Reading from and writing to files is a fundamental part of automation. In this lab, you'll learn how to handle files using Python — a skill that's essential for log parsing, configuration management, and system monitoring.

---

## 🎯 Objectives

By the end of this lab, you will:
- Open and read from text files
- Write and append to files
- Use `with` blocks to manage file context safely
- Handle basic file errors gracefully

---

## 🧰 Prerequisites

- Completion of LAB03 (Functions and Modules)
- Python 3.8+ installed

---

## 📁 Lab Files

```
LAB04-File-Handling/
├── main.py
├── input.txt             # A sample input file
└── README.md
```

---

## 🚀 Getting Started

1. Navigate to the lab folder:
```bash
cd Core-Python/LAB04-File-Handling/
```

2. (Optional) Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate
```

---

## ✍️ Your Task

### 1. Read the file content:
```python
with open("input.txt", "r") as file:
    content = file.read()
    print("File Content:\n", content)
```

### 2. Write to a new file:
```python
with open("output.txt", "w") as file:
    file.write("This is a new file created by Python!\n")
```

### 3. Append to the same file:
```python
with open("output.txt", "a") as file:
    file.write("Adding another line.\n")
```

### 4. Handle FileNotFoundError:
```python
try:
    with open("missing.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found!")
```

---

## 🧪 Validation Checklist

✅ You read from `input.txt` and printed its content  
✅ You wrote and appended to `output.txt`  
✅ You handled a missing file with a `try-except` block  
✅ Script runs cleanly using:
```bash
python main.py
```

---

## 🧹 Cleanup
You may remove any temporary `.txt` files after running the lab if desired.

---

## 💬 What's Next?
Go to [LAB05 - Error Handling and Logging](../LAB05-Error-Handling-and-Logging/) to make your scripts more robust and production-ready.

---

## 🙏 Acknowledgments
File I/O is the bridge between your code and the real world — from processing logs to managing config files.

Happy coding! 📁🐍


# LAB02 - Python Basics: Loops and Conditional Logic

In this lab, you'll learn how to control the flow of your Python programs using loops and conditionals. These are fundamental building blocks for writing powerful automation scripts.

---

## 🎯 Objectives

By the end of this lab, you will:
- Use `if`, `elif`, and `else` to control logic based on conditions
- Write `for` and `while` loops
- Combine loops with lists and dictionaries
- Practice real-world scenarios with decision logic

---

## 🧰 Prerequisites

- Completion of LAB01 (Variables and Data Types)
- Python 3.8+ installed

---

## 📁 Lab Files

```
LAB02-Loops-and-Conditions/
├── main.py
└── README.md
```

---

## 🚀 Getting Started

1. Navigate to the lab folder:
```bash
cd Core-Python/LAB02-Loops-and-Conditions/
```

2. (Optional) Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate
```

---

## ✍️ Your Task

Open `main.py` and complete the following exercises:

### 1. Conditional Statements:
```python
age = 20
if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")
```

### 2. Loop Over a List:
```python
skills = ["Python", "Bash", "Docker"]
for skill in skills:
    print("Learning:", skill)
```

### 3. Use a While Loop:
```python
counter = 0
while counter < 3:
    print("Counter is:", counter)
    counter += 1
```

### 4. Bonus: Loop with Conditional Logic
```python
users = ["admin", "guest", "devops"]
for user in users:
    if user == "admin":
        print("Welcome, administrator!")
    else:
        print(f"Hello, {user}!")
```

---

## 🧪 Validation Checklist

✅ `if`/`elif`/`else` blocks correctly executed  
✅ Loops iterate over lists or variables correctly  
✅ Conditional logic is used inside loops  
✅ Script runs without errors:
```bash
python main.py
```

---

## 🧹 Cleanup
Nothing to clean up — this lab is run locally.

---

## 💬 What's Next?
Continue to [LAB03 - Functions and Modules](../LAB03-Functions-and-Modules/) to learn how to organize and reuse your Python code.

---

## 🙏 Acknowledgments
This lab was crafted to give you practical, real-world experience with decision-making logic and control flow — the backbone of automation.

Happy scripting! 🔁🐍


# LAB01 - Python Basics: Variables and Data Types

Welcome to your first Python lab! In this beginner-friendly exercise, you'll explore how to define variables and work with basic data types in Python. This is the foundation for all Python programming and scripting you'll do as a DevOps engineer.

---

## 🎯 Objectives

By the end of this lab, you will:
- Understand what variables are and how to create them
- Learn the most common Python data types: `int`, `float`, `str`, `bool`, `list`, and `dict`
- Write and run your first Python script
- Practice using the `print()` function and basic operations

---

## 🧰 Prerequisites

- Python 3.8+ installed
- Basic understanding of the terminal
- Code editor (VSCode recommended)

---

## 📁 Lab Files

```
LAB01-Basics-Variables/
├── main.py                # Your primary Python script
└── README.md              # This file
```

---

## 🚀 Getting Started

1. **Navigate to the lab folder:**
   ```bash
   cd Core-Python/LAB01-Basics-Variables/
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. **Open `main.py` and start coding!**

---

## ✍️ Your Task

Edit the `main.py` file to include the following:

### 1. Create variables of different types:
```python
name = "DevOps Learner"
age = 25
height = 1.75
is_hungry = True
skills = ["Python", "Git", "Linux"]
profile = {"name": name, "age": age, "skills": skills}
```

### 2. Print them using `print()`:
```python
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Hungry:", is_hungry)
print("Skills:", skills)
print("Profile Dictionary:", profile)
```

### 3. Try basic operations:
```python
print("Age in 5 years:", age + 5)
print("Number of skills:", len(skills))
print("First skill:", skills[0])
```

---

## 🧪 Validation Checklist

✅ You created variables using different data types  
✅ You printed the variables with context using `print()`  
✅ You used indexing, `len()`, and arithmetic operations  
✅ Script runs without error using:
```bash
python main.py
```

---

## 🧹 Cleanup
No cleanup needed — this is a local Python script.

---

## 💬 What's Next?
Proceed to [LAB02 - Loops and Conditions](../LAB02-Loops-and-Conditions/) to learn how to control your program’s flow!

---

## 🙏 Acknowledgments
This lab was designed for beginners starting their DevOps journey. Mastering the basics is key to building powerful automation and cloud tools in the future.

Happy coding! 🐍


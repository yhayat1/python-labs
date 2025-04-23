# LAB06 - Object-Oriented Programming (OOP) in Python

In this lab, you’ll be introduced to classes, objects, and methods — the core concepts of Object-Oriented Programming (OOP). OOP helps organize large automation tools and services in a clean and scalable way.

---

## 🎯 Objectives

By the end of this lab, you will:
- Understand what classes and objects are
- Define methods and attributes
- Instantiate objects and use class methods
- Apply inheritance and encapsulation (basic)

---

## 🧰 Prerequisites

- Completion of LAB05 (Error Handling and Logging)
- Python 3.8+ installed

---

## 📁 Lab Files

```
LAB06-OOP-and-Classes/
├── main.py
└── README.md
```

---

## 🚀 Getting Started

1. Navigate to the lab folder:
```bash
cd Core-Python/LAB06-OOP-and-Classes/
```

2. (Optional) Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate
```

---

## ✍️ Your Task

### 1. Create a class with attributes and methods:
```python
class Server:
    def __init__(self, name, ip):
        self.name = name
        self.ip = ip

    def ping(self):
        print(f"Pinging server {self.name} at {self.ip}...")
```

### 2. Instantiate and use the class:
```python
srv = Server("web01", "192.168.1.10")
srv.ping()
```

### 3. Inherit from the class:
```python
class DatabaseServer(Server):
    def __init__(self, name, ip, engine):
        super().__init__(name, ip)
        self.engine = engine

    def backup(self):
        print(f"Backing up {self.engine} database on {self.name}")
```

### 4. Use the derived class:
```python
db = DatabaseServer("db01", "192.168.1.11", "PostgreSQL")
db.ping()
db.backup()
```

---

## 🧪 Validation Checklist

✅ Defined at least one class with methods and attributes  
✅ Instantiated objects and used methods  
✅ Demonstrated inheritance  
✅ Script runs cleanly:
```bash
python main.py
```

---

## 🧹 Cleanup
No cleanup required.

---

## 💬 What's Next?
Head to [LAB07 - Virtualenv and Packaging](../LAB07-Virtualenv-and-Packaging/) to learn how to manage dependencies and share your code.

---

## 🙏 Acknowledgments
OOP helps you think like a system designer. By structuring code with classes, you’ll be better prepared for building DevOps platforms and automation frameworks.

Happy class-building! 🧱🐍


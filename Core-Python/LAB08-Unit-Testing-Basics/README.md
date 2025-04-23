# LAB08 - Unit Testing Basics in Python

Writing tests ensures your automation scripts work as expected and remain reliable. In this lab, you'll learn how to write unit tests using Python’s built-in `unittest` module.

---

## 🎯 Objectives

By the end of this lab, you will:
- Write simple unit tests using `unittest`
- Understand test assertions: `assertEqual`, `assertTrue`, etc.
- Run tests from the command line
- Follow basic test structure and naming conventions

---

## 🧰 Prerequisites

- Completion of LAB07 (Virtualenv and Packaging)
- Python 3.8+ installed

---

## 📁 Lab Files

```
LAB08-Unit-Testing-Basics/
├── main.py               # Business logic
├── test_main.py          # Unit tests
└── README.md
```

---

## 🚀 Getting Started

1. Navigate to the lab folder:
```bash
cd Core-Python/LAB08-Unit-Testing-Basics/
```

2. (Optional) Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate
```

---

## ✍️ Your Task

### 1. Write some logic in `main.py`:
```python
def add(a, b):
    return a + b

def is_even(n):
    return n % 2 == 0
```

### 2. Test it in `test_main.py`:
```python
import unittest
from main import add, is_even

class TestMain(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_is_even(self):
        self.assertTrue(is_even(2))
        self.assertFalse(is_even(3))

if __name__ == '__main__':
    unittest.main()
```

---

## 🧪 Validation Checklist

✅ Functions defined in `main.py`  
✅ Corresponding tests written in `test_main.py`  
✅ Tests run successfully using:
```bash
python -m unittest test_main.py
```

---

## 🧹 Cleanup
No cleanup required. Files are local.

---

## 💬 What's Next?
Move on to the **Automation-Scripting** section to begin applying your Python knowledge to DevOps scenarios!

---

## 🙏 Acknowledgments
Testing builds confidence. Writing tests now will save hours of debugging in real-world projects.

Happy testing! ✅🐍


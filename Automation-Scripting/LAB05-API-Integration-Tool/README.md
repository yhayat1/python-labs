# LAB05 - API Integration Tool with Python

APIs (Application Programming Interfaces) are fundamental to modern DevOps. In this lab, you'll create a Python tool that interacts with a public REST API, processes the data, and performs actions based on the results.

---

## 🎯 Objectives

By the end of this lab, you will:
- Make HTTP requests to a REST API using the `requests` library
- Parse and work with JSON responses
- Handle API authentication and error responses
- Create a reusable API client class

---

## 🧰 Prerequisites

- Completion of LAB04 (System Monitoring Scripts)
- Python 3.8+ and `requests` installed

---

## 📁 Lab Files

```
Automation-Scripting/LAB05-API-Integration-Tool/
├── api_client.py         # Main script with the API integration
├── config.py             # Configuration settings
├── requirements.txt      # Dependencies
└── README.md
```

---

## 🚀 Getting Started

1. Navigate to the lab folder:
```bash
cd Automation-Scripting/LAB05-API-Integration-Tool/
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install requests
pip freeze > requirements.txt
```

---

## ✍️ Your Task

### 1. Create a configuration file (config.py):
```python
# API Settings
API_BASE_URL = "https://jsonplaceholder.typicode.com"
API_TIMEOUT = 10  # seconds

# Optional API Auth (for APIs that require it)
# API_KEY = "your_api_key_here"
```

### 2. Create an API client class in api_client.py:
```python
import requests
from config import API_BASE_URL, API_TIMEOUT

class APIClient:
    def __init__(self):
        self.base_url = API_BASE_URL
        self.timeout = API_TIMEOUT
    
    def get_users(self):
        """Fetch users from the API"""
        response = requests.get(
            f"{self.base_url}/users", 
            timeout=self.timeout
        )
        response.raise_for_status()  # Raise exception for HTTP errors
        return response.json()
    
    # Add more methods for other API endpoints
```

### 3. Use the API client to fetch and display data:
```python
if __name__ == "__main__":
    client = APIClient()
    
    try:
        users = client.get_users()
        print(f"Found {len(users)} users:")
        for user in users[:5]:  # Show just first 5 users
            print(f"  - {user['name']} ({user['email']})")
    except requests.exceptions.RequestException as e:
        print(f"API Error: {e}")
```

---

## 🧪 Validation Checklist

✅ API client successfully connects to the API  
✅ JSON responses are properly parsed and displayed  
✅ Error handling is implemented for API failures  
✅ Script runs cleanly:
```bash
python api_client.py
```

---

## 🧹 Cleanup
No cleanup required, all operations are read-only.

---

## 💬 What's Next?
Proceed to [LAB06 - Task Scheduler Automation](../LAB06-Task-Scheduler-Automation/) to learn how to schedule and automate recurring tasks with Python.

---

## 🙏 Acknowledgments
API integration is a cornerstone skill for DevOps engineers—whether connecting to monitoring services, CI/CD pipelines, or cloud providers.

Happy integrating! 🔌🐍 
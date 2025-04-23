# LAB02 - Automate File Downloads with Python

In this lab, you will write a script to download files from the internet. This type of automation is useful for fetching logs, backups, or even binary artifacts in DevOps workflows.

---

## 🎯 Objectives

By the end of this lab, you will:
- Use the `requests` module to download files via HTTP
- Save files to disk using Python
- Handle response status and file naming

---

## 🧰 Prerequisites

- Completion of LAB01 (Simple CLI Tool)
- Python 3.8+ and `requests` installed

---

## 📁 Lab Files

```
Automation-Scripting/LAB02-Automate-File-Downloads/
├── downloader.py
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

1. Navigate to the lab folder:
```bash
cd Automation-Scripting/LAB02-Automate-File-Downloads/
```

2. Create a virtual environment and install dependencies:
```bash
python -m venv .venv
source .venv/bin/activate
pip install requests
```

3. Optionally save dependencies:
```bash
pip freeze > requirements.txt
```

---

## ✍️ Your Task

### 1. Write a download script:
```python
import requests

def download_file(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"File saved as {filename}")
    else:
        print("Failed to download. Status:", response.status_code)

# Example usage
download_file("https://www.example.com/sample.txt", "sample.txt")
```

---

## 🧪 Validation Checklist

✅ Script downloads a file from a given URL  
✅ File is saved locally with correct content  
✅ HTTP status handling is implemented  
✅ Runs without error:
```bash
python downloader.py
```

---

## 🧹 Cleanup
You may delete any downloaded files after the lab.

---

## 💬 What's Next?
Explore [LAB03 - Process Logs and Reports](../LAB03-Process-Logs-and-Reports/) to practice parsing and summarizing data from downloaded files.

---

## 🙏 Acknowledgments
Automation isn’t just about infrastructure — data fetching and scripting are just as essential.

Happy downloading! 📥🐍
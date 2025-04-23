# Python Development & Cloud Automation Labs

A practical, hands-on collection of labs that combine **Python development** with **cloud automation** across **AWS**, **Azure**, and **GCP**.

This repository complements our Terraform-based labs by enabling learners to build **automation scripts**, **microservices**, and **cloud-native tools** in Python — laying the foundation for infrastructure and application automation using code.

---

## 📦 About This Repository

These labs are ideal for learners who want to:
- Build real-world **Python tools** that automate cloud workflows
- Learn how to **interact with cloud APIs** using SDKs like `boto3`, `azure-mgmt`, and `google-cloud`
- Write **robust, scalable, and testable** Python scripts and services
- Bridge the gap between **development** and **operations** using Python

---

## 📁 Repository Structure

```bash
python-labs/
│
├── AWS/                         # AWS-focused Python labs
│   ├── LAB01-EC2-Automation/
│   ├── LAB02-S3-File-Upload/
│   └── ...
│
├── Azure/                       # Azure-focused Python labs
│   ├── LAB01-VM-Management/
│   ├── LAB02-Blob-Storage-Automation/
│   └── ...
│
├── GCP/                         # GCP-focused Python labs
│   ├── LAB01-Instance-Creation/
│   ├── LAB02-GCS-Automation/
│   └── ...
│
└── Common/                      # Shared utilities and documentation
    └── SDK-Setup.md             # Setup instructions for cloud SDKs
```

Each lab folder includes:
- Python scripts (`main.py`, `utils.py`, etc.)
- `README.md` with lab objectives, usage, and cleanup
- Optional: `requirements.txt`, `config.yaml`, or `env.example`

---

## 🧰 Prerequisites

To complete these labs, you'll need:
- Python 3.8+ with `pip` or `venv`
- A cloud account (AWS, Azure, or GCP)
- SDK credentials configured (environment variables or auth file)
- Basic terminal and Git knowledge

---

## 🚀 How to Use These Labs

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-org>/python-labs.git
   cd python-labs
   ```

2. Navigate to a lab folder (e.g., `AWS/LAB01-EC2-Automation/`)

3. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Run the Python script:
   ```bash
   python main.py
   ```

6. Follow the lab `README.md` for instructions and validation steps.

---

## 📈 Learning Progression

Labs are designed to evolve Python automation skills in stages:

- **Beginner**: Cloud SDK setup, API calls, scripting basics
- **Intermediate**: CLI tools, environment automation, stateful tasks
- **Advanced**: Microservices, event-driven automation, observability, serverless

---

## 🌐 Lab Roadmap

See the [Python Labs Roadmap](./ROADMAP.md) for a full list of labs, categories, and upcoming additions.

---

## 🤝 Contributing

We welcome your contributions! Whether it's bug fixes, lab ideas, or new automation workflows:

1. Fork the repo
2. Create a branch (`feature/lab-name`)
3. Add your lab under the relevant cloud provider
4. Submit a pull request with lab description and test steps

---

## 🙏 Acknowledgments

- Python.org
- AWS `boto3`, Azure SDK for Python, Google Cloud Client Libraries
- DevOps and Python community contributors

---

## 🧠 Automate Smartly

Whether you're writing a one-off script or building a full-blown automation service, these Python labs will equip you to **code cloud automation confidently and creatively**.

Happy coding! 🐍☁️

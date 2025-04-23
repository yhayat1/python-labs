# Azure LAB08 - Automate Virtual Network Setup with Python

In this lab, you'll use Python to create a Virtual Network (VNet) and subnet in Azure. This foundational skill enables secure and segmented cloud deployments.

---

## 🎯 Objectives

By the end of this lab, you will:
- Create a virtual network using Azure SDK
- Configure address spaces and subnet ranges
- Understand Azure networking components

---

## 🧰 Prerequisites

- Azure subscription
- Python 3.8+ and the following packages:
  - `azure-mgmt-network`
  - `azure-identity`

---

## 📁 Lab Files

```
Cloud-Automation/Azure/LAB08-Virtual-Network-Setup/
├── create_vnet.py
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

1. Set environment variables for authentication:
```bash
export AZURE_CLIENT_ID="<your-client-id>"
export AZURE_CLIENT_SECRET="<your-client-secret>"
export AZURE_TENANT_ID="<your-tenant-id>"
export AZURE_SUBSCRIPTION_ID="<your-subscription-id>"
```

2. Navigate to the lab directory:
```bash
cd Cloud-Automation/Azure/LAB08-Virtual-Network-Setup/
```

3. Set up a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate
pip install azure-mgmt-network azure-identity
pip freeze > requirements.txt
```

---

## ✍️ Your Task

### 1. Create a VNet and subnet:
```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.network import NetworkManagementClient
import os

subscription_id = os.environ['AZURE_SUBSCRIPTION_ID']
resource_group = 'devops-lab-rg'
location = 'eastus'
vnet_name = 'devops-vnet'
subnet_name = 'devops-subnet'

credential = DefaultAzureCredential()
network_client = NetworkManagementClient(credential, subscription_id)

vnet_params = {
    "location": location,
    "address_space": {
        "address_prefixes": ["10.1.0.0/16"]
    },
    "subnets": [{
        "name": subnet_name,
        "address_prefix": "10.1.0.0/24"
    }]
}

network_client.virtual_networks.begin_create_or_update(
    resource_group,
    vnet_name,
    vnet_params
).result()

print("Virtual Network and Subnet created successfully.")
```

---

## 🧪 Validation Checklist

✅ Virtual network and subnet created  
✅ Address spaces defined and accessible  
✅ Script runs without error:
```bash
python create_vnet.py
```

---

## 🧹 Cleanup
```bash
az network vnet delete --name devops-vnet --resource-group devops-lab-rg
```

---

## 💬 What's Next?
Move to [Azure LAB09 - CosmosDB Document Management](../LAB09-CosmosDB-Document-Management/) to automate NoSQL operations.

---

## 🙏 Acknowledgments
VNets are the heart of cloud networking. Automating them ensures secure and repeatable setups.

Provision safely, automate confidently! 🌐☁️🐍
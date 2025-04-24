# AWS LAB06 - Automate CloudFormation Stack Launch with Python (boto3)

CloudFormation lets you define your infrastructure as code. In this lab, you'll use Python to programmatically deploy a CloudFormation template using `boto3`.

---

## 🎯 Objectives

By the end of this lab, you will:
- Use Python to launch a CloudFormation stack
- Deploy a simple EC2 instance using a template
- Monitor stack creation status
- Configure stack parameters through an INI file
- Handle stack updates and deployments

---

## 🧰 Prerequisites

- AWS account with CloudFormation and EC2 permissions
- Python 3.8+ and `boto3` installed

---

## 📁 Lab Files

```
Cloud-Automation/AWS/LAB06-CloudFormation-Stack-Launch/
├── launch_stack.py        # Scaffolded file for students to complete
├── deploy_stack.py        # Reference implementation with advanced features
├── ec2_template.yaml      # CloudFormation template file for EC2 instance
├── config.ini             # Configuration file for stack parameters
└── README.md
```

---

## 🚀 Getting Started

1. Navigate to the lab folder:
```bash
cd Cloud-Automation/AWS/LAB06-CloudFormation-Stack-Launch/
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install required packages:
```bash
pip install boto3 configparser
pip freeze > requirements.txt
```

4. Review configuration settings:
```bash
# The default AWS region is set to eu-west-1 (Ireland)
# Make sure to update subnet and VPC IDs in config.ini before deploying
```

---

## ✍️ Your Task

### 1. Examine the CloudFormation Template
Review the provided `ec2_template.yaml` file to understand the EC2 instance and security group configuration. Note how parameters are defined and how resources reference each other.

### 2. Review the Configuration File
Examine `config.ini` to see how stack parameters are configured outside the code for better separation of concerns.

**Important**: Before deploying, students must update:
- VPC ID - replace `subnet-12345678` with a valid subnet ID
- Subnet ID - replace `vpc-12345678` with a valid VPC ID
- KeyName - replace `my-demo-key` with an existing EC2 key pair name

### 3. Complete the `launch_stack.py` Script
Fill in the TODOs in the `launch_stack.py` file to:
- Read the CloudFormation template 
- Create a CloudFormation client
- Deploy the stack with proper parameters
- Monitor stack creation progress
- Implement stack deletion functionality

### 4. Optional: Study the Reference Implementation
For advanced concepts, examine `deploy_stack.py` which includes:
- Comprehensive error handling
- Stack update capabilities
- Configuration file parsing
- Stack output retrieval
- Status monitoring with proper waits

---

## 🧪 Validation Checklist

✅ Configuration file properly set up  
✅ Stack launched successfully with parameters from config  
✅ Stack status monitored until completion  
✅ Stack outputs retrieved and displayed  
✅ Script handles errors gracefully
✅ Stack can be deleted cleanly

---

## 🧹 Cleanup
Delete the stack to avoid ongoing AWS charges:
```bash
python launch_stack.py --delete
```

Or add deletion code to your script:
```python
cf.delete_stack(StackName='DevOpsEC2Stack')
print("Stack deletion initiated")
```

**Important**: AWS resources like EC2 instances will continue to incur charges until explicitly deleted. Always clean up your resources after completing the lab to avoid unexpected costs.

---

## 💬 What's Next?
Next: [AWS LAB07 - DynamoDB Table Automation](../LAB07-DynamoDB-Table-Automation/) to learn how to automate NoSQL databases in the cloud.

---

## 🙏 Acknowledgments
Using CloudFormation with Python empowers you to scale infrastructure as code with precision and control.

Happy stacking! 🏗🐍
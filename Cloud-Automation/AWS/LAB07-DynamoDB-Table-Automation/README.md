# AWS LAB07 - DynamoDB Table Automation with Python (boto3)

This lab guides you through creating a Python script to automate DynamoDB table operations using the AWS SDK for Python (Boto3). You'll implement various DynamoDB operations including table creation, item insertion, retrieval, and table deletion.

---

## 🎯 Objectives

By the end of this lab, you will:
- Understand how to use boto3 to interact with DynamoDB
- Learn to create and manage DynamoDB tables programmatically
- Implement basic CRUD operations for DynamoDB items
- Practice handling AWS SDK exceptions
- Learn about DynamoDB's data model and indexing

---

## 🧰 Prerequisites

- AWS account with appropriate permissions
- Python 3.8+ installed
- AWS CLI configured with appropriate credentials

---

## 📁 Lab Files

```
Cloud-Automation/AWS/LAB07-DynamoDB-Table-Automation/
├── dynamodb_script.py
├── requirements.txt
├── README.md
└── solution_reference.py (reference only)
```

---

## 🚀 Getting Started

1. Navigate to the lab folder:
```bash
cd Cloud-Automation/AWS/LAB07-DynamoDB-Table-Automation/
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Verify your AWS credentials are configured:
```bash
aws configure list
```

---

## ✍️ Your Task

The script `dynamodb_script.py` contains skeleton functions with TODOs that you need to implement:

1. Complete the `create_table()` function to create a DynamoDB table with a partition key
2. Implement `wait_for_table_creation()` to poll the table status until it becomes active
3. Code the `list_tables()` function to list all DynamoDB tables in your account
4. Fill in the `insert_item()` function to add an item to the table
5. Complete the `get_item()` function to retrieve an item based on its key
6. Implement `delete_table()` to remove a DynamoDB table

---

## 🧪 Validation Checklist

✅ Run the script to test your implementation:
```bash
python dynamodb_script.py
```

✅ The script should:
- Create a DynamoDB table named 'DevOpsUsers' (default)
- Wait for the table to become active
- List all tables in your account
- Insert a sample item
- Retrieve the item from the table

✅ Try running with custom parameters:
```bash
python dynamodb_script.py --table-name MyCustomTable --region us-east-1
```

---

## 🧹 Cleanup

When you're done with the lab, clean up resources to avoid charges:
```bash
python dynamodb_script.py --cleanup
```

---

## 💬 What's Next?

Try [AWS LAB08 - SNS Topic and Subscription](../LAB08-SNS-Topic-and-Subscription/) to learn about messaging services.

---

## 📚 DynamoDB Key Concepts

- **Partition Key**: Unique identifier for items in the table
- **Provisioned Throughput**: Read and write capacity units
- **Table Status**: Tables transition through states like CREATING, UPDATING, ACTIVE
- **Item Operations**: How to put, get, update, and delete items
- **Error Handling**: Handling common DynamoDB exceptions

---

## 🚀 Extension Tasks

If you complete the main tasks, try these additional challenges:
1. Add update_item functionality to modify existing items
2. Implement batch operations to insert or retrieve multiple items at once
3. Add a secondary (sort) key to the table for more complex data modeling
4. Implement a scan operation to retrieve items without knowing the key
5. Add support for conditional operations when inserting or updating items

---

## 🙏 Acknowledgments

DynamoDB automation is fundamental for building scalable, serverless applications in AWS.

Happy NoSQL automating! 📊🐍
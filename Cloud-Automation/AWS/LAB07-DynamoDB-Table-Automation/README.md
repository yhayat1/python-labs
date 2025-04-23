# AWS LAB07 - Automate DynamoDB Table Creation with Python (boto3)

In this lab, you’ll learn how to create and interact with a DynamoDB table using Python. This is a great introduction to NoSQL database automation in AWS.

---

## 🎯 Objectives

By the end of this lab, you will:
- Create a DynamoDB table using `boto3`
- Insert and retrieve items
- List tables and describe table structure

---

## 🧰 Prerequisites

- AWS account with DynamoDB permissions
- Python 3.8+ and `boto3` installed

---

## 📁 Lab Files

```
Cloud-Automation/AWS/LAB07-DynamoDB-Table-Automation/
├── dynamodb_script.py
├── requirements.txt
└── README.md
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

3. Install dependencies:
```bash
pip install boto3
pip freeze > requirements.txt
```

---

## ✍️ Your Task

### 1. Create a table:
```python
import boto3

dynamodb = boto3.client('dynamodb')

table_name = 'DevOpsUsers'

dynamodb.create_table(
    TableName=table_name,
    KeySchema=[
        {'AttributeName': 'username', 'KeyType': 'HASH'}
    ],
    AttributeDefinitions=[
        {'AttributeName': 'username', 'AttributeType': 'S'}
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)
print("Table created.")
```

### 2. Add and retrieve an item:
```python
resource = boto3.resource('dynamodb')
table = resource.Table(table_name)

# Add an item
table.put_item(Item={'username': 'alice', 'role': 'admin'})

# Get the item
response = table.get_item(Key={'username': 'alice'})
print("Retrieved:", response.get('Item'))
```

---

## 🧪 Validation Checklist

✅ Table created successfully  
✅ Data inserted and retrieved  
✅ Script runs cleanly:
```bash
python dynamodb_script.py
```

---

## 🧹 Cleanup
```python
dynamodb.delete_table(TableName=table_name)
```

---

## 💬 What's Next?
Move on to [AWS LAB08 - SNS Topic and Subscription](../LAB08-SNS-Topic-and-Subscription/) to automate messaging and notifications.

---

## 🙏 Acknowledgments
DynamoDB is a key NoSQL tool in AWS. Automating it with Python helps you build dynamic and scalable systems.

Happy table-building! 🗃🐍
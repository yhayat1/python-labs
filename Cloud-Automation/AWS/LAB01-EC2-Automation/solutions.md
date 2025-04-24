# LAB01 - EC2 Automation: Solutions

This document contains the complete solution for the EC2 Instance Launch Automation lab exercise. Use this file as a reference only after attempting to solve the lab exercises on your own.

## Solution for launch_ec2.py

```python
#!/usr/bin/env python3
"""
AWS LAB01 - EC2 Instance Launch Automation

This script demonstrates how to use boto3 to launch an EC2 instance in AWS.
It covers basic EC2 instance creation with tags and waiting for the instance to be ready.

Usage:
    python launch_ec2.py
"""

import boto3
import time
from botocore.exceptions import ClientError

# Initialize the EC2 resource with specified region
ec2 = boto3.resource('ec2', region_name='eu-west-1')

# Define instance parameters
AMI_ID = 'ami-0fe0b2cf0e1f25c8a'  # Amazon Linux 2023 AMI in eu-west-1
INSTANCE_TYPE = 't2.micro'
KEY_NAME = 'devops-key'  # Replace with your key pair name
SECURITY_GROUP_ID = 'sg-xxxxxxxxxxxx'  # Replace with your security group ID

# Tags to identify your instance
INSTANCE_TAGS = [
    {
        'Key': 'Name',
        'Value': 'DevOps-Lab-Instance'
    },
    {
        'Key': 'Environment',
        'Value': 'Training'
    },
    {
        'Key': 'Project',
        'Value': 'AWS-Automation'
    }
]

def launch_instance():
    """
    Launch an EC2 instance with defined parameters
    
    Returns:
        ec2.Instance: The created EC2 instance object
    """
    try:
        # Create a new EC2 instance
        instances = ec2.create_instances(
            ImageId=AMI_ID,
            InstanceType=INSTANCE_TYPE,
            KeyName=KEY_NAME,
            SecurityGroupIds=[SECURITY_GROUP_ID] if SECURITY_GROUP_ID else None,
            MinCount=1,
            MaxCount=1,
            TagSpecifications=[
                {
                    'ResourceType': 'instance',
                    'Tags': INSTANCE_TAGS
                }
            ]
        )
        
        instance = instances[0]
        print(f"Launched EC2 instance: {instance.id}")
        
        return instance
    except ClientError as e:
        print(f"Error launching EC2 instance: {e}")
        return None

def wait_for_instance(instance):
    """
    Wait for the instance to be in a running state
    
    Args:
        instance (ec2.Instance): EC2 instance object
    """
    try:
        print("Waiting for instance to start running...")
        instance.wait_until_running()
        
        # Reload the instance to get the updated attributes
        instance.reload()
        
        print("Instance is now running!")
        return True
    except ClientError as e:
        print(f"Error waiting for instance: {e}")
        return False

def display_instance_details(instance):
    """
    Print useful details about the instance
    
    Args:
        instance (ec2.Instance): EC2 instance object
    """
    print("\nInstance Details:")
    print(f"  Instance ID: {instance.id}")
    print(f"  Instance State: {instance.state['Name']}")
    print(f"  Instance Type: {instance.instance_type}")
    print(f"  AMI ID: {instance.image_id}")
    print(f"  Public DNS: {instance.public_dns_name}")
    print(f"  Public IP: {instance.public_ip_address}")
    print(f"  Private IP: {instance.private_ip_address}")
    
    # Print the instance tags
    print("\nInstance Tags:")
    for tag in instance.tags:
        print(f"  {tag['Key']}: {tag['Value']}")

def terminate_instance(instance):
    """
    Terminate an EC2 instance
    
    Args:
        instance (ec2.Instance): EC2 instance object
    """
    try:
        instance.terminate()
        print(f"\nTerminating instance: {instance.id}")
        print("Waiting for instance to terminate...")
        
        # Wait for the instance to terminate
        instance.wait_until_terminated()
        print("Instance terminated successfully.")
        
        return True
    except ClientError as e:
        print(f"Error terminating instance: {e}")
        return False

if __name__ == "__main__":
    print("AWS EC2 Instance Launch Tool")
    print("===========================")
    
    # Launch a new EC2 instance
    instance = launch_instance()
    
    if instance:
        # Wait for the instance to be running
        if wait_for_instance(instance):
            # Display instance details
            display_instance_details(instance)
            
            # Provide SSH connection command if the instance has a public DNS
            if instance.public_dns_name:
                print(f"\nTo connect to your instance via SSH:")
                print(f"ssh -i /path/to/{KEY_NAME}.pem ec2-user@{instance.public_dns_name}")
        
        # Warning about charges
        print("\n⚠️  IMPORTANT: Remember to terminate this instance when done to avoid charges!")
        print("To terminate the instance, uncomment the terminate_instance call below or use the AWS console.")
        
        # Uncomment the line below to terminate the instance automatically
        # terminate_instance(instance)
```

## Key Learning Points

1. **AWS SDK Setup**:
   - Using boto3 to interact with AWS services
   - Initializing an EC2 resource with a specific region

2. **EC2 Instance Creation**:
   - Configuring instance parameters: AMI ID, instance type, key pair, etc.
   - Adding tags for resource identification and organization
   - Using security groups to control network access

3. **Resource Monitoring**:
   - Using waiters to poll for resource state changes
   - Reloading resources to get updated attributes

4. **Error Handling**:
   - Implementing try/except blocks to handle AWS API errors
   - Using ClientError from botocore.exceptions

5. **Resource Management**:
   - Creating helpful utility functions for common operations
   - Properly terminating resources to avoid unexpected charges

## Common Issues and Troubleshooting

1. **Missing Credentials**:
   - Error when AWS credentials are not configured
   - Solution: Set up AWS CLI with `aws configure` or use environment variables

2. **Permission Issues**:
   - Error when your IAM user lacks EC2 permissions
   - Solution: Attach appropriate policies to your IAM user or role

3. **Resource Availability**:
   - Error when instance type is not available in the selected region
   - Solution: Choose a different instance type or region

4. **Key Pair Access**:
   - Unable to connect to instance if key pair is not specified correctly
   - Solution: Ensure you have the private key file (.pem) for the specified key pair

5. **Security Group Configuration**:
   - Unable to connect to instance if security group doesn't allow SSH access
   - Solution: Update security group to allow inbound traffic on port 22 
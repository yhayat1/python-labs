#!/usr/bin/env python3
"""
AWS LAB01 - EC2 Instance Launch Automation

This script demonstrates how to use boto3 to launch an EC2 instance in AWS.
It covers basic EC2 instance creation with tags and waiting for the instance to be running.

Usage:
    python launch_ec2.py
"""

# TODO: Import the boto3 library and botocore exceptions
# import boto3
# from botocore.exceptions import ClientError
# import time


# TODO: Set up EC2 client
# Initialize the EC2 client using boto3.client('ec2', region_name='eu-west-1')


# TODO: Define instance parameters
# You can define variables for your instance parameters here:
# - AMI ID (Amazon Linux 2023 AMI in eu-west-1): ami-0fe0b2cf0e1f25c8a
# - Instance type (e.g., t2.micro)
# - Key pair name (for SSH access)
# - Security Group IDs (optional)
# - Tags to identify your instance


# TODO: Launch the EC2 instance
# Use ec2_client.run_instances() with appropriate parameters
# Remember to capture the response to get instance information


# TODO: Wait for the instance to be running
# Use ec2_client.describe_instances() to check instance status
# Implement a polling mechanism with time.sleep()


# TODO: Print instance details
# Show useful information about the instance:
# - Instance ID
# - Public DNS name
# - Public IP address
# - Current state


# TODO: (Advanced) Add error handling
# Implement try/except blocks to handle potential errors:
# - ClientError for AWS API errors
# - Other exceptions for network issues, etc.


# TODO: (Optional) Add a function to terminate the instance
# Create a function that terminates the instance and waits for termination


if __name__ == "__main__":
    print("AWS EC2 Instance Launch Tool")
    print("===========================")
    
    # TODO: Implement your EC2 launch code here
    # Example outline:
    # 1. Set up EC2 client
    # 2. Launch instance with parameters
    # 3. Wait for instance to be running
    # 4. Display instance details
    
    # Print reminder for cleanup to avoid charges
    print("\n⚠️  IMPORTANT: Remember to terminate this instance when done to avoid charges!")
    print("To terminate, you can use the AWS console or modify this script to add termination code.")
    print("\nTo terminate via Python, use:")
    print("ec2_client.terminate_instances(InstanceIds=['i-instance-id'])")

"""
Sample output:

AWS EC2 Instance Launch Tool
===========================
Launching instance...
Waiting for instance to be running...
Instance is now running!

Instance Details:
ID:         i-0abc123def456789
Public DNS: ec2-12-34-56-78.compute-1.amazonaws.com
Public IP:  12.34.56.78
State:      running

⚠️  IMPORTANT: Remember to terminate this instance when done to avoid charges!
To terminate, you can use the AWS console or modify this script to add termination code.

To terminate via Python, use:
ec2_client.terminate_instances(InstanceIds=['i-0abc123def456789'])
""" 
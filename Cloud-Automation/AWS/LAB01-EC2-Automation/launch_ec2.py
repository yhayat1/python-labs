#!/usr/bin/env python3
"""
AWS LAB01 - EC2 Instance Launch Automation

This script demonstrates how to use boto3 to launch an EC2 instance in AWS.
It covers basic EC2 instance creation with tags and waiting for the instance to be ready.

Usage:
    python launch_ec2.py
"""

# TODO: Import the boto3 library
# import boto3


# TODO: Set up EC2 resource
# Initialize the EC2 resource using boto3.resource('ec2', region_name='eu-west-1')


# TODO: Define instance parameters
# You can define variables for your instance parameters here:
# - AMI ID (Amazon Linux 2023 AMI in eu-west-1): ami-0fe0b2cf0e1f25c8a
# - Instance type (e.g., t2.micro)
# - Key pair name (for SSH access)
# - Security Group IDs (optional)
# - Tags to identify your instance


# TODO: Launch the EC2 instance
# Use ec2.create_instances() with appropriate parameters
# Remember to store the returned instance object


# TODO: Wait for the instance to be running
# Use instance.wait_until_running() to wait for the instance to start
# Then reload instance details with instance.reload()


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


if __name__ == "__main__":
    print("AWS EC2 Instance Launch Tool")
    print("===========================")
    
    # TODO: Implement your EC2 launch code here
    # Example outline:
    # 1. Set up EC2 resource
    # 2. Launch instance with parameters
    # 3. Wait for instance to be running
    # 4. Display instance details
    
    # Print reminder for cleanup to avoid charges
    print("\n⚠️  IMPORTANT: Remember to terminate this instance when done to avoid charges!")
    print("To terminate, you can use the AWS console or modify this script to add termination code.")
    print("\nTo terminate via Python, use:")
    print("instance.terminate()")

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
instance.terminate()
""" 
#!/usr/bin/env python3
"""
AWS LAB03 - IAM User and Policy Automation

This script demonstrates how to use boto3 to create IAM users and attach policies.
It covers creating users, attaching managed policies, and creating custom policies.

Usage:
    python create_iam_user.py
"""

# TODO: Import the boto3 library
# import boto3
# You may also want to import json for policy document formatting


# TODO: Define the IAM user parameters
# Set the username for the new IAM user
# Example: username = 'devops-lab-user'


# TODO: Initialize IAM client
# Use boto3.client('iam', region_name='eu-west-1') to create an IAM client


# TODO: Create IAM user
# Use iam.create_user() to create a new user
# Print confirmation message with user details


# TODO: Attach a managed policy
# Define the ARN of a managed policy (e.g., AmazonS3ReadOnlyAccess)
# Use iam.attach_user_policy() to attach the policy to the user
# Example policy ARN: 'arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess'


# TODO: (Optional) Create and attach a custom inline policy
# Define a custom policy document as a Python dictionary
# Convert the policy to JSON and attach it to the user
# Use iam.put_user_policy()


# TODO: List IAM users
# Use iam.list_users() to get all users
# Print the username of each user


# TODO: List policies attached to the user
# Use iam.list_attached_user_policies() to see attached managed policies
# Use iam.list_user_policies() to see inline policies


# TODO: Add error handling
# Implement try/except blocks to handle common IAM errors:
# - EntityAlreadyExists
# - NoSuchEntity
# - Other boto3 exceptions


if __name__ == "__main__":
    print("AWS IAM User and Policy Automation")
    print("=================================")
    
    # TODO: Implement your IAM automation code here
    # Example flow:
    # 1. Create IAM user
    # 2. Attach managed policy
    # 3. (Optional) Create inline policy
    # 4. List users to verify creation
    # 5. List attached policies
    
    # Print cleanup instructions
    print("\n⚠️  IMPORTANT: For cleanup, remember to:")
    print("1. Detach all policies from the user")
    print("2. Delete any inline policies")
    print("3. Delete the user")
    print("\nCleanup code example:")
    print("iam.detach_user_policy(UserName='username', PolicyArn='policy_arn')")
    print("iam.delete_user(UserName='username')")

"""
Sample output:

AWS IAM User and Policy Automation
=================================
Creating user: devops-lab-user
User created successfully: devops-lab-user

Attaching policy: AmazonS3ReadOnlyAccess
Policy attached successfully

Creating custom inline policy: DevopsCustomAccess
Custom policy attached successfully

Listing all IAM users:
- admin
- devops-lab-user
- other-existing-user

Policies attached to devops-lab-user:
- Managed policies:
  * AmazonS3ReadOnlyAccess
- Inline policies:
  * DevopsCustomAccess

⚠️  IMPORTANT: For cleanup, remember to:
1. Detach all policies from the user
2. Delete any inline policies
3. Delete the user

Cleanup code example:
iam.detach_user_policy(UserName='username', PolicyArn='policy_arn')
iam.delete_user(UserName='username')
""" 
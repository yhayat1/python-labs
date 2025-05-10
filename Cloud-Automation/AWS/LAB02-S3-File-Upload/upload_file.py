#!/usr/bin/env python3
"""
AWS LAB02 - S3 File Upload Automation

This script demonstrates how to use boto3 to upload files to an Amazon S3 bucket using the client SDK.
It shows how to set metadata, control access permissions, and list objects in a bucket.

Usage:
    python upload_file.py
"""

# TODO: Import the boto3 library and botocore exceptions
# import boto3
# from botocore.exceptions import ClientError


# TODO: Configure S3 connection parameters
# Define your bucket name, file path, and S3 object key
# Example:
# bucket_name = 'your-bucket-name'  # Replace with your actual bucket name
# file_name = 'sample.txt'          # Local file to upload
# s3_key = 'uploads/sample.txt'     # Destination path in S3


# TODO: Initialize S3 client
# Use boto3.client('s3', region_name='eu-west-1')


# TODO: Upload file to S3
# Use s3_client.upload_file() to upload the file
# 
# Example:
# s3_client.upload_file(
#     file_name,            # Local file path
#     bucket_name,          # S3 bucket name
#     s3_key,               # S3 object key
#     ExtraArgs={           # Optional extra arguments
#         'ACL': 'public-read',
#         'ContentType': 'text/plain',
#         'Metadata': {
#             'Creator': 'DevOps-Lab'
#         }
#     }
# )


# TODO: List objects in the bucket
# Use s3_client.list_objects_v2() to list objects
# Parse the response and print out object keys
# 
# Example:
# response = s3_client.list_objects_v2(Bucket=bucket_name)
# for obj in response.get('Contents', []):
#     print(f" - {obj['Key']}")


# TODO: (Advanced) Add error handling
# Implement try/except blocks to handle potential errors:
# - ClientError for AWS API errors
# - FileNotFoundError if the local file doesn't exist
# - Other exceptions for network issues, etc.


# TODO: (Optional) Add a function to check if an object exists
# Create a function that checks if an object exists in the bucket before uploading


if __name__ == "__main__":
    print("AWS S3 File Upload Tool")
    print("======================")
    
    # TODO: Implement your S3 upload code here
    # Example outline:
    # 1. Set up S3 client
    # 2. Upload file with desired parameters
    # 3. List objects in the bucket to verify
    
    # Print reminder for cleanup to avoid unnecessary storage costs
    print("\n⚠️  NOTE: Don't forget to delete objects if they're no longer needed!")
    print("To delete via Python, use:")
    print("s3_client.delete_object(Bucket=bucket_name, Key=s3_key)")

"""
Sample output:

AWS S3 File Upload Tool
======================
Uploading sample.txt to S3 bucket: your-bucket-name
Upload successful! File available at: https://your-bucket-name.s3.amazonaws.com/uploads/sample.txt

Objects in bucket:
- uploads/sample.txt
- other-existing-file.jpg
- another-file.pdf

⚠️  NOTE: Don't forget to delete objects if they're no longer needed!
To delete via Python, use:
s3_client.delete_object(Bucket=bucket_name, Key=s3_key)
""" 
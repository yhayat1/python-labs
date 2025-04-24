#!/usr/bin/env python3
"""
AWS LAB02 - S3 File Upload Automation

This script demonstrates how to use boto3 to upload files to an Amazon S3 bucket.
It shows how to set metadata, control access permissions, and list objects in a bucket.

Usage:
    python upload_file.py
"""

# TODO: Import the boto3 library
# import boto3


# TODO: Configure S3 connection parameters
# Define your bucket name, file path, and S3 object key
# Example:
# bucket_name = 'your-bucket-name'  # Replace with your actual bucket name
# file_name = 'sample.txt'          # Local file to upload
# s3_key = 'uploads/sample.txt'     # Destination path in S3


# TODO: Initialize S3 client or resource
# Use boto3.client('s3', region_name='eu-west-1') or boto3.resource('s3', region_name='eu-west-1')


# TODO: Upload file to S3
# Use the appropriate method to upload the file:
# - With client: s3.upload_file()
# - With resource: s3_object.upload_file()
# 
# Consider adding ExtraArgs for:
# - ACL (Access Control List)
# - ContentType
# - Metadata


# TODO: List objects in the bucket
# Use s3.list_objects_v2() or another appropriate method
# Print out the keys of objects found in the bucket


# TODO: (Advanced) Add error handling
# Implement try/except blocks to handle potential errors:
# - ClientError for AWS API errors
# - FileNotFoundError if the local file doesn't exist
# - Other exceptions for network issues, etc.


if __name__ == "__main__":
    print("AWS S3 File Upload Tool")
    print("======================")
    
    # TODO: Implement your S3 upload code here
    # Example outline:
    # 1. Set up S3 client/resource
    # 2. Upload file with desired parameters
    # 3. List objects in the bucket to verify
    
    # Print reminder for cleanup to avoid unnecessary storage costs
    print("\n⚠️  NOTE: Don't forget to delete objects if they're no longer needed!")
    print("To delete via Python, use:")
    print("s3.delete_object(Bucket=bucket_name, Key=s3_key)")

"""
Sample output:

AWS S3 File Upload Tool
======================
Uploading sample.txt to S3 bucket: your-bucket-name
Upload successful! File available at: s3://your-bucket-name/uploads/sample.txt

Objects in bucket:
- uploads/sample.txt
- other-existing-file.jpg
- another-file.pdf

⚠️  NOTE: Don't forget to delete objects if they're no longer needed!
To delete via Python, use:
s3.delete_object(Bucket=bucket_name, Key=s3_key)
""" 
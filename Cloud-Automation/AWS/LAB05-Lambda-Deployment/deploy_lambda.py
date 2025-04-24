#!/usr/bin/env python3
"""
AWS LAB05 - Lambda Deployment Script

This script demonstrates how to package and deploy an AWS Lambda function using boto3.
It creates a zip file from the Lambda function code and deploys it to AWS.

Usage:
    python deploy_lambda.py
"""

# TODO: Import necessary libraries
# import boto3
# import zipfile
# import os
# import json
# from botocore.exceptions import ClientError


# TODO: Configure Lambda deployment parameters
# function_name = 'MyDevOpsLambda'
# lambda_handler = 'lambda_function.lambda_handler'
# runtime = 'python3.9'  # Use a supported Python runtime
# region = 'eu-west-1'  # Use Ireland region by default
# 
# # The IAM role ARN needs to be replaced with a valid role that has Lambda execution permissions
# role_arn = 'arn:aws:iam::your-account-id:role/lambda-execute-role'
# 
# # Timeout and memory settings
# timeout = 10
# memory_size = 128


# TODO: Function to package the Lambda code into a zip file
# def create_deployment_package(source_file):
#     """Create a zip file containing the Lambda function code"""
#     zip_name = "function.zip"
#     with zipfile.ZipFile(zip_name, 'w') as zip_file:
#         zip_file.write(source_file)
#     return zip_name


# TODO: Function to create/update the Lambda function
# def deploy_lambda_function(function_name, zip_file, handler, role_arn, runtime, timeout, memory_size):
#     """Create or update the Lambda function in AWS"""
#     client = boto3.client('lambda', region_name='eu-west-1')
#     # rest of the function...


# TODO: Function to invoke the Lambda function
# def invoke_lambda_function(function_name):
#     """Invoke the Lambda function and return the response"""


# TODO: Function to delete the Lambda function (for cleanup)
# def delete_lambda_function(function_name):
#     """Delete the Lambda function from AWS"""


# TODO: Error handling functions
# def handle_error(e, operation):
#     """Handle boto3 errors with detailed output"""


if __name__ == "__main__":
    print("AWS Lambda Function Deployment Tool")
    print("=================================")
    
    # TODO: Main workflow
    # Try to use a try/except structure to handle errors gracefully
    # 1. Create the deployment package (zip file)
    # 2. Deploy the Lambda function (create or update)
    # 3. Invoke the function to test it
    # 4. Display the result
    
    # Example implementation
    # try:
    #     print(f"\nPackaging Lambda function...")
    #     zip_file = create_deployment_package('lambda_function.py')
    #     
    #     print(f"\nDeploying Lambda function '{function_name}'...")
    #     function_arn = deploy_lambda_function(function_name, zip_file, lambda_handler, role_arn, runtime, timeout, memory_size)
    #     
    #     print(f"\nTesting Lambda function...")
    #     response = invoke_lambda_function(function_name)
    #     
    #     print(f"\nLambda Response:")
    #     print(json.dumps(json.loads(response['Payload'].read().decode('utf-8')), indent=2))
    #     
    #     # Cleanup the zip file
    #     os.remove(zip_file)
    #     
    # except Exception as e:
    #     print(f"\nError: {str(e)}")
    
    print("\n⚠️  CLEANUP: Remember to delete the Lambda function when you're done!")
    print("Use: python deploy_lambda.py --delete")
    print("Or programmatically: client.delete_function(FunctionName='MyDevOpsLambda')")

"""
Sample output:

AWS Lambda Function Deployment Tool
=================================

Packaging Lambda function...
Created deployment package: function.zip

Deploying Lambda function 'MyDevOpsLambda'...
Function deployed successfully!
ARN: arn:aws:lambda:us-east-1:123456789012:function:MyDevOpsLambda

Testing Lambda function...
Function invoked successfully!

Lambda Response:
{
  "statusCode": 200,
  "body": "Hello from Lambda! This function was deployed using Python and boto3."
}

⚠️  CLEANUP: Remember to delete the Lambda function when you're done!
Use: python deploy_lambda.py --delete
Or programmatically: client.delete_function(FunctionName='MyDevOpsLambda')
""" 
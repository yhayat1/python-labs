#!/usr/bin/env python3
"""
CloudFormation Stack Deployment Script
This script automates the deployment of AWS CloudFormation stacks using a configuration file.
"""

import boto3
import configparser
import json
import sys
import os
import time
from botocore.exceptions import ClientError

def load_config(config_file='config.ini'):
    """Load configuration from config file"""
    if not os.path.exists(config_file):
        print(f"Error: Configuration file '{config_file}' not found.")
        sys.exit(1)
        
    config = configparser.ConfigParser()
    config.read(config_file)
    return config

def load_template(template_file):
    """Load CloudFormation template from file"""
    try:
        with open(template_file, 'r') as file:
            return file.read()
    except Exception as e:
        print(f"Error loading template file: {e}")
        sys.exit(1)

def get_stack_parameters(config):
    """Extract stack parameters from config"""
    parameters = []
    if 'PARAMETERS' in config:
        for key, value in config['PARAMETERS'].items():
            parameters.append({
                'ParameterKey': key,
                'ParameterValue': value
            })
    return parameters

def get_stack_tags(config):
    """Extract stack tags from config"""
    tags = []
    if 'TAGS' in config:
        for key, value in config['TAGS'].items():
            tags.append({
                'Key': key,
                'Value': value
            })
    return tags

def create_update_stack(cf_client, stack_name, template_body, parameters, tags, capabilities):
    """Create or update CloudFormation stack"""
    stack_exists = False
    
    # Check if stack exists
    try:
        cf_client.describe_stacks(StackName=stack_name)
        stack_exists = True
        print(f"Stack {stack_name} exists. Attempting update...")
    except ClientError as e:
        if "does not exist" in str(e):
            stack_exists = False
            print(f"Stack {stack_name} does not exist. Creating new stack...")
        else:
            print(f"Error checking stack: {e}")
            sys.exit(1)
    
    # Create params dict for boto3 call
    stack_params = {
        'StackName': stack_name,
        'TemplateBody': template_body,
        'Parameters': parameters,
        'Tags': tags
    }
    
    # Add capabilities if specified
    if capabilities:
        stack_params['Capabilities'] = capabilities.split(',')
    
    try:
        if stack_exists:
            # Update existing stack
            response = cf_client.update_stack(**stack_params)
            print(f"Updating stack {stack_name}...")
            wait_for_stack(cf_client, stack_name, 'update')
        else:
            # Create new stack
            response = cf_client.create_stack(**stack_params)
            print(f"Creating stack {stack_name}...")
            wait_for_stack(cf_client, stack_name, 'create')
        
        return response
    except ClientError as e:
        if "No updates are to be performed" in str(e):
            print("No changes detected in the template. Stack is up to date.")
            return None
        else:
            print(f"Error: {e}")
            sys.exit(1)

def wait_for_stack(cf_client, stack_name, operation):
    """Wait for stack operation to complete and print progress"""
    print(f"Waiting for stack {operation} to complete...")
    waiter_type = f"stack_{operation}_complete"
    waiter = cf_client.get_waiter(waiter_type)
    
    try:
        # Poll every 5 seconds, print status every 10 seconds
        start_time = time.time()
        poll_interval = 5
        status_interval = 10
        last_status_time = start_time
        
        while True:
            # Check current status
            stacks = cf_client.describe_stacks(StackName=stack_name)
            status = stacks['Stacks'][0]['StackStatus']
            
            current_time = time.time()
            # Print status every 10 seconds
            if current_time - last_status_time >= status_interval:
                print(f"Current status: {status} (Time elapsed: {int(current_time - start_time)}s)")
                last_status_time = current_time
            
            # Check if stack is in a terminal state
            if (operation == 'create' and status == 'CREATE_COMPLETE') or \
               (operation == 'update' and status == 'UPDATE_COMPLETE'):
                break
            
            # Check for failure states
            if 'FAILED' in status or 'ROLLBACK' in status:
                print(f"Stack operation failed with status: {status}")
                print_stack_events(cf_client, stack_name)
                sys.exit(1)
            
            time.sleep(poll_interval)
            
    except ClientError as e:
        print(f"Error waiting for stack completion: {e}")
        sys.exit(1)
        
    print(f"Stack {operation} completed successfully!")

def print_stack_events(cf_client, stack_name, limit=10):
    """Print recent stack events, focusing on failures"""
    try:
        print("\nRecent stack events:")
        events = cf_client.describe_stack_events(StackName=stack_name)['StackEvents']
        
        # Focus on recent events, especially failures
        count = 0
        for event in events:
            if count >= limit:
                break
            
            # Always show failure events
            if 'FAILED' in event['ResourceStatus']:
                reason = event.get('ResourceStatusReason', 'No reason provided')
                print(f"FAILED: {event['LogicalResourceId']} - {reason}")
                count += 1
            # Show other events up to the limit
            elif count < limit:
                print(f"{event['Timestamp'].strftime('%H:%M:%S')} - {event['LogicalResourceId']} - {event['ResourceStatus']}")
                count += 1
                
    except ClientError as e:
        print(f"Error retrieving stack events: {e}")

def print_stack_outputs(cf_client, stack_name):
    """Print stack outputs"""
    try:
        stacks = cf_client.describe_stacks(StackName=stack_name)
        outputs = stacks['Stacks'][0].get('Outputs', [])
        
        if outputs:
            print("\nStack Outputs:")
            for output in outputs:
                print(f"  {output['OutputKey']}: {output['OutputValue']}")
                if 'Description' in output:
                    print(f"    Description: {output['Description']}")
        else:
            print("\nNo outputs defined for this stack.")
            
    except ClientError as e:
        print(f"Error retrieving stack outputs: {e}")

def validate_config_parameters(config):
    """Validate configuration parameters to ensure they're not using placeholder values"""
    if 'PARAMETERS' not in config:
        return
        
    params = config['PARAMETERS']
    warnings = []
    
    # Check for common placeholder values that should be replaced
    if 'SubnetID' in params and params['SubnetID'] == 'subnet-12345678':
        warnings.append("- SubnetID is still set to the placeholder value 'subnet-12345678'")
    
    if 'VpcID' in params and params['VpcID'] == 'vpc-12345678':
        warnings.append("- VpcID is still set to the placeholder value 'vpc-12345678'")
    
    if 'KeyName' in params and params['KeyName'] == 'my-demo-key':
        warnings.append("- KeyName is still set to the placeholder value 'my-demo-key'")
    
    if warnings:
        print("\n⚠️  WARNING: Configuration contains placeholder values that should be updated:")
        for warning in warnings:
            print(warning)
        print("\nThese values need to be replaced with actual AWS resource IDs before deployment.")
        confirm = input("\nDo you want to continue anyway? (y/n): ")
        if confirm.lower() != 'y':
            print("Deployment cancelled. Please update config.ini with correct values.")
            sys.exit(0)
        print("Continuing with deployment...")

def main():
    """Main function to deploy CloudFormation stack"""
    # Load configuration
    config = load_config()
    
    # Validate configuration parameters
    validate_config_parameters(config)
    
    # Extract AWS configuration
    aws_region = config['AWS']['region']
    aws_profile = config['AWS'].get('profile', None)
    
    # Create boto3 session and client
    session_params = {}
    if aws_profile:
        session_params['profile_name'] = aws_profile
    
    # Handle explicit credentials if provided
    if 'aws_access_key_id' in config['AWS'] and 'aws_secret_access_key' in config['AWS']:
        session_params['aws_access_key_id'] = config['AWS']['aws_access_key_id']
        session_params['aws_secret_access_key'] = config['AWS']['aws_secret_access_key']
    
    session = boto3.Session(**session_params, region_name=aws_region)
    cf_client = session.client('cloudformation')
    
    # Extract stack configuration
    stack_name = config['STACK']['stack_name']
    template_file = config['STACK']['template_file']
    capabilities = config['STACK'].get('capabilities', '')
    
    # Load template and parameters
    template_body = load_template(template_file)
    parameters = get_stack_parameters(config)
    tags = get_stack_tags(config)
    
    # Print deployment info
    print("Deploying CloudFormation Stack:")
    print(f"  Stack Name: {stack_name}")
    print(f"  Template: {template_file}")
    print(f"  Region: {aws_region}")
    
    # Create or update stack
    result = create_update_stack(cf_client, stack_name, template_body, parameters, tags, capabilities)
    
    if result:
        # Print outputs
        print_stack_outputs(cf_client, stack_name)
        print("\nStack deployment completed successfully!")

if __name__ == "__main__":
    main() 
#!/usr/bin/env python3
"""
AWS LAB04 - CloudWatch Metrics and Alerts

This script demonstrates how to use boto3 to monitor EC2 instances using CloudWatch,
retrieve metrics, and set up alarms based on resource utilization thresholds.

Usage:
    python monitor.py
"""

# TODO: Import the required libraries
# import boto3
# from datetime import datetime, timedelta


# TODO: Define the instance ID to monitor
# Replace with your actual EC2 instance ID
# instance_id = 'i-0abc123def456789'


# TODO: Initialize CloudWatch client
# Use boto3.client('cloudwatch', region_name='eu-west-1') to create a CloudWatch client


# TODO: Function to get CPU utilization metrics
# Create a function that retrieves CPU utilization metrics for the specified instance
# Parameters should include:
#   - instance_id: The EC2 instance ID
#   - period: Time period in seconds (e.g., 300 for 5 minutes)
#   - start_time: Starting time for metrics (e.g., 1 hour ago)
#   - end_time: Ending time for metrics (e.g., now)


# TODO: Function to create a CPU utilization alarm
# Create a function that sets up a CloudWatch alarm for high CPU usage
# Parameters should include:
#   - instance_id: The EC2 instance ID
#   - alarm_name: Name for the alarm
#   - threshold: CPU percentage that triggers the alarm
#   - evaluation_periods: Number of periods to evaluate
#   - period: Time period in seconds


# TODO: Function to list alarms
# Create a function that lists all CloudWatch alarms or specific ones


# TODO: Function to delete an alarm
# Create a function to clean up by deleting a specified alarm


# TODO: Add error handling
# Implement try/except blocks to handle common CloudWatch errors


if __name__ == "__main__":
    print("AWS CloudWatch Monitoring Tool")
    print("=============================")
    
    # TODO: Implement your monitoring logic here
    # Example workflow:
    # 1. Get and display CPU metrics for the instance
    # 2. Create a CPU utilization alarm
    # 3. List all alarms to verify creation
    
    # Get and display metrics
    # print("\nRetrieving CPU metrics for instance:", instance_id)
    # metrics = get_cpu_metrics(instance_id)
    # if metrics:
    #     print("\nCPU Utilization (last hour):")
    #     for point in metrics:
    #         timestamp = point['Timestamp'].strftime('%Y-%m-%d %H:%M:%S')
    #         print(f"  {timestamp}: {point['Average']:.2f}%")
    # else:
    #     print("No metrics found for this instance")
    
    # Create an alarm
    # print("\nCreating CPU utilization alarm...")
    # create_cpu_alarm(instance_id, 'HighCPUAlert', 70.0)
    
    # List alarms
    # print("\nCurrent CloudWatch Alarms:")
    # list_alarms()
    
    # Print cleanup instructions
    print("\n⚠️  IMPORTANT: Remember to delete test alarms when you're done!")
    print("To delete an alarm via Python, use:")
    print("cloudwatch.delete_alarms(AlarmNames=['HighCPUAlert'])")

"""
Sample output:

AWS CloudWatch Monitoring Tool
=============================

Retrieving CPU metrics for instance: i-0abc123def456789

CPU Utilization (last hour):
  2023-06-07 14:15:00: 2.35%
  2023-06-07 14:20:00: 1.78%
  2023-06-07 14:25:00: 12.53%
  2023-06-07 14:30:00: 3.42%
  2023-06-07 14:35:00: 2.05%
  2023-06-07 14:40:00: 1.95%

Creating CPU utilization alarm...
Alarm 'HighCPUAlert' created successfully!

Current CloudWatch Alarms:
- HighCPUAlert (OK)
- Database-HighCPU (OK)

⚠️  IMPORTANT: Remember to delete test alarms when you're done!
To delete an alarm via Python, use:
cloudwatch.delete_alarms(AlarmNames=['HighCPUAlert'])
""" 
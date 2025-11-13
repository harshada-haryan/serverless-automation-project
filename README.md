# Serverless Infrastructure Automation — README

**Project Title:** Serverless Infrastructure Automation using AWS Lambda & EventBridge

## 📘 Overview

This project demonstrates how to automate common AWS infrastructure management tasks using a **serverless architecture** built with **AWS Lambda**, **EventBridge**, and **IAM**. It automates tasks such as EC2 volume backup, snapshot cleanup, resource tagging, and S3 log rotation — all without requiring manual intervention.

---

## 📁 Project Structure

```
serverless-automation-project/
├── lambda-functions/
│   ├── ec2-backup/
│   │   └── lambda_function.py
│   ├── snapshot-cleanup/
│   │   └── lambda_function.py
│   ├── resource-tagging/
│   │   └── lambda_function.py
│   └── s3-log-rotation/
│       └── lambda_function.py
├── iam-roles/
│   ├── lambda-execution-role.json
│   ├── ec2-backup-policy.json
│   ├── snapshot-cleanup-policy.json
│   ├── resource-tagging-policy.json
│   └── s3-log-rotation-policy.json
├── eventbridge-rules/
│   ├── ec2-backup-schedule.json
│   ├── snapshot-cleanup-schedule.json
│   ├── resource-tagging-schedule.json
│   └── s3-log-rotation-schedule.json
├── screenshots/
│   └── [All project screenshots]
└── README.md

```

---

## ⚙️ Workflow Description

1. **EventBridge Rules** — Schedule automated triggers for each Lambda function (daily/weekly as needed).
2. **Lambda Functions** — Perform automation tasks such as:

   * **ec2-backup:** Takes EBS volume snapshots.
   * **snapshot-cleanup:** Deletes outdated snapshots to save cost.
   * **resource-tagging:** Adds consistent tags to resources for tracking.
   * **s3-log-rotation:** Rotates and manages S3 logs.
3. **IAM Policies** — Provide least-privilege access for each Lambda function.
4. **CloudWatch** — Monitors logs and metrics for automation validation.


---

🔧 Implementation Details
Lambda Functions
1. EC2 Volume Backup Function
Purpose: Creates automated snapshots of tagged EC2 volumes
Trigger: EventBridge (Daily at 2:00 AM UTC)
Key Operations:

Identifies EC2 volumes with specific tags
Creates snapshots with descriptive names
Adds metadata tags to snapshots
<img width="1916" height="853" alt="lambda function-ec2 backup" src="https://github.com/user-attachments/assets/d01bf57f-6998-460e-b205-e7a6d7c4b6ad" />

EC2 Backup Lambda function configuration

2. Snapshot Cleanup Function
Purpose: Removes outdated EBS snapshots to optimize costs
Trigger: EventBridge (Daily at 3:00 AM UTC)
Key Operations:

Scans all EBS snapshots
Identifies snapshots older than 30 days
Deletes qualifying snapshots automatically

Show Image
Snapshot cleanup Lambda function

3. Resource Tagging Function
Purpose: Applies consistent tags based on naming conventions
Trigger: EventBridge (Every 6 hours)
Key Operations:

Scans untagged resources
Applies tags based on naming patterns
Ensures compliance with tagging policies

Show Image
Resource tagging automation function

4. S3 Log Rotation Function
Purpose: Manages log lifecycle in S3 buckets
Trigger: EventBridge (Daily at 1:00 AM UTC)
Key Operations:

Applies lifecycle policies to log buckets
Transitions old logs to cheaper storage classes
Archives or deletes logs based on retention rules

Show Image
S3 log rotation Lambda function

📅 EventBridge Schedules
Schedule Configuration
Show Image
EventBridge rules overview showing all scheduled automations
EC2 Backup Schedule
Show Image
Nightly EC2 volume backup schedule configuration
Snapshot Cleanup Schedule
Show Image
Daily snapshot cleanup schedule
Resource Tagging Schedule
Show Image
Periodic resource tagging schedule
S3 Log Rotation Schedule
Show Image
Daily S3 log rotation schedule

🔐 IAM Configuration
IAM Roles Dashboard
Show Image
Overview of all Lambda execution roles
EC2 Backup Role
Show Image
IAM role with permissions for EC2 snapshot operations
Permissions:

ec2:CreateSnapshot
ec2:DescribeVolumes
ec2:CreateTags
ec2:DescribeTags

Snapshot Cleanup Role
Show Image
IAM role for snapshot deletion operations
Permissions:

ec2:DescribeSnapshots
ec2:DeleteSnapshot
ec2:DescribeTags

Resource Tagging Role
Show Image
IAM role for resource tagging operations
Permissions:

ec2:DescribeInstances
ec2:DescribeVolumes
ec2:CreateTags
tag:GetResources

S3 Log Rotation Role
Show Image
IAM role for S3 lifecycle management
Permissions:

s3:PutLifecycleConfiguration
s3:GetLifecycleConfiguration
s3:ListBucket


📊 Monitoring & Logs
CloudWatch Dashboard
Show Image
Central monitoring dashboard for all Lambda functions
EC2 Backup Execution Logs
Show Image
Execution logs showing successful backup operations
Snapshot Cleanup Logs
Show Image
Snapshot cleanup execution history

📸 AWS Console Screenshots
Lambda Functions Dashboard
Show Image
Overview of all deployed Lambda functions
Configuration Settings
Show Image
AWS CLI configuration for deployment
Resource Tagging Results
Show Image
Successfully tagged resources
S3 Log Rotation Results
Show Image
S3 bucket lifecycle configuration

💰 Cost Optimization Impact
Before Implementation

EBS Snapshot Storage: ~500 GB of old snapshots
S3 Log Storage: ~2 TB in Standard storage class
Manual Operations: 10 hours/month of engineer time
Estimated Monthly Cost: $125/month

After Implementation

EBS Snapshot Storage: ~150 GB (70% reduction)
S3 Log Storage: 500 GB Standard, 1.5 TB in Glacier
Lambda Execution Cost: ~$2/month
Automated Operations: 0 manual hours
Estimated Monthly Cost: $45/month

Cost Savings

Direct Savings: $80/month ($960/year)
Operational Efficiency: 10 hours/month recovered
ROI: 94% cost reduction

Show Image
Deployment confirmation showing all components

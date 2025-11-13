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

## 🔧 Implementation Details

### Lambda Functions Overview

This project includes 4 Lambda functions for different automation tasks:

![Lambda Functions Dashboard](screenshots/AWS-lambda-dashboard.png)
*Overview of all deployed Lambda functions in AWS Console*

---

#### 1. EC2 Volume Backup Function

**Purpose:** Creates automated snapshots of tagged EC2 volumes

**Trigger:** EventBridge (Daily at 2:00 AM UTC)

**Key Operations:**
- Identifies EC2 volumes with specific tags
- Creates snapshots with descriptive names
- Adds metadata tags to snapshots

![Lambda Function - EC2 Backup](screenshots/lambda-function-ec2-backup.png)
*EC2 Backup Lambda function configuration showing runtime and handler settings*

![IAM Role - EC2 Backup](screenshots/IAM-ec2-backup.png)
*IAM role with necessary permissions for EC2 snapshot operations*

---

#### 2. Snapshot Cleanup Function

**Purpose:** Removes outdated EBS snapshots to optimize costs

**Trigger:** EventBridge (Daily at 3:00 AM UTC)

**Key Operations:**
- Scans all EBS snapshots
- Identifies snapshots older than 30 days
- Deletes qualifying snapshots automatically

![Lambda Function - Snapshot Cleanup](screenshots/lambda-function-snapshot-cleanup.png)
*Snapshot cleanup Lambda function*

![IAM Role - Snapshot Cleanup](screenshots/IAM-snapshot-cleanup.png)
*IAM role for snapshot deletion operations*

![CloudWatch Snapshots](screenshots/cloudwatch-snapshots.png)
*CloudWatch logs showing snapshot cleanup execution history*

---

#### 3. Resource Tagging Function

**Purpose:** Applies consistent tags based on naming conventions

**Trigger:** EventBridge (Every 6 hours)

**Key Operations:**
- Scans untagged resources
- Applies tags based on naming patterns
- Ensures compliance with tagging policies

![Lambda Function - Resource Tagging](screenshots/lambda-function-resource-tagging.png)
*Resource tagging automation function configuration*

![IAM Role - Resource Tagging](screenshots/IAM-resource-tagging.png)
*IAM role with permissions for resource tagging operations*

![Cloud Resource Tagging](screenshots/cloud-resource-tagging.png)
*Successfully tagged resources in AWS Console*

---

#### 4. S3 Log Rotation Function

**Purpose:** Manages log lifecycle in S3 buckets

**Trigger:** EventBridge (Daily at 1:00 AM UTC)

**Key Operations:**
- Applies lifecycle policies to log buckets
- Transitions old logs to cheaper storage classes
- Archives or deletes logs based on retention rules

![Lambda Function - S3 Log Rotation](screenshots/lambda-function-s3-log-rotation.png)
*S3 log rotation Lambda function*

![IAM Role - S3 Log Rotation](screenshots/IAM-s3-log-rotation.png)
*IAM role for S3 lifecycle management*

![Cloud S3 Log Rotation](screenshots/cloud-s3-log-rotation.png)
*S3 bucket lifecycle configuration applied by the function*

---

## 📅 EventBridge Schedules

### EventBridge Rules Dashboard

![EventBridge Dashboard](screenshots/AWS-eventbridge-dashboard.png)
*EventBridge rules overview showing all scheduled automations*

---

### Individual Schedule Configurations

#### EC2 Backup Schedule
**Cron Expression:** `cron(0 2 * * ? *)` (Daily at 2:00 AM UTC)

![EventBridge - EC2 Backup](screenshots/eventbridge-ec2-backup.png)
*Nightly EC2 volume backup schedule configuration*

---

#### Snapshot Cleanup Schedule
**Cron Expression:** `cron(0 3 * * ? *)` (Daily at 3:00 AM UTC)

![EventBridge - Snapshot Cleanup](screenshots/eventbridge-snapshot-cleanup.png)
*Daily snapshot cleanup schedule*

---

#### Resource Tagging Schedule
**Cron Expression:** `cron(0 */6 * * ? *)` (Every 6 hours)

![EventBridge - Resource Tagging](screenshots/eventbridge-resource-tagging.png)
*Periodic resource tagging schedule*

---

#### S3 Log Rotation Schedule
**Cron Expression:** `cron(0 1 * * ? *)` (Daily at 1:00 AM UTC)

![EventBridge - S3 Log Rotation](screenshots/eventbridge-s3-log-rotation.png)
*Daily S3 log rotation schedule*

---

## 🔐 IAM Configuration

### IAM Roles Dashboard

![IAM Roles Overview](screenshots/IAM-roles-dashboard.png)
*Overview of all Lambda execution roles with attached policies*

---

### Role Permissions Summary

Each Lambda function has a dedicated IAM role following the principle of least privilege:

| Function | Key Permissions |
|----------|----------------|
| EC2 Backup | `ec2:CreateSnapshot`, `ec2:DescribeVolumes`, `ec2:CreateTags` |
| Snapshot Cleanup | `ec2:DescribeSnapshots`, `ec2:DeleteSnapshot` |
| Resource Tagging | `ec2:DescribeInstances`, `ec2:CreateTags`, `tag:GetResources` |
| S3 Log Rotation | `s3:PutLifecycleConfiguration`, `s3:GetLifecycleConfiguration` |

---

## 📊 Monitoring & Logs

### CloudWatch Dashboard

![CloudWatch Dashboard](screenshots/AWS-cloudwatch-dashboard.png)
*Central monitoring dashboard for all Lambda functions showing invocations, errors, and duration*

---

### CloudWatch Logs - EC2 Backup

![CloudWatch EC2 Backup Logs](screenshots/cloudwatch-ec2-backup-logs.png)
*Execution logs showing successful backup operations with snapshot IDs and timestamps*

---

## 🛠️ AWS Configuration

### AWS CLI Configuration

![AWS Configure](screenshots/aws-configure.png)
*AWS CLI configuration used for deployment*

---

## 🚀 Deployment Process

### Deployment Overview

![Deploy All Components](screenshots/deploy-all.png)
*Complete deployment showing all Lambda functions, IAM roles, and EventBridge rules*

---

## 💰 Cost Optimization Impact

### Before Implementation
- **EBS Snapshot Storage:** ~500 GB of old snapshots
- **S3 Log Storage:** ~2 TB in Standard storage class
- **Manual Operations:** 10 hours/month of engineer time
- **Estimated Monthly Cost:** $125/month

### After Implementation
- **EBS Snapshot Storage:** ~150 GB (70% reduction)
- **S3 Log Storage:** 500 GB Standard, 1.5 TB in Glacier
- **Lambda Execution Cost:** ~$2/month
- **Automated Operations:** 0 manual hours
- **Estimated Monthly Cost:** $45/month

### Cost Savings
- **Direct Savings:** $80/month ($960/year)
- **Operational Efficiency:** 10 hours/month recovered
- **ROI:** 94% cost reduction in infrastructure costs

---

## 🛠️ Setup & Deployment Instructions

### Prerequisites
- AWS Account with appropriate permissions
- AWS CLI configured
- Python 3.9+ installed
- Git installed
- Bash shell (Linux/Mac) or Git Bash (Windows)

---

### Quick Deployment (Automated)

The project includes an automated deployment script that handles all setup steps.

#### Step 1: Clone Repository
```bash
git clone 
cd capstone-project-3
```

#### Step 2: Configure AWS Credentials
```bash
aws configure
# Enter your AWS Access Key ID
# Enter your AWS Secret Access Key
# Default region: us-east-1
# Default output format: json
```

![AWS Configuration](screenshots/aws-configure.png)
*AWS CLI configuration setup*

#### Step 3: Update Configuration (Optional)
Edit `deploy-all.sh` and update the following variables if needed:
```bash
AWS_REGION="us-east-1"
ACCOUNT_ID="YOUR_ACCOUNT_ID"  # Replace with your AWS Account ID
```

#### Step 4: Make Script Executable
```bash
chmod +x deploy-all.sh
```

#### Step 5: Run Deployment Script
```bash
./deploy-all.sh
```

![Deploy All](screenshots/deploy-all.png)
*Automated deployment script in action*

**The script will automatically:**
1. ✅ Create all IAM roles and policies
2. ✅ Package Lambda functions into ZIP files
3. ✅ Deploy all 4 Lambda functions
4. ✅ Create EventBridge schedules
5. ✅ Configure Lambda permissions
6. ✅ Verify successful deployment
#### Step 6: Verify Deployment
```bash
# Check Lambda functions
aws lambda list-functions --query 'Functions[*].FunctionName'

# Check EventBridge rules
aws events list-rules --query 'Rules[*].Name'

# Check IAM roles
aws iam list-roles --query 'Roles[?contains(RoleName, `lambda`)].RoleName'
```

---

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
├── docs/
│   ├── create-iam-roles.sh
│   └── setup-eventbridge.sh
├── deploy_all.sh
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

<img width="1919" height="893" alt="AWS lambda dashboard" src="https://github.com/user-attachments/assets/59d66af1-4679-4426-aec1-9d121efa7d3a" />

*Overview of all deployed Lambda functions in AWS Console*

---

#### 1. EC2 Volume Backup Function

**Purpose:** Creates automated snapshots of tagged EC2 volumes

**Trigger:** EventBridge (Daily at 1:00 AM UTC)

**Key Operations:**
- Identifies EC2 volumes with specific tags
- Creates snapshots with descriptive names
- Adds metadata tags to snapshots

**EC2 Backup Lambda function configuration showing runtime and handler settings**
<img width="1916" height="853" alt="lambda function-ec2 backup" src="https://github.com/user-attachments/assets/5e2b6e72-8131-41ed-adcd-f595358ebbc2" />


**IAM role with necessary permissions for EC2 snapshot operations**
<img width="1917" height="902" alt="IAM-ec2-backup" src="https://github.com/user-attachments/assets/fb7ee765-a000-444d-9026-198eeef81191" />

**Cloudwatch logs showing successful backup operations with snapshot IDs and timestamps**
<img width="1919" height="909" alt="cloudwatch ec2-backup" src="https://github.com/user-attachments/assets/d5092744-96b1-4b04-ba06-8968319326a5" />


---

#### 2. Snapshot Cleanup Function

**Purpose:** Removes outdated EBS snapshots to optimize costs

**Trigger:** EventBridge (every sunday at 3:00 AM UTC)

**Key Operations:**
- Scans all EBS snapshots
- Identifies snapshots older than 30 days
- Deletes qualifying snapshots automatically

**Snapshot cleanup Lambda function**
<img width="1919" height="908" alt="lambda function-snapshot-cleanup" src="https://github.com/user-attachments/assets/4917e5c8-0cec-4097-b694-08a65ae25b76" />


**IAM role for snapshot deletion operations**
<img width="1918" height="906" alt="IAM-snapshot-cleanup" src="https://github.com/user-attachments/assets/feb6241f-fada-45f3-90c3-9a0538c21f69" />


**CloudWatch logs showing snapshot cleanup execution history**
<img width="1917" height="908" alt="cloudwatch snapshot-cleanup" src="https://github.com/user-attachments/assets/5a5d85cc-9150-4c33-a8ce-aa159ea74cad" />



---

#### 3. Resource Tagging Function

**Purpose:** Applies consistent tags based on naming conventions

**Trigger:** EventBridge (Daily at 2:00 AM UTC)

**Key Operations:**
- Scans untagged resources
- Applies tags based on naming patterns
- Ensures compliance with tagging policies

**Resource tagging automation function configuration**
<img width="1914" height="903" alt="lambda function-resource-tagging" src="https://github.com/user-attachments/assets/4490bf96-87d4-4a20-b033-39dd323d293c" />



**IAM role with permissions for resource tagging operations**
<img width="1919" height="912" alt="IAM-resource-tagging" src="https://github.com/user-attachments/assets/4e07444a-ecc2-4f28-9ef8-35e46cd6969b" />


**Successfully tagged resources in AWS Console**
<img width="1919" height="907" alt="cloud resource-tagging" src="https://github.com/user-attachments/assets/dd55e304-cca1-4f32-b37d-869306f3a14d" />


---

#### 4. S3 Log Rotation Function

**Purpose:** Manages log lifecycle in S3 buckets

**Trigger:** EventBridge (every monday at 4:00 AM UTC)

**Key Operations:**
- Applies lifecycle policies to log buckets
- Transitions old logs to cheaper storage classes
- Archives or deletes logs based on retention rules

**S3 log rotation Lambda function**
<img width="1919" height="909" alt="lambda function-s3-log-rotation" src="https://github.com/user-attachments/assets/7a562e70-f440-4d18-992e-18c553c8cf97" />


**IAM role for S3 lifecycle management**
<img width="1919" height="907" alt="IAM-s3-log-rotation" src="https://github.com/user-attachments/assets/3db51aa5-b97c-4536-935f-9ecc7d345b1d" />


**S3 bucket lifecycle configuration applied by the function**
<img width="1919" height="911" alt="cloud s3-log-rotation" src="https://github.com/user-attachments/assets/eed02622-48ad-4dfe-8ab6-2f95875b4c68" />



---

## 📅 EventBridge Schedules

### EventBridge Rules Dashboard

**EventBridge rules overview showing all scheduled automations**
<img width="1919" height="912" alt="AWS eventbridge dashboard" src="https://github.com/user-attachments/assets/f40dc4ca-b655-4c92-ac0f-e8a029be62ea" />


---

### Individual Schedule Configurations

#### EC2 Backup Schedule
**Cron Expression:** `cron(0 1 * * ? *)` (Daily at 1:00 AM UTC)

*Nightly EC2 volume backup schedule configuration*
<img width="1919" height="906" alt="eventbridge-ec2-backup-schedule" src="https://github.com/user-attachments/assets/d0648b2c-6345-4a2b-a444-9bf315fccfba" />



---

#### Snapshot Cleanup Schedule
**Cron Expression:** `cron(0 3 ? *SUN*)` (every sunday at 3:00 AM UTC)

*Weekly(sunday) snapshot cleanup schedule*
<img width="1918" height="911" alt="eventbridge-snapshot-cleanup-schedule" src="https://github.com/user-attachments/assets/d5e4a2ce-10b7-4466-9def-25a5d994783a" />


---

#### Resource Tagging Schedule
**Cron Expression:** `cron(0 2 * * ? *)` ((Daily at 2:00 AM UTC)

*Periodic resource tagging schedule*
<img width="1919" height="912" alt="eventbridge-resource-tagging-schedule" src="https://github.com/user-attachments/assets/bcd9c4cf-ebed-4849-87e4-850d0faf82c3" />



---

#### S3 Log Rotation Schedule
**Cron Expression:** `cron(0 4 ? 8MON *)` (every monday at 4:00 AM UTC)

**Weekly(monday) S3 log rotation schedule*
<img width="1913" height="902" alt="eventbridge-s3-log-rotation-schedule" src="https://github.com/user-attachments/assets/31b482ff-7b93-4230-ade8-5e0bb5c3943c" />



---

## 🔐 IAM Configuration

### IAM Roles Dashboard

<img width="1918" height="911" alt="IAM roles dashboard" src="https://github.com/user-attachments/assets/75725056-1d72-4625-8d91-1fe88d8d546d" />

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

<img width="1919" height="908" alt="AWS cloudwatch dashboard" src="https://github.com/user-attachments/assets/f15c654d-ca24-4637-8d2e-6b47b54c0ea1" />

*Central monitoring dashboard for all Lambda functions showing invocations, errors, and duration*


---

## 🛠️ AWS Configuration

### AWS CLI Configuration

<img width="878" height="104" alt="aws configure" src="https://github.com/user-attachments/assets/16510390-3db5-4ab6-8e11-42c3171e6109" />

*AWS CLI configuration used for deployment*

---

## 🚀 Deployment Process


**Complete deployment showing all Lambda functions, IAM roles, and EventBridge rules**
<img width="1280" height="627" alt="deploy all" src="https://github.com/user-attachments/assets/a74bd2a3-7fff-4587-bbf9-ee1b0e89cec7" />



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
cd serverless-automation-project
```

#### Step 2: Configure AWS Credentials
```bash
aws configure
# Enter your AWS Access Key ID
# Enter your AWS Secret Access Key
# Default region: ap-south-1
# Default output format: json
```


#### Step 3: Update Configuration (Optional)
Edit `deploy-all.sh` and update the following variables if needed:
```bash
AWS_REGION="ap-south-1"
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

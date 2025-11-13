# Serverless Infrastructure Automation — README

**Project Title:** Serverless Infrastructure Automation using AWS Lambda & EventBridge

## 📘 Overview

This project demonstrates how to automate common AWS infrastructure management tasks using a **serverless architecture** built with **AWS Lambda**, **EventBridge**, and **IAM**. It automates tasks such as EC2 volume backup, snapshot cleanup, resource tagging, and S3 log rotation — all without requiring manual intervention.

---

## 📁 Project Structure

```
serverless-automation-project/
├── deploy_all.sh                     # Main script to deploy all components
├── deployment/                       # Deployment helper scripts
│   ├── create-iam-roles.sh           # Script to create IAM roles and attach policies
│   └── setup-eventbridge.sh          # Script to configure EventBridge rules
├── docs/
│   └── cost-analysis.md              # Simple cost analysis report (fresher level)
├── eventbridge-rules/                # JSON rules for scheduling Lambda functions
│   ├── ec2-backup-schedule.json
│   ├── resource-tagging-schedule.json
│   ├── s3-log-rotation-schedule.json
│   └── snapshot-cleanup-schedule.json
├── iam-policies/                     # IAM policies for Lambda functions
│   ├── ec2-backup-policy.json
│   ├── resource-tagging-policy.json
│   ├── s3-log-rotation-policy.json
│   └── snapshot-cleanup-policy.json
├── lambda-functions/                 # Lambda source code for each automation task
│   ├── ec2-backup/
│   │   └── lambda-functions.py
│   │  
│   ├── resource-tagging/
│   │   └── lambda-functions.py
│   ├── s3-log-rotation/
│   │   └── lambda-functions.py
│   │  
│   └── snapshot-cleanup/
│       └── lambda-functions.py

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

## 👩‍💻 Author

**Harshada Haryan**
*Fresher Cloud Support Engineer Project — AWS Lambda & EventBridge Automation*

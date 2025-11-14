# 💰 AWS Cost Analysis — Serverless Automation Project

## 📘 Overview

This document explains the approximate **monthly cost** of running the **Serverless Infrastructure Automation Project** using **AWS Lambda** and **EventBridge**.  


---

## ⚙️ AWS Services Used

| AWS Service | Purpose | Pricing Model |
|--------------|----------|----------------|
| **AWS Lambda** | Runs automation scripts like EC2 Backup, Tagging, Cleanup, and Log Rotation | Pay per request and execution time |
| **Amazon EventBridge** | Triggers Lambda functions automatically on a schedule | Pay per event |
| **Amazon S3** | Stores log files or reports | Pay per GB stored |
| **Amazon EC2 Snapshots (EBS)** | Stores volume backups | Pay per GB-month of snapshot storage |
| **Amazon CloudWatch** | Monitors and stores logs for Lambda | Pay per metric and log storage |

---

## 🕓 Lambda Schedule Summary

| Lambda Function | Trigger Frequency | Description |
|------------------|------------------|--------------|
| **EC2 Backup** | **Daily** | Creates new snapshots of EC2 volumes for daily backup. |
| **Snapshot Cleanup** | **Weekly** | Deletes old EBS snapshots to save cost. |
| **Resource Tagging** | **Daily** | Automatically applies or updates resource tags. |
| **S3 Log Rotation** | **Weekly** | Removes or compresses old log files in S3. |

---

## 🧮 Estimated Monthly Cost (Example)

| Component | Example Usage | Cost Estimate |
|------------|----------------|----------------|
| **Lambda Functions** | 4 functions × ~120 total runs/month | **$0.10** |
| **EventBridge Rules** | 4 rules × 30–40 events/month | **$0.01** |
| **S3 Storage** | 1 GB of log data | **$0.03** |
| **Snapshots** | 50 GB snapshot data × $0.05/GB | **$2.50** |
| **CloudWatch Logs** | 50 MB logs | **$0.02** |
| ✅ **Total Approx. Cost** | | **~$2.66 / month** |

🟢 **In AWS Free Tier**, this cost may be almost **$0**, since Lambda and EventBridge include free limits.

---

## 💡 Cost Optimization Impact

| Optimization Step | Impact |
|-------------------|--------|
| **Weekly Cleanup of Snapshots** | Reduces EBS storage cost by 25–30%. |
| **Weekly Log Rotation in S3** | Keeps S3 cost under control. |
| **Using Lifecycle Policies** | Automates deletion of old resources. |
| **Using Right Lambda Memory Size** | Reduces execution cost. |
| **Using AWS Free Tier** | Makes the setup almost free for testing. |

---

## 🧾 Summary 

> This project runs 4 Lambda functions automatically.  
> Two (EC2 Backup and Resource Tagging) run daily, and two (Snapshot Cleanup and S3 Log Rotation) run weekly.  
> The total estimated cost is around **$2.66 per month**, and under AWS Free Tier, it’s **almost free**.  
> So it’s a **low-cost, serverless, and efficient automation solution** that also helps reduce manual work.”

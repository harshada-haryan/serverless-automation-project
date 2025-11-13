# 💰 AWS Cost Analysis — Serverless Automation Project

## 📘 Overview

This project uses **AWS Lambda** and **Amazon EventBridge** to automate daily cloud operations like:
- Taking EC2 backups  
- Cleaning old snapshots  
- Tagging AWS resources  
- Rotating S3 logs  

It is fully **serverless**, so no EC2 instance runs continuously — we only pay when the automation runs.

---

## ⚙️ AWS Services Used

| AWS Service | Purpose | How Cost Works |
|--------------|----------|----------------|
| **AWS Lambda** | Runs automation scripts for EC2 backup, tagging, and cleanup. | Pay per request and execution time. |
| **Amazon EventBridge** | Triggers Lambda functions on a schedule. | Pay per rule and per event published. |
| **Amazon S3** | Stores log files or backup data. | Pay per GB stored per month. |
| **Amazon EBS Snapshots** | Stores EC2 volume backups. | Pay per GB of snapshot data. |
| **Amazon CloudWatch** | Monitors functions and stores logs. | Pay for log size and metrics. |

---

## 🧮 Estimated Monthly Cost (Example)

| Component | Example Usage | Cost Estimate |
|------------|----------------|----------------|
| **Lambda Functions** | 4 functions × 30 runs = 120 total runs | **$0.10** |
| **EventBridge Rules** | 4 rules × 30 events = 120 events | **$0.01** |
| **S3 Storage** | 1 GB of log data | **$0.03** |
| **Snapshots** | 50 GB snapshot data × $0.05/GB | **$2.50** |
| **CloudWatch Logs** | 50 MB logs | **$0.02** |
| **✅ Total Approx. Cost** |  | **~$2.66 / month** |

🟢 In AWS Free Tier, this cost may be **almost $0**, since **Lambda and EventBridge** both include free usage limits.

---

### 💬 How to Explain (For Sir or Interview)

> “Sir, this project runs 4 Lambda functions every day, and all are triggered automatically by EventBridge.  
> The total estimated cost is around **$2.66 per month**, and under the AWS Free Tier, it’s **almost free**.  
> So it’s a **low-cost, serverless, and efficient automation solution**.”

---

## 💡 Cost Optimization Techniques Used

| Optimization Method | Description | Why It Saves Cost |
|----------------------|--------------|-------------------|
| **Automated Snapshot Cleanup** | Old EBS snapshots are deleted automatically after a set number of days. | Reduces unnecessary storage cost. |
| **Right-Sizing Lambda Memory** | Each function uses only the required memory. | Avoids paying for unused capacity. |
| **CloudWatch Log Retention** | Log retention is limited to 7–14 days. | Reduces log storage cost. |
| **S3 Log Compression** | Logs are stored in `.zip` or `.gz` format. | Uses less S3 storage. |
| **Serverless Setup** | No EC2 instance needed. | Saves continuous compute cost. |

---

## 📊 💥 Cost Optimization Impact

| Area | Before Automation (Manual) | After Automation (Serverless) | Impact |
|-------|------------------------------|-------------------------------|---------|
| **EC2 Backup Management** | Manual snapshots; unused backups increase cost. | Automated backups and cleanup. | **~30% storage cost saved** |
| **Monitoring and Logging** | Logs stored forever. | Logs auto-rotated and compressed. | **~50% log cost saved** |
| **Operations Time** | Manual effort daily. | Fully automated using Lambda. | **~80% time saved** |
| **Compute Resources** | Required EC2 instance for scripts. | Uses Lambda (no servers). | **~$5–$10 saved per month** |
| **Overall Monthly Cost** | ~$10–$15 (manual). | ~$2–$3 (serverless). | **~70–80% total cost reduction** |

---

## ✅ Conclusion

This serverless automation setup is **cost-effective, efficient, and scalable**.  
It helps reduce manual work, storage cost, and maintenance effort — ideal for cloud operations automation.

### 🔹 Key Takeaways:
- Pay only when automation runs → no idle cost.  
- Automatically deletes old data → lower storage bills.  
- No servers → zero maintenance effort.  
- Practical example of **cost optimization in AWS**.

> 💬 **In short:**  
> This project shows how AWS Lambda + EventBridge can automate daily tasks, saving **money (up to 80%)** and **manual time (up to 80%)**.

---

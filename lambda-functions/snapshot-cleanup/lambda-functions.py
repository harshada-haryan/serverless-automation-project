import os
import boto3
from datetime import datetime, timezone, timedelta

REGION = os.getenv("AWS_REGION", "ap-south-1")
RETENTION_DAYS = int(os.getenv("RETENTION_DAYS", "30"))

ec2 = boto3.client("ec2", region_name=REGION)

def lambda_handler(event, context):
    cutoff = datetime.now(timezone.utc) - timedelta(days=RETENTION_DAYS)
    filters = [{"Name": "tag:AutoBackup", "Values": ["true"]}]
    snaps = ec2.describe_snapshots(OwnerIds=['self'], Filters=filters).get("Snapshots", [])
    deleted = []
    for s in snaps:
        if s["StartTime"] < cutoff:
            try:
                ec2.delete_snapshot(SnapshotId=s["SnapshotId"])
                deleted.append(s["SnapshotId"])
            except Exception as e:
                print(f"Failed delete {s['SnapshotId']}: {e}")
    return {"deleted": deleted, "count": len(deleted)}

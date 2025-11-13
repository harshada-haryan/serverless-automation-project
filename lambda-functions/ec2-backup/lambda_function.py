import os
import boto3
from datetime import datetime

REGION = os.getenv("AWS_REGION", "ap-south-1")
RETENTION_DAYS = int(os.getenv("RETENTION_DAYS", "30"))
VOLUME_TAG_KEY = os.getenv("VOLUME_TAG_KEY", "Backup")
VOLUME_TAG_VALUE = os.getenv("VOLUME_TAG_VALUE", "true")

ec2 = boto3.client("ec2", region_name=REGION)

def lambda_handler(event, context):
    filters = [
        {"Name": f"tag:{VOLUME_TAG_KEY}", "Values": [VOLUME_TAG_VALUE]},
        {"Name": "status", "Values": ["in-use", "available"]}
    ]
    volumes = ec2.describe_volumes(Filters=filters).get("Volumes", [])
    created = []
    for v in volumes:
        vol_id = v["VolumeId"]
        desc = f"Auto-backup of {vol_id} created by Lambda on {datetime.utcnow().isoformat()}Z"
        try:
            resp = ec2.create_snapshot(VolumeId=vol_id, Description=desc)
            snap_id = resp["SnapshotId"]
            ec2.create_tags(Resources=[snap_id], Tags=[
                {"Key": "AutoBackup", "Value": "true"},
                {"Key": "VolumeId", "Value": vol_id},
                {"Key": "RetentionDays", "Value": str(RETENTION_DAYS)}
            ])
            created.append(snap_id)
        except Exception as e:
            print(f"Error creating snapshot for {vol_id}: {e}")
    return {"created_snapshots": created, "count": len(created)}

import os
import boto3

REGION = os.getenv("AWS_REGION", "ap-south-1")
BUCKET_PREFIX = os.getenv("BUCKET_PREFIX", "")
DAYS_TO_GLACIER = int(os.getenv("DAYS_TO_GLACIER", "30"))
DAYS_TO_EXPIRE = int(os.getenv("DAYS_TO_EXPIRE", "365"))

s3 = boto3.client("s3", region_name=REGION)

def lambda_handler(event, context):
    resp = s3.list_buckets()
    processed = []
    for b in resp.get("Buckets", []):
        name = b["Name"]
        if BUCKET_PREFIX and not name.startswith(BUCKET_PREFIX):
            continue
        rule = {
            "Rules": [
                {
                    "ID": "RotateLogs",
                    "Filter": {"Prefix": ""},
                    "Status": "Enabled",
                    "Transitions": [
                        {"Days": DAYS_TO_GLACIER, "StorageClass": "STANDARD_IA"}
                    ],
                    "Expiration": {"Days": DAYS_TO_EXPIRE}
                }
            ]
        }
        try:
            s3.put_bucket_lifecycle_configuration(Bucket=name, LifecycleConfiguration=rule)
            processed.append({"bucket": name, "status": "configured"})
        except Exception as e:
            processed.append({"bucket": name, "error": str(e)})
    return {"processed": processed}

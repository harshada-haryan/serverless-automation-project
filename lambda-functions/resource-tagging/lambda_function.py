import boto3
import re
import os

REGION = os.getenv("AWS_REGION", "ap-south-1")
ec2 = boto3.resource("ec2", region_name=REGION)
s3 = boto3.client("s3", region_name=REGION)

def tag_ec2_instances():
    results = []
    for inst in ec2.instances.filter(Filters=[{"Name": "instance-state-name", "Values": ["running", "stopped"]}]):
        name = next((t["Value"] for t in (inst.tags or []) if t["Key"] == "Name"), None)
        tags_to_apply = []
        if name and re.search(r"web[-_]", name, re.I):
            tags_to_apply.append({"Key": "Environment", "Value": "web"})
        if tags_to_apply:
            inst.create_tags(Tags=tags_to_apply)
            results.append({"instance": inst.id, "tags": tags_to_apply})
    return results

def tag_volumes_from_instance():
    results = []
    for vol in ec2.volumes.filter(Filters=[{"Name": "status", "Values": ["in-use"]}]):
        if vol.attachments:
            instance_id = vol.attachments[0]["InstanceId"]
            inst = ec2.Instance(instance_id)
            name_tag = next((t for t in inst.tags or [] if t["Key"] == "Name"), None)
            if name_tag:
                vol.create_tags(Tags=[{"Key": "Name", "Value": name_tag["Value"]}])
                results.append({"volume": vol.id, "propagated": "Name"})
    return results

def tag_s3_buckets():
    results = []
    for b in s3.list_buckets().get("Buckets", []):
        name = b["Name"]
        if "logs" in name.lower():
            try:
                s3.put_bucket_tagging(
                    Bucket=name,
                    Tagging={"TagSet": [{"Key": "LogsBucket", "Value": "true"}]}
                )
                results.append({"bucket": name, "tagged": True})
            except Exception as e:
                results.append({"bucket": name, "error": str(e)})
    return results

def lambda_handler(event, context):
    ec2_tags = tag_ec2_instances()
    vol_tags = tag_volumes_from_instance()
    s3_tags = tag_s3_buckets()
    return {"ec2": ec2_tags, "volumes": vol_tags, "s3": s3_tags}

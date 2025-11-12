#!/bin/bash
# Creates IAM roles and attaches policies for all Lambda functions

set -e

LAMBDA_FUNCTIONS=("ec2-backup" "snapshot-cleanup" "resource-tagging" "s3-log-rotation")
POLICY_PATH="../iam-policies"

echo "Creating IAM roles for Lambda functions..."

for FUNC in "${LAMBDA_FUNCTIONS[@]}"; do
  ROLE_NAME="${FUNC}-role"
  POLICY_FILE="${POLICY_PATH}/${FUNC}-policy.json"

  echo "Creating role: $ROLE_NAME"
  aws iam create-role \
    --role-name "$ROLE_NAME" \
    --assume-role-policy-document '{
      "Version": "2012-10-17",
      "Statement": [{
        "Effect": "Allow",
        "Principal": {"Service": "lambda.amazonaws.com"},
        "Action": "sts:AssumeRole"
      }]
    }' >/dev/null

  echo "Attaching policy to $ROLE_NAME..."
  aws iam put-role-policy \
    --role-name "$ROLE_NAME" \
    --policy-name "${FUNC}-policy" \
    --policy-document file://${POLICY_FILE}

  echo "IAM role created for ${FUNC}"
done

echo "All IAM roles created successfully."

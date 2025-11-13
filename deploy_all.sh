#!/bin/bash
# ==========================================================
# 🚀 Deploy All Script - Serverless Automation Project
# Automates IAM roles, Lambda uploads, and EventBridge setup
# ==========================================================

set -e

ACCOUNT_ID=$(aws sts get-caller-identity --query "Account" --output text)
REGION="ap-south-1"

echo "==========================================="
echo "🚀 Starting Full Deployment for AWS Serverless Automation"
echo "AWS Account: $ACCOUNT_ID"
echo "Region: $REGION"
echo "==========================================="

# 1️⃣ Create IAM Roles
echo "-------------------------------------------"
echo "🔹 Step 1: Creating IAM Roles for Lambdas..."
echo "-------------------------------------------"
cd deployment
bash create-iam-roles.sh
cd ..

# 2️⃣ Package and Deploy Lambda Functions
echo "-------------------------------------------"
echo "🔹 Step 2: Deploying Lambda Functions..."
echo "-------------------------------------------"

LAMBDA_FUNCTIONS=("ec2-backup" "snapshot-cleanup" "resource-tagging" "s3-log-rotation")

for FUNC in "${LAMBDA_FUNCTIONS[@]}"; do
  echo "📦 Packaging Lambda: ${FUNC}"
  cd lambda-functions/${FUNC}
  zip -r ${FUNC}.zip . >/dev/null
  cd ../..

  ROLE_ARN="arn:aws:iam::${ACCOUNT_ID}:role/${FUNC}-role"

  echo "-------------------------------------------"
  echo "🧹 Deleting old Lambda (if exists): ${FUNC}"
  echo "-------------------------------------------"
  aws lambda delete-function --function-name ${FUNC} --region ${REGION} 2>/dev/null || true

  echo "🚀 Creating new Lambda: ${FUNC}"
  aws lambda create-function \
    --function-name ${FUNC} \
    --runtime python3.9 \
    --role ${ROLE_ARN} \
    --handler lambda_function.lambda_handler \
    --zip-file fileb://lambda-functions/${FUNC}/${FUNC}.zip \
    --region ${REGION} \
    --timeout 900 \
    --memory-size 256

  echo "✅ Lambda function '${FUNC}' deployed successfully."
done

# 3️⃣ Set up EventBridge Rules
echo "-------------------------------------------"
echo "🔹 Step 3: Setting up EventBridge Schedules..."
echo "-------------------------------------------"
cd deployment
bash setup-eventbridge.sh
cd ..

# ✅ DONE
echo "==========================================="
echo "🎉 Deployment Completed Successfully!"
echo "✅ IAM Roles Created"
echo "✅ Lambda Functions Deployed"
echo "✅ EventBridge Rules Configured"
echo "==========================================="

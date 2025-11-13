#!/bin/bash
# Sets up EventBridge rules for scheduling Lambda functions

set -e

ACCOUNT_ID="285168796340"
REGION="ap-south-1"
EVENT_PATH="../eventbridge-rules"

declare -A FUNCTIONS
FUNCTIONS=(
  ["ec2-backup"]="EC2BackupSchedule"
  ["snapshot-cleanup"]="SnapshotCleanupSchedule"
  ["resource-tagging"]="ResourceTaggingSchedule"
  ["s3-log-rotation"]="S3LogRotationSchedule"
)

for FUNC in "${!FUNCTIONS[@]}"; do
  RULE_FILE="${EVENT_PATH}/${FUNC}-schedule.json"
  RULE_NAME="${FUNCTIONS[$FUNC]}"
  LAMBDA_ARN="arn:aws:lambda:${REGION}:${ACCOUNT_ID}:functions:${FUNC}"

  echo "Creating EventBridge rule: ${RULE_NAME}"
  SCHEDULE=$(jq -r '.ScheduleExpression' "${RULE_FILE}")
  aws events put-rule \
    --name "${RULE_NAME}" \
    --schedule-expression "${SCHEDULE}" \
    --state ENABLED

  echo "Adding target: ${FUNC}"
  aws events put-targets \
    --rule "${RULE_NAME}" \
    --targets "Id=${FUNC}Target,Arn=${LAMBDA_ARN}"

  echo "Adding permission for EventBridge to invoke Lambda..."
  aws lambda add-permission \
    --function-name "${FUNC}" \
    --statement-id "EventBridgeInvoke${FUNC}" \
    --action "lambda:InvokeFunction" \
    --principal "events.amazonaws.com" \
    --source-arn "arn:aws:events:${REGION}:${ACCOUNT_ID}:rule/${RULE_NAME}" || true

done

echo "EventBridge scheduling setup complete."

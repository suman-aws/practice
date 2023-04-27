#!/bin/bash

output=$(python prepare_new_deployment.py)

environment=$(echo "$output" | awk -F ': ' '/ENVironment:/ {print $2}')
deployment_context=$(echo "$output" | awk -F ': ' '/DEPLOYMENT_CONTEXT:/ {print $2}')
model_names=$(echo "$output" | awk -F ': ' '/MODEL_NAMES:/ {print $2}')
model_versions=$(echo "$output" | awk -F ': ' '/MODEL_VERSIONS:/ {print $2}')
system_uids=$(echo "$output" | awk -F ': ' '/SYSTEM_UIDS:/ {print $2}')
testing_times=$(echo "$output" | awk -F ': ' '/TESTING_TIMES:/ {print $2}')

echo "environment: $environment"
echo "deployment_context: $deployment_context"
echo "model_names: $model_names"
echo "model_versions: $model_versions"
echo "system_uids: $system_uids"
echo "testing_times: $testing_times"

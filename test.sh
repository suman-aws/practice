#!/bin/bash
# env=("QA" "QA")

# if [ "$env[0]" = "QA" ]; then
#   host="abc5.com"
# elif [ "$env[0" = "PROD" ]; then
#   host="abc3.com"
# else
#   host="abc7.com"
# fi

# echo "$host"
i

# DEPLOYMENT_CONTEXT=$1
# MODEL_NAMES=$2
# MODEL_VERSIONS=$3
# SYSTEM_UIDS=$4
# TESTING_TIMES=$5

echo "Deployment Context: $DEPLOYMENT_CONTEXT"
echo "Model Names: $MODEL_NAMES"
echo "Model Versions: $MODEL_VERSIONS"
echo "System UIDs: $SYSTEM_UIDS"
echo "Testing Times: $TESTING_TIMES"

siuid=$(python -V)
echo $siuid

# # rest of deployment script

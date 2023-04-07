import os
import subprocess

# Run the prepare_re_deployment.py script and capture the output
result = subprocess.run(['python3', 'new.py'], capture_output=True, text=True)

# Split the output into lines and loop through each line
for line in result.stdout.strip().split('\n'):
    # Extract the deployment information from each line
    env, context, model, version, sysuid, testingtime = [x.strip() for x in line.split('=')]
    
    # Set the environment variables for the GitHub workflow
    os.environ['DEPLOY_ENV'] = envi
#     os.environ['DEPLOY_CONTEXT'] = context
    os.environ['DEPLOY_MODEL'] = model
    os.environ['DEPLOY_VERSION'] = version
#     os.environ['DEPLOY_SYSUID'] = sysuid
#     os.environ['DEPLOY_TESTINGTIME'] = testingtime

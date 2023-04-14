import subprocess
import os

# Run the script and capture the output
result = subprocess.run(["python", "prepare_re_deployment.py"], capture_output=True, text=True)

# Split the output into lines
lines = result.stdout.strip().split('\n')

# Initialize empty lists for each environment variable
env = []
context = []
model = []
version = []
sysuid = []
testingtime = []

# Process each line and populate the lists
for line in lines:
    parts = line.split('=')
    env.append(parts[0].strip())
    context.append(parts[1].strip())
    model.append(parts[2].strip())
    version.append(parts[3].strip())
    sysuid.append(parts[4].strip())
    testingtime.append(parts[5].strip())

# Set the environment variables in GitHub Actions
os.environ['ENVironment'] = str(env)
os.environ['DEPLOYMENT_CONTEXT'] = str(context)
os.environ['MODEL_NAMES'] = str(model)
os.environ['MODEL_VERSIONS'] = str(version)
os.environ['SYSTEM_UIDS'] = str(sysuid)
os.environ['TESTING_TIMES'] = str(testingtime)

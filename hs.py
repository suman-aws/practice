import subprocess
import os

# Run the script and capture the output
script_path = r"C:\Users\hp\Desktop\New folder\practice\prepare_re_deployment.py"
result = subprocess.run(['python', script_path], capture_output=True)

# Parse the output into variables
output = result.stdout.decode('utf-8').split('\n')
env = output[0].split(': ')[1].split(', ')
deployment_context = output[1].split(': ')[1].split(', ')
model_names = output[2].split(': ')[1].split(', ')
model_versions = output[3].split(': ')[1].split(', ')
system_uids = output[4].split(': ')[1].split(', ')
testing_time = output[5].split(': ')[1].split(', ')

# Set the environment variables for the GitHub workflow
os.environ['ENVIRONMENT'] = ', '.join(env)
os.environ['DEPLOYMENT_CONTEXT'] = ', '.join(deployment_context)
os.environ['MODEL_NAMES'] = ', '.join(model_names)
os.environ['MODEL_VERSIONS'] = ', '.join(model_versions)
os.environ['SYSTEM_UIDS'] = ', '.join(system_uids)
os.environ['TESTING_TIME'] = ', '.join(testing_time)

# Print the environment variables for verification
print(os.environ['ENVIRONMENT'])
print(os.environ['DEPLOYMENT_CONTEXT'])
print(os.environ['MODEL_NAMES'])
print(os.environ['MODEL_VERSIONS'])
print(os.environ['SYSTEM_UIDS'])
print(os.environ['TESTING_TIME'])

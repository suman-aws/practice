import subprocess
import os

# Run the script and capture the output
result = subprocess.run(["python", "prepare_re_deployment.py"], capture_output=True, text=True)
import os

# input string
input_str = '''QA=RW=T-PR=1.0=77276535=20230218-235959
QA=RW+RS=LR=1.0=77276535=20230218-235959'''

# initialize empty lists
env_list = []
deployment_context_list = []
model_names_list = []
model_versions_list = []
system_uids_list = []
testing_times_list = []

# split the input string by newline character and iterate over each line
for line in result.split('\n'):
    # split the line by '=' character and append the values to the corresponding lists
    parts = line.split('=')
    env_list.append(parts[0])
    deployment_context_list.append(parts[1])
    model_names_list.append(parts[2])
    model_versions_list.append(parts[3])
    system_uids_list.append(parts[4])
    testing_times_list.append(parts[5])

# set the values as environment variables in the GitHub Actions workflow
os.environ['ENVironment'] = str(env_list)
os.environ['DEPLOYMENT_CONTEXT'] = str(deployment_context_list)
os.environ['MODEL_NAMES'] = str(model_names_list)
os.environ['MODEL_VERSIONS'] = str(model_versions_list)
os.environ['SYSTEM_UIDS'] = str(system_uids_list)
os.environ['TESTING_TIMES'] = str(testing_times_list)

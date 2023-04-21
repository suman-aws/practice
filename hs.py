import subprocess
import re
import os

output = subprocess.check_output(["python", "prepare_new_deployment.py"]).decode("utf-8")

environment = re.findall(r"(?<=ENVironment: )\['.*?'\]", output)[0].strip("[]''")
os.environ["ENVironment"] = environment

model_names = re.findall(r"(?<=MODEL_NAMES: )\['.*?'\]", output)[0].strip("[]''")
os.environ["MODEL_NAMES"] = model_names

model_versions = re.findall(r"(?<=MODEL_VERSIONS: )\['.*?'\]", output)[0].strip("[]''")
os.environ["MODEL_VERSIONS"] = model_versions

deployment_contexts = re.findall(r"(?<=DEPLOYMENT_CONTEXT: )\['.*?'\]", output)[0].strip("[]''")
os.environ["DEPLOYMENT_CONTEXT"] = deployment_contexts

system_uids = re.findall(r"(?<=SYSTEM_UIDS: )\['.*?'\]", output)[0].strip("[]''")
os.environ["SYSTEM_UIDS"] = system_uids

testing_times = re.findall(r"(?<=TESTING_TIMES: )\['.*?'\]", output)[0].strip("[]''")
os.environ["TESTING_TIMES"] = testing_times

import re

output = """
ENVironment: ['QA', 'QA']
DEPLOYMENT_CONTEXT: ['RW', 'RW+RS']
MODEL_NAMES: ['T-PR', 'LR']
MODEL_VERSIONS: ['1.0', '1.0']
SYSTEM_UIDS: ['77276535', '77276535']
TESTING_TIMES: ['20230218-235959', '20230218-235959']
"""

environment = re.findall(r"ENVironment: (\[.*?\])", output)[0]
deployment_context = re.findall(r"DEPLOYMENT_CONTEXT: (\[.*?\])", output)[0]
model_names = re.findall(r"MODEL_NAMES: (\[.*?\])", output)[0]
model_versions = re.findall(r"MODEL_VERSIONS: (\[.*?\])", output)[0]
system_uids = re.findall(r"SYSTEM_UIDS: (\[.*?\])", output)[0]
testing_times = re.findall(r"TESTING_TIMES: (\[.*?\])", output)[0]

print("environment:", environment)
print("deployment_context:", deployment_context)
print("model_names:", model_names)
print("model_versions:", model_versions)
print("system_uids:", system_uids)
print("testing_times:", testing_times)

import subprocess

result = subprocess.run(['python3', 'prepare_re_deployment.py'], capture_output=True, text=True)
output = result.stdout.strip()

env = []
context = []
model = []
version = []
sysuid = []
testingtime = []

for line in output.split('\n'):
    parts = line.split('=')
    for j, part in enumerate(parts):
        if j == 0:
            env.append(part)
        elif j == 1:
            context.append(part)
        elif j == 2:
            model.append(part)
        elif j == 3:
            version.append(part)
        elif j == 4:
            sysuid.append(part)
        elif j == 5:
            testingtime.append(part)

print("Env:", env)
print("Deployment Context:", context)
print("Model Names:", model)
print("Model Versions:", version)
print("SystemUIDs:", sysuid)
print("TestingTime:", testingtime)

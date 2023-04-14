import subprocess

output = subprocess.check_output(['python3', 'prepare_re_deployment.py'], universal_newlines=True)

env = []
context = []
model = []
version = []
sysuid = []
testingtime = []

for line in output.splitlines():
    parts = line.split('=')

    if len(parts) == 6:
        env.append(parts[0])
        context.append(parts[1])
        model.append(parts[2])
        version.append(parts[3])
        sysuid.append(parts[4])
        testingtime.append(parts[5])
    else:
        print(f"Unexpected number of parts in line: {line}")

print(f"Env: {env}")
print(f"Deployment Context: {context}")
print(f"Model Names: {model}")
print(f"Model Versions: {version}")
print(f"SystemUIDs: {sysuid}")
print(f"TestingTime: {testingtime}")

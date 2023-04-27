import sys
output = sys.argv[1]
lines = output.splitlines()
MODEL_VERSIONS = ''
for line in lines:
    # print(line.split(': ')[1])
    if 'MODEL_VERSIONS' in line:
        MODEL_VERSIONS=line.split(': ')[1]
       
print(MODEL_VERSIONS)

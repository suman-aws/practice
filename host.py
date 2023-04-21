import sys
output = sys.argv[1]
lines = output.splitlines()
DEPLOYMENT_CONTEXT = '';
for line in lines:
    # print(line.split(': ')[1])
    if 'DEPLOYMENT_CONTEXT' in line:
        DEPLOYMENT_CONTEXT=line.split(': ')[1];
       
print(DEPLOYMENT_CONTEXT)
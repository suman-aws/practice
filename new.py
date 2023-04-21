import sys
output = sys.argv[1]
lines = output.splitlines()
ENVironment = ''
for line in lines:
    # print(line.split(': ')[1])
    if 'ENVironment' in line:
        ENVironment=line.split(': ')[1]
       
print(ENVironment)
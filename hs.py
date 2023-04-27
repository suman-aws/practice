import sys
# output = sys.argv[1]
MODEL = ("T-PR" "LR")
lines = MODEL.splitlines()
MODEL_NAMES = ''
for line in lines:
    # print(line.split(': ')[1])
    if 'MODEL_NAMES' in line:
        MODEL_NAMES=line.split(': ')[1]
       
print(MODEL_NAMES)
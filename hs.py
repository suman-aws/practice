import sys
n = len(sys.argv[1])
env = sys.argv[1][1 : n - 1]
env = env.split(", ")

# e = []
host = []
for i in range(len(env)):
    e = env[i].split(" ")
for i in range(len(e)):
    f = e[i].split(",")
# print(str(f))
if "INT" in f:
    host.append('abc.host.7')
elif "QA" in f:
    host.append('abc.host.3')
elif "PROD" in f:
    host.append('abc.host.5')
    
print(host)

import sys 
model = ['INT']
envi = ['Apple']
stdoutOrigin=sys.stdout 
sys.stdout = open("model_list.txt", "w")

# for i in range(len(model)):
print (str(model)+'='+str(envi))
sys.stdout.close()
sys.stdout=stdoutOrigin




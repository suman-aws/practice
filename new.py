model=['Water.wa','sample.Water.s']
envir=['abc qa','abc qa']
version=[1.0,2.0]
hsiuid=[1,2]
tableName=['Mango','Tango']
model_details = []
deployment_models = []
# for i in range(len(model)):
#   print(envir[i]+'='+model[i]+'='+str(version[i]))
# for i in range(len(model)):
#     deployment_models.append([str(model[i])+','+str(version[i])])
    # deployment_models.append(context[i])
    # deployment_models.append(modellist[i])
    # deployment_models.append(version[i])
    # deployment_models.append(sysuid[i])
    # deployment_models.append(testingtime[i])
# print (str(deployment_models))
# envr = []
# def environement(envir):

#     if "qa" in envir:
#         env.append("QA") 
#     return env
# envi = []
for i in range(len(envir)):
    
    if envir[i].find("INT") >= 0:
        envi ="int"
    if envir[i].find("qa") >= 0:
        envi ="qa"
    if envir[i].find("prod") >= 0:
        envi ="prod"
        
    
print(model)
print(envir)
print(version)
print(tableName)
print(envi)

# model_details.append(model)
# model_details.append(envir)
# model_details.append(version)
# model_details.append(tableName)
# print(model_details)

# print("model details:",model)
# # print("environment:",envir)
# print("version details:",version)

# for i in range(len(model)):
#     # print(str(model[i])+'='+str(version[i])+'='+str(hsiuid[i]))
#     print(envi[i]+'='+(model[i]) +'='+str(version[i]))ion)

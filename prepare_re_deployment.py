import yaml

# with open("model_list_for_deployment.yml") as file:
#     document = yaml.safe_load(file)


# env = []
# context = []
# modellist = []
# version = []

# for i in range (len(document)):
#     for j in document[i].items():
#         for d in j[1].items():
#             for m in d[1]:
#                 for v in m.items():
#                     env.append(j[0])
#                     context.append(d[0])
#                     modellist.append(v[0])
#                     version.append(v[1])

#                    #print(j[0]+'='+d[0]+'='+v[0]+'='+v[1])  #env, context, model name, version

# with open("model_details_for_deployment.yml") as f:
#     doc = yaml.safe_load(f)

# sysuid = []
# testingtime = []
# for key, value in doc.items():
#     for k,v in value.items():
#             if k == 'SystemUIDs':
#                 sysuid.append(v)
#             if k == 'TestingTime':
#                 testingtime.append(v)


# for i in range(len(modellist)):
#     print(env[i]+'='+context[i]+'='+modellist[i]+'='+version[i]+'='+str(sysuid[i])+'='+str(testingtime[i]))

# # print(sysuid)
# # print(testingtime)

with open("model_detailsdeployment.yml") as f:
    doc = yaml.safe_load(f)

sysuid = []
testingtime = []
env = []
context = []
modellist = []
version = []
for key, value in doc.items():
    for k,v in value.items():
            if k == 'SystemUIDs':
                sysuid.append(v)
            if k == 'TestingTime':
                testingtime.append(v)
            if k == 'DeploymentEnv':
                env.append(v)
            if k == 'DeploymentContext':
                context.append(v)
            if k == 'ModelUID':
                modellist.append(v)
            if k == 'ModelVersion':
                version.append(v)

for i in range(len(modellist)):
    print(env[i]+'='+context[i]+'='+modellist[i]+'='+version[i]+'='+str(sysuid[i])+'='+str(testingtime[i]))
# model_names = [name.strip() for name in env]
# print("ENVironment:",env)

# print(model_names)
# print("DEPLOYMENT_CONTEXT:",context)
# print("MODEL_NAMES:",modellist)
# print("MODEL_VERSIONS:",version)
# print("SYSTEM_UIDS:",sysuid)
# print("TESTING_TIMES:",testingtime)

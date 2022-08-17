import yaml

with open("Model_list.yml") as file:
    document = yaml.safe_load(file)


env = []


for i in range (len(document)):
    for j in document[i].items():
        for d in j[1].items():
            for m in d[1]:
                for v in m.items():
                    env.append(j[0])
                    # context.append(d[0])
                    # modellist.append(v[0])
                    # version.append(v[1])

                   #print(j[0]+'='+d[0]+'='+v[0]+'='+v[1])  #env, context, model name, version
                    # print(j[0])  #env, context, model name, version

with open("Model_details.yml") as f:
    doc = yaml.safe_load(f)

Host = []
testingtime = []
for key, value in doc.items():
    for k,v in value.items():
            if k == 'ServiceURL':
                Host.append(v)
print(Host)

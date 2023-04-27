import yaml

with open('model_detailsdeployment.yml') as file:
    data = yaml.load(file, Loader=yaml.FullLoader)

model_name = data['ModelName']
model_version = data['ModelVersion']
system_uids = data['SystemUIDs']
testing_time = data['TestingTime']

print(f"Model Name: {model_name}")
print(f"Model Version: {model_version}")
print(f"System UIDs: {system_uids}")
print(f"Testing Time: {testing_time}")


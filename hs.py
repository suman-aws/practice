import os

# Replace this with the Python code that generates your output
output = "['M1','M2'] [V1,V2] ['QA','QA']"

# Parse the output
model_names, model_versions, deployment_contexts = [], [], []
for value in output.split():
    if value.startswith("['"):
        model_names.append(value.strip("[,']"))
    elif value.startswith("[") and value.endswith("]"):
        model_versions.append(value.strip("[]"))
    elif value.startswith("'") and value.endswith("'"):
        deployment_contexts.append(value.strip("'"))

# Set the environment variables for use in GitHub Actions
os.environ["MODEL_NAMES"] = ",".join(model_names)
os.environ["MODEL_VERSIONS"] = ",".join(model_versions)
os.environ["DEPLOYMENT_CONTEXTS"] = ",".join(deployment_contexts)

# Print the parsed values for verification
print("Model Names:", model_names)
print("Model Versions:", model_versions)
print("Deployment Contexts:", deployment_contexts)

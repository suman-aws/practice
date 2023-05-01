output_string = "ENVironment: ['QA', 'QA']\nDEPLOYMENT_CONTEXT: ['RW', 'RW+RS']\nMODEL_NAMES: ['T-PR', 'LR']\nMODEL_VERSIONS: ['1.0', '1.0']\nSYSTEM_UIDS: ['77276535', '77276535']\nTESTING_TIMES: ['20230218-235959', '20230218-235959']"

# Split the output string by newline character to get separate lines
output_lines = output_string.split("\n")

# Create an empty dictionary to store variable name and value pairs
output_dict = {}

# Iterate over each line in the output and split the variable name and value
for line in output_lines:
    # Split the line by colon character to get the variable name and value
    variable_name, value_string = line.split(": ")
    # Remove any whitespace around the variable name
    variable_name = variable_name.strip()
    # Remove the square brackets and single quotes around the value
    value_string = value_string.strip("[]").replace("'", "")
    # Split the value string by comma to get separate values
    values = value_string.split(", ")
    # Store the variable name and values in the output dictionary
    output_dict[variable_name] = values

# Create separate variables for each value in the output dictionary
environment = output_dict["ENVironment"]
deployment_context = output_dict["DEPLOYMENT_CONTEXT"]
model_names = output_dict["MODEL_NAMES"]
model_versions = output_dict["MODEL_VERSIONS"]
system_uids = output_dict["SYSTEM_UIDS"]
testing_times = output_dict["TESTING_TIMES"]

# Print the values of the separate variables
print(environment)
print(deployment_context)
print(model_names)
print(model_versions)
print(system_uids)
print(testing_times)

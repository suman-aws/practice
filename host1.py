models = ["model1","model2","model3"]
versions = ["v1","v2","v3"]

models_str = '(' + ' '.join(['"{}"'.format(x) for x in models]) + ')'
versions_str = '(' + ' '.join(['"{}"'.format(x) for x in versions]) + ')'

print(models_str)    # Output: ("model1" "model2" "model3")
print(versions_str)  # Output: ("v1" "v2" "v3")



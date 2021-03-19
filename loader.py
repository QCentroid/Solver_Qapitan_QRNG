input_file_name = "input.json"

################################################
#########    DO NOT TOUCH FROM HERE    #########
################################################
# Input data loader. Container will get data from here
import json
with open(input_file_name) as f:
  input_data = json.load(f)

# Optional extra parameters
if "arguments" in input_data:
    extra_arguments = input_data['arguments']
else:
    extra_arguments = {}


import main
result = main.run(input_data)
print(result)

################################################
#########    DO NOT UNTIL FROM HERE    #########
################################################
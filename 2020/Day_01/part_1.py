import os
import sys
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

input_data = []
with open(abs_file_path, 'r') as f:
    for line in f:
        input_data.append(int(line.rstrip()))

def twoSum(nums, target):
    seen = {}
    for i,v in enumerate(input_data):
        complement = target - v
        if complement in seen:
            return [seen[complement],i]
        else:
            seen[v] = i

target = 2020
resultIndices = twoSum(input_data, target)
result = input_data[resultIndices[0]] * input_data[resultIndices[1]]
print(result)
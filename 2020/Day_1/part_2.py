import os
import sys
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

input_data = []
with open(abs_file_path, 'r') as f:
    for line in f:
        input_data.append(int(line.rstrip()))

def threeSum(nums, target):
    n = len(nums)
    nums.sort()
    for i in range(0, n - 2):
        a = nums[i]
        start = i + 1
        end = n - 1
        while start < end:
            b = nums[start]
            c = nums[end]
            if a + b + c == target:
                return [i, start, end]
            elif a + b + c > 0:
                end -= 1
            else:
                start += 1

target = 2020
resultIndices = threeSum(input_data, target)
result = input_data[resultIndices[0]] * input_data[resultIndices[1]] * input_data[resultIndices[2]]
print(result)
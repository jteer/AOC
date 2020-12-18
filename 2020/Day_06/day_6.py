import os
import sys
from functools import reduce

rel_path = "input.txt"
script_dir = os.path.dirname(__file__)
abs_file_path = os.path.join(script_dir, rel_path)

input_data = open(abs_file_path).read().split("\n\n")
# input_data = open(abs_file_path).read().split("\n")
# groups = []
# temp = []
# for i in input_data:
#     if i == '':
#         groups.append(temp)
#         temp = []
#     else:
#         temp.append(i)

# Find the count of distinct characters in each group and sum them
part_1 = sum([len(set(''.join(group).replace('\n', ''))) for group in input_data])
print(f'part 1: {part_1}')

# For each group reduce down only the characters that occur in every line of a group
# Get the count of those characters and sum
part_2 = sum([(len(reduce(lambda x, y: set(x) & set(y), group.split('\n')))) for group in input_data])
print(f'part 2: {part_2}')

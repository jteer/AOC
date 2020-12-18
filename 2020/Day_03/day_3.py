import os
import sys

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

input_data = []
with open(abs_file_path, 'r') as f:
    for line in f:
        input_data.append(line.rstrip())


def part1(input_data, r, d, tree):
    if not input_data:
        return
    n, m = len(input_data), len(input_data[0])
    ans = 0
    j = 0
    for i in range(0, n, d):
        if input_data[i][j] == tree:
            ans += 1
        j = (j + r) % m

    return ans

def part2(input_data, slopes, tree):
    ans = 1
    for r,d in slopes:
        ans *= part1(input_data, r, d, tree)
    return ans

part_1_ans = part1(input_data, 3, 1, '#')
print(f'part 1: {part_1_ans}')

part_2_slopes = [ [1,1], [3,1], [5,1], [7,1], [1,2]]
part_2_ans = part2(input_data, part_2_slopes, '#')
print(f'part 2: {part_2_ans}')
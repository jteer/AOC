import os
import sys
sys.path.append('..\AOC')
from Utils.utils import timer
rel_path = "input.txt"
script_dir = os.path.dirname(__file__)
abs_file_path = os.path.join(script_dir, rel_path)

input_data = []
with open(abs_file_path, 'r') as f:
    for line in f:
        input_data.append(line.rstrip())

def cost(x):
    x = abs(x)
    return ((x + 1) * x) // 2

@timer
def part1(data):
    data = list(map(int, data[0].split(',')))
    return min(sum((abs(d - i)) for d in data) for i in data)

@timer                    
def part2(data):
    data = list(map(int, data[0].split(',')))
    return min(sum(cost(i - d) for d in data) for i in range(min(data), max(data) + 1))

# https://adventofcode.com/2021/day/7
if __name__ == "__main__":
    print(part1(input_data))
    print(part2(input_data))

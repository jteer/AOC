import os
import sys
sys.path.append('..\AOC')
from Utils.utils import timer
import numpy as np
from functools import reduce

rel_path = "input.txt"
script_dir = os.path.dirname(__file__)
abs_file_path = os.path.join(script_dir, rel_path)

input_data = []
with open(abs_file_path, 'r') as f:
    for line in f:
        input_data.append(int(line.rstrip()))

part1 = lambda: reduce(lambda acc, i: acc + int(input_data[i] > input_data[i - 1]), range(1, len(input_data)), 0) 
# lambda data: sum(data[i] > data[i-1] for i in range(len(data)))

part2 = lambda nums: reduce(lambda acc, i: acc + int(nums[i] > nums[i - 3]), range(3, len(nums)), 0)
# lambda data, window_size=3: part1(np.convolve(data,np.ones(window_size,dtype=int),'valid'))

# https://adventofcode.com/2021/day/1
if __name__ == "__main__":
    print(part1())
    print(part2(input_data))

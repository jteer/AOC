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
        input_data.append(line.rstrip().split(' '))

@timer
def part1(input_data):
    h = sum(int(i[1]) for i in input_data if i[0] == 'forward')
    d = sum(int(i[1]) if i[0] == 'up' else -int(i[1]) if i[0] == 'down' else 0 for i in input_data)    
    return h * abs(d)

@timer
def part2(input_data):
    h,d,a = 0,0,0
    for line in input_data:
        if(line[0] == 'forward'):
            h += int(line[1])
            d += a * int(line[1])
        if(line[0] == 'up'):
            a -= int(line[1])
        if(line[0] == 'down'):
            a += int(line[1])
    return h * abs(d)

# https://adventofcode.com/2021/day/2
if __name__ == "__main__":
    print(part1(input_data))
    print(part2(input_data))

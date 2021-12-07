import os
import sys
sys.path.append('..\AOC')
from Utils.utils import timer
rel_path = "input.txt"
script_dir = os.path.dirname(__file__)
abs_file_path = os.path.join(script_dir, rel_path)

input_data = []
with open('input.txt', 'r') as f:
    for line in f:
        input_data.append(line.rstrip())

def sim(data, days=80):
    fish_counts = [data.count(i) for i in range(9)]
    for i in range(days):
        fish_counts[(i + 7) % 9] += fish_counts[i % 9]
    return sum(fish_counts)

@timer
def part1(data):
    data = list(map(int, data[0].split(',')))
    return sim(data, days=80)

@timer                    
def part2(data):
    data = list(map(int, data[0].split(',')))
    return sim(data, days=256)

# https://adventofcode.com/2021/day/6
if __name__ == "__main__":
    print(part1(input_data))
    print(part2(input_data))

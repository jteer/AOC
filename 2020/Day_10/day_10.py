import os
import sys
sys.path.append('..\AOC')
from Utils.utils import timer
from collections import Counter
from collections import defaultdict
rel_path = "input.txt"
script_dir = os.path.dirname(__file__)
abs_file_path = os.path.join(script_dir, rel_path)
input_data = open(abs_file_path).read().splitlines()


@timer
def part1(joltage_adapters):
    sorted_adapters = sorted(joltage_adapters + [0, max(joltage_adapters) + 3 ])
    diff = [j-i for i, j in zip(sorted_adapters[:-1], sorted_adapters[1:])] 
    counted_diff = Counter(diff)
    part1 = counted_diff[1] * counted_diff[3]
    print(f'part 1: {part1}')

@timer
def part2(joltage_adapters):
    mod_joltage_adapters = sorted(joltage_adapters + [max(joltage_adapters) + 3])    
    counts = defaultdict(int)
    counts[0] = part2 = 1
    for i in mod_joltage_adapters:
        counts[i] = part2 = counts[i - 1] + counts[i - 2] + counts[i - 3]
    print(f'part 2: {part2}')

if __name__ == "__main__":
    parsed_input = [int(i) for i in input_data]
    part1(parsed_input)
    part2(parsed_input)
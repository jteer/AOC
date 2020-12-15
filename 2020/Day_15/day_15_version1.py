import os
import sys

from collections import defaultdict
sys.path.append('..\AOC')
from Utils.utils import timer

rel_path = "input.txt"
script_dir = os.path.dirname(__file__)
abs_file_path = os.path.join(script_dir, rel_path)
input_data = open(abs_file_path).read().splitlines()


def recite(total_turns):
    pass


@timer
def part1(numbers):
    total_turns = 2020

    seen = defaultdict(lambda: [0, []])
    prev, turn = 0, 1
    for i in numbers:
        seen[i][0] += 1
        seen[i][1].append(turn)
        prev = i
        turn += 1

    while turn <= total_turns:
        c = seen[prev]
        prev = 0 if c[0] == 1 else c[1][-1] - c[1][-2]
        seen[prev][0] += 1
        seen[prev][1].append(turn)
        turn += 1

    print(f'part 1: {prev}')


@timer
def part2(numbers):
    total_turns = 30000000

    seen = {v: i+1 for i, v in enumerate(numbers)}
    prev = 0
    for turn in range(len(seen)+1, total_turns):
        if prev in seen:
            seen[prev], prev = turn, turn - seen[prev]
            # age = turn - seen[prev]
            # seen[prev] = turn
            # prev = age
        else:
            seen[prev], prev = turn, 0

    print(f'part 2: {prev}')


if __name__ == "__main__":
    # print(input_data)
    parsed_input = [int(j) for i in input_data for j in i.split(',')]
    part1(parsed_input)
    part2(parsed_input)

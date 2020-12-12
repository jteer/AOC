import copy
import os
import sys
sys.path.append('..\AOC')
from Utils.utils import timer

rel_path = "input.txt"
script_dir = os.path.dirname(__file__)
abs_file_path = os.path.join(script_dir, rel_path)
input_data = open(abs_file_path).read().splitlines()

DIRECTIONS = { 'N': 0 + 1j, 'S': 0 + - 1j, 'E': 1 + 0j, 'W': -1 + 0j}
FACE = {'R': 0 - 1j, 'L': 0 + 1j}

@timer
def part1(data):
    position = 0 + 0j
    direction_facing = DIRECTIONS['E']
    for action, unit in data:
        if action in DIRECTIONS:
            position += DIRECTIONS[action] * unit
        elif action in FACE:
            direction_facing *= FACE[action] ** (unit // 90)
        elif action == 'F':
            position += direction_facing * unit

    man_distance = abs(int(position.real)) + abs(int(position.imag))
    print(f'part 1: {man_distance}')


@timer
def part2(data):
    position = 0 + 0j
    way = 10 + 1j
    for action, unit in data:
        if action in DIRECTIONS:
            way += DIRECTIONS[action] * unit
        elif action in FACE:
            way *= FACE[action] ** (unit // 90)
        elif action == 'F':
            position += way * unit

    man_distance = abs(int(position.real)) + abs(int(position.imag))
    print(f'part 2: {man_distance}')


if __name__ == "__main__":
    parsed_input = [(i[0], int(i[1:])) for i in input_data]
    part1(parsed_input)
    part2(parsed_input)

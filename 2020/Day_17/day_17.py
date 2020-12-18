import os
import sys
import re
from collections import defaultdict
from itertools import product
import json
sys.path.append('..\AOC')
from Utils.utils import timer
rel_path = "input.txt"
script_dir = os.path.dirname(__file__)
abs_file_path = os.path.join(script_dir, rel_path)
input_data = open(abs_file_path).read().splitlines()


def simulate_generations(start_slice, dimensions=2, generations=1):
    zeros = [0] * (dimensions - 2)
    dim_coordinates = {
        *product((-1, 0, 1), repeat=dimensions)} - {(0, 0, *zeros)}
    active_cubes = {(row, col, *zeros) for row, line in enumerate(start_slice) for col, char in enumerate(line) if char == "#"}
    # print(active_cubes)

    for gen in range(generations):
        neighbor_counts = defaultdict(int)
        for cube in active_cubes:
            for coordinate in dim_coordinates:
                neighbor_counts[tuple(sum(x) for x in zip(cube, coordinate))] += 1

        # print (json.dumps(({str(k):v for k,v in neighbors.items()}),indent=4))

        active_cubes = {neighbor for neighbor, count in neighbor_counts.items() if count == 3 or (count == 2 and neighbor in active_cubes)}

    return len(active_cubes)


@timer
def part1(data):
    print(f'part 1: {simulate_generations(data, 3, 6)}')


@timer
def part2(data):
    print(f'part 2: {simulate_generations(data, 4, 6)}')


if __name__ == "__main__":
    parsed_input = [list(i) for i in input_data]
    # print(parsed_input)
    part1(parsed_input)
    part2(parsed_input)

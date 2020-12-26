import os
import sys

sys.path.append('..\AOC')
from Utils.utils import timer
rel_path = "input.txt"
script_dir = os.path.dirname(__file__)
abs_file_path = os.path.join(script_dir, rel_path)

input_data = open(abs_file_path).read().splitlines()

def crab_cups(cups, max_n, rounds):
    new_cups = [0] * (max_n + 1)
    first = curr = cups[0]
    for i in range(1, len(cups)):
        cups[curr] = cups[i]
        curr = new_cups[curr]
    for idx in range(len(cups)+1, max_n+1):
        cups[curr] = idx
        curr = idx

    cups[curr], curr = first, first
    
    for i in range(rounds):
        removed = (a := new_cups[curr], b := new_cups[a], c := new_cups[b])
        dest = curr - 1 if curr > 1 else max_n
        while dest in removed:
            dest = dest - 1 if dest > 1 else max_n

        cups[curr] = new_cups[c]
        cups[c] = new_cups[dest]
        cups[dest] = a
        curr = new_cups[curr]

    return new_cups

@timer
def part1(cups):
    cup_order = crab_cups(cups, 9, 100)
    print(cup_order)
    res, cup = '', cup_order[1]
    while cup != 1:
        res += str(cup)
        cup = cup_order[cup]
    
    print(f'part 1: {res}')


@timer
def part2(cups):
    cup_order = crab_cups(cups, 1000000, 10000000)
    # print(cup_order)
    cup = cup_order[1]
    print(f'part 2: {cup * cup_order[cup]}')


if __name__ == "__main__":
    print(input_data)
    parsed_data = [int(cup) for cup in input_data[0]]
    part1(parsed_data)
    part2(parsed_data)

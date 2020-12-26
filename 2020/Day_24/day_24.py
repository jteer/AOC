from collections import Counter
import os
import sys

sys.path.append('..\AOC')
from Utils.utils import timer
rel_path = "input.txt"
script_dir = os.path.dirname(__file__)
abs_file_path = os.path.join(script_dir, rel_path)

input_data = open(abs_file_path).read().splitlines()

def solve(puzzle, part2=False):
    def get_neighbors(x,y):
        for dx, dy in dirs.values():
            yield x + dx, y + dy

    dirs = dict(
        e=(2, 0),se=(1, 1),sw=(-1, 1),
        w=(-2, 0),nw=(-1, -1),ne=(1, -1))
    
    endPos = []
    for line in puzzle:
        pos = 0
        x = y = 0
        while pos < len(line):
            for l in range(1, 3):
                if (char := line[pos:pos+l]) in dirs:
                    dx, dy = dirs[char]
                    x += dx
                    y += dy
                    pos += l
                    break
        endPos.append((x, y))
    
    black_tiles = {p for p, x in Counter(endPos).items() if x % 2 == 1}
    
    res = len(black_tiles)
    if part2:
        for _ in range(100):
            neighbors = Counter([n for p in black_tiles for n in get_neighbors(*p)])
            black_tiles = {p for p, x in neighbors.items() if x == 2 or (x == 1 and p in black_tiles)}
        res = len(black_tiles)
    
    return res


@timer
def part1(data):
    res = solve(data)
    print(f'part 1: {res}')


@timer
def part2(data):
    res = solve(data, True)
    print(f'part 2: {res}')


if __name__ == "__main__":
    # print(input_data)
    part1(input_data)
    part2(input_data)

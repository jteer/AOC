import ast
import collections
import os
import sys
from itertools import groupby
from functools import reduce

sys.path.append('..\AOC')
from Utils.utils import timer
rel_path = "input.txt"
script_dir = os.path.dirname(__file__)
abs_file_path = os.path.join(script_dir, rel_path)
input_data = open(abs_file_path).read().splitlines()

def parse_data(input_data):
    tiles_raw = [list(sub) for ele, sub in groupby(input_data, key = bool) if ele] 
    parsed_tiles = {}
    for tile in tiles_raw:
        tile_id = int(tile[0].split()[1][:-1])
        tile_data = tile[1:]
        # print(tile_data)
        parsed_tiles[tile_id] = tile_data
    return parsed_tiles

def get_edges(tile):
    e = [tile[0], tile[-1], ''.join(row[0] for row in tile), ''.join(row[-1] for row in tile)]
    return e + [i[::-1] for i in e]

def orient(tile):
    for _ in range(2):
        yield tile
        yield tile[::-1]
        yield [row[::-1] for row in tile]
        yield [row[::-1] for row in tile[::-1]]
        tile = list(map(''.join, zip(*tile)))  

def solve_image(tiles, corners):  
    def make_row(possible, c, f):
        row = [c]
        while True:
            tile_added = False
            for tid, tile in list(possible.items()):
                for temp in orient(tile):
                    if f(row[-1], temp):
                        row.append(temp)
                        del possible[tid]
                        tile_added = True
                        break
            if not tile_added:
                return row

    possible = dict(tiles)
    for corner in corners:
        corner = possible.pop(corner)
        left = make_row(possible, corner, lambda old, new: old[-1] == new[0])
        rows = [make_row(possible, tile, lambda old, new: all(x[-1] == y[0] for x, y in zip(old, new))) for tile in left]
        if not possible:
            return [ ''.join(subrow[1:-1] for subrow in l) for r in rows for l in zip(*(part[1:-1] for part in r))]
    return None

@timer
def part1(tiles):
    edge_counts = collections.Counter(e for tile in tiles.values() for e in get_edges(tile))
    res = reduce((lambda x, y: x * y), sorted(tiles, key=lambda tile_id: sum(1 for e in get_edges(tiles[tile_id]) if edge_counts[e] > 1))[:4])
    print(f'part 1: {res}')

@timer
def part2(tiles):
    edge_counts = collections.Counter(e for tile in tiles.values() for e in get_edges(tile))
    corners = sorted(tiles, key=lambda tile_id: sum(1 for e in get_edges(tiles[tile_id]) if edge_counts[e] > 1))[:4]
    image = solve_image(tiles, corners)
    
    monster = ['                  # ',
               '#    ##    ##    ###', 
               ' #  #  #  #  #  #   ']
    
    locations = set()
    h, w = len(image), len(image[0])
    for oriented_monster in orient(monster):
        active = [ (i, j) for i, monster_row in enumerate(oriented_monster) for j, c in enumerate(monster_row) if c == '#']
        for i in range(h - len(oriented_monster)):
            for j in range(w - len(oriented_monster[0])):
                loc = {(i + di, j + dj) for (di, dj) in active}
                if all(image[i1][j1] == '#' for i1, j1 in loc):
                    locations |= loc

    monster_count = sum(1 for row in image for x in row if x == '#') - len(locations)
    print(f'part 2: {monster_count}')

if __name__ == "__main__":
    # print(input_data)
    parsed_data = parse_data(input_data)
    part1(parsed_data)
    part2(parsed_data)

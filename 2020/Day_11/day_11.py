import os
import sys
sys.path.append('..\AOC')
from Utils.utils import timer
import copy
rel_path = "input.txt"
script_dir = os.path.dirname(__file__)
abs_file_path = os.path.join(script_dir, rel_path)
input_data = open(abs_file_path).read().splitlines()

def neighbors(row, col, seats):
    max_col = len(seats[0])
    max_row = len(seats)
    neighbors = [(row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
                (row, col - 1),                      (row, col + 1),
                (row + 1, col - 1),  (row + 1, col), (row + 1, col + 1)]
    return list(filter(lambda p: p[0] >= 0 and p[0] < max_row and p[1] >= 0 and p[1] < max_col, neighbors))

def seated_neighbors(r, c, seats):
    return list(filter(lambda x: seats[x[0]][x[1]] == '#',  neighbors(r, c, seats)))

def part1(data):
    data_copy = copy.deepcopy(data)
    while True:
        changes = False
        for i, r in enumerate(data):
            for j, seat in enumerate(r):
                seated_neighbor_count = len(seated_neighbors(i, j, data))
                if seat == 'L' and seated_neighbor_count == 0:
                    data_copy[i][j] = '#'
                    changes = True
                elif seat == '#' and seated_neighbor_count >= 4:
                    data_copy[i][j] = 'L'
                    changes = True
        data = copy.deepcopy(data_copy)
        if not changes:
            break

    total_occ = 0
    for i in data:
        total_occ += i.count('#')

    print(f'part 1: {total_occ}')


def can_see(data, r, c, dr, dc):
    if r < 0 or r == len(data) or c < 0 or c == len(data[0]) or data[r][c] == 'L':
        return False
    if data[r][c] == '#':
        return True
    return can_see(data, r+dr, c+dc, dr, dc)


def part2(data):
    while True:
        changes = False
        r, c = len(data), len(data[0])
        data_copy = copy.deepcopy(data)
        for i in range(r):
            for j in range(c):
                if data[i][j]== '.':
                    continue
            
                seat_count = 0
                seat_count += can_see(data, i-1, j-1, -1, -1)
                seat_count += can_see(data, i-1, j  , -1,  0)
                seat_count += can_see(data, i-1, j+1, -1,  1)
                seat_count += can_see(data, i  , j-1,  0, -1)
                seat_count += can_see(data, i  , j+1,  0,  1)
                seat_count += can_see(data, i+1, j-1,  1, -1)
                seat_count += can_see(data, i+1, j  ,  1,  0)
                seat_count += can_see(data, i+1, j+1,  1,  1)
                
                if data[i][j] == 'L' and seat_count == 0:
                    changes = True
                    data_copy[i][j] = '#'
                elif data[i][j] == '#' and seat_count >= 5:
                    changes = True
                    data_copy[i][j] = 'L'
        
        data = copy.deepcopy(data_copy)
        if not changes:
            break

    total_occ = 0
    for i in data:
        total_occ += i.count('#')

    print(f'part 2: {total_occ}')

if __name__ == "__main__":
    parsed_data = [ list(i) for i in input_data ]
    part1(parsed_data)
    part2(parsed_data)
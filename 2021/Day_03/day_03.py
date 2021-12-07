import os
from collections import Counter
import sys
sys.path.append('..\AOC')
from Utils.utils import timer
rel_path = "input.txt"
script_dir = os.path.dirname(__file__)
abs_file_path = os.path.join(script_dir, rel_path)

input_data = []
with open(abs_file_path, 'r') as f:
    for line in f:
        input_data.append(line.rstrip())

def column(matrix, i):
    return [row[i] for row in list(matrix)]

# returns if this value is the most common in this column by summing the col and checking
# if the sum is >= to the col length / 2
def most_common(col_n, data):
    return sum(int(line[col_n]) for line in data) >= len(data)/2

@timer
def part1(input_data):
    gamma = sum(2**(len(input_data[0])-col-1) * most_common( col, input_data) for col in range(len(input_data[0])))
    epsilon = 2**len(input_data[0]) - 1 - gamma
    return(gamma * epsilon)

@timer
def part2(codes):
    oxygen = codes[:]
    i = 0
    while len(oxygen) != 1:
        c = Counter(column(oxygen, i))
        k = '1' if c.most_common(1)[0][1] == c.most_common()[-1][1] else c.most_common(1)[0][0]
        oxygen = [j for j in oxygen if j[i] == k]
        i += 1

    co2 = codes[:]    
    i = 0 
    while len(co2) != 1:
        c = Counter(column(co2, i))
        k = '0' if c.most_common(1)[0][1] == c.most_common()[-1][1] else c.most_common()[-1][0]
        co2 = [j for j in co2 if j[i] == k]
        i +=1
    
    return int(co2[0],2) * int(oxygen[0], 2)

# https://adventofcode.com/2021/day/3
if __name__ == "__main__":
    print(part1(input_data))
    print(part2(input_data))
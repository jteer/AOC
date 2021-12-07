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


@timer
def part1(line_data):
    c = Counter()
    for line in line_data:
        line = line.split()
        x1 = int(line[0].split(",")[0])
        y1 = int(line[0].split(",")[1])
        x2 = int(line[2].split(",")[0])
        y2 = int(line[2].split(",")[1])
        if x1==x2 or y1==y2:
            for x in range(min(x1,x2),max(x1,x2)+1):
                for y in range(min(y1,y2),max(y1,y2)+1):
                    c[(x,y)] +=1
    return sum(c > 1 for c in c.values())
                
@timer
def part2(line_data):
    c = Counter()
    for line in line_data:
        line = line.split()
        x1 = int(line[0].split(",")[0])
        y1 = int(line[0].split(",")[1])
        x2 = int(line[2].split(",")[0])
        y2 = int(line[2].split(",")[1])
        
        dx = (x2-x1) // (abs(x2-x1) or 1) # numpy.sign()?
        dy = (y2-y1) // (abs(y2-y1) or 1)
        c[(x1,y1)] += 1
        while x1 != x2 or y1 != y2:
            x1 += dx
            y1 += dy
            c[(x1,y1)] += 1

    return sum(c > 1 for c in c.values())

# https://adventofcode.com/2021/day/5
if __name__ == "__main__":
    print(part1(input_data))
    print(part2(input_data))

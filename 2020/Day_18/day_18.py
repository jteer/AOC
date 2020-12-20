import ast
import os
import sys

sys.path.append('..\AOC')
from Utils.utils import timer
rel_path = "input.txt"
script_dir = os.path.dirname(__file__)
abs_file_path = os.path.join(script_dir, rel_path)
input_data = open(abs_file_path).read().splitlines()


def my_eval(equation):
    root = ast.parse(equation, mode='eval')
    for n in ast.walk(root):
        if type(n) is ast.BinOp:
            n.op = ast.Add() if type(n.op) is ast.Div else ast.Mult()
    return eval(compile(root, '<string>', 'eval'))

@timer
def part1(data):
    # Replace + operation with / so addition has the same precedence as multiplication
    res = sum( my_eval(line.replace('+', '/')) for line in data)
    print(f'part 1: {res}')


@timer
def part2(data):
    # Replace + operation with / so addition has the same precedence as multiplication
    # Replace * with + so multiplication happens after addition
    res = sum( my_eval(line.replace('+','/').replace('*', '+')) for line in data)
    print(f'part 2: {res}')


if __name__ == "__main__":
    # print(input_data)
    part1(input_data)
    part2(input_data)

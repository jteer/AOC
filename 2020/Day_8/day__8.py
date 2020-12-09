import os
import copy
from collections import deque

rel_path = "input.txt"
script_dir = os.path.dirname(__file__)
abs_file_path = os.path.join(script_dir, rel_path)
input_data = open(abs_file_path).read().splitlines()


def parse_input(input_data):
    return [ op.split(' ') for op in input_data]

def run_program(program):
    """
    Returns:
        list: [return code, accumulator, [executed operations]]
    """
    i, acc = 0, 0
    seen = set()
    executed_ops = deque()
    while True:
        if i >= len(program):
            # return code, accumulator, executed operations
            # return codes -> 0 = success, -1 = fail
            return [0, acc, executed_ops]
        elif i in seen:
            return [-1, acc, executed_ops]
        
        executed_ops.append(i)
        seen.add(i)
        line = program[i]
        op, v = line[0], int(line[1])
        if op == 'acc':
            acc += v
            i+=1
        elif op == 'jmp':
            i += v
        elif op == 'nop':
            i+=1
    
def fix_code(program, replacements, possible_replacements):
    while possible_replacements:
        i = possible_replacements.pop()
        code_copy = copy.deepcopy(program)
        if code_copy[i][0] in replacements:
            code_copy[i][0] = replacements[code_copy[i][0]]
            new_code_res = run_program(code_copy)
            if new_code_res[0] == 0:
                return [new_code_res, code_copy]

if __name__ == "__main__":
    # print(input_data)
    program = parse_input(input_data)
    
    program_results = run_program(program)
    # print(program_results)

    print(f'part 1: {program_results[1]}')

    replacements = { 'jmp': 'nop', 'nop':'jmp'}
    fixed_code_results = fix_code(program, replacements, program_results[2])
    print(f'part 2: {fixed_code_results[0][1]}')


import os
import re
import sys
import itertools

from collections import defaultdict
sys.path.append('..\AOC')
from Utils.utils import timer

rel_path = "input.txt"
script_dir = os.path.dirname(__file__)
abs_file_path = os.path.join(script_dir, rel_path)
input_data = open(abs_file_path).read().splitlines()


@timer
def part1(input_data):
    mask_regex = r'(mask\s=\s)(.*)'
    mem_regex = r'mem\[(\d+)]\s=\s(\d+)'
    mask_len = 36
    mask = 'X' * mask_len
    current_mem = defaultdict(int)
    for line in input_data:
        if (g := re.match(mask_regex, line)):
            mask = g[2]
        else:
            g = re.match(mem_regex, line)
            mem_addr, mem_value = g[1], g[2]
            mem_value_bin = bin(int(mem_value))[2:].zfill(mask_len)
            current_mem[mem_addr] = int(
                ''.join(c if c != 'X' else mem_value_bin[i] for i, c in enumerate(mask)), 2)

    # print(current_mem)
    mem_sum = sum(current_mem.values())
    print(f'part 1: {mem_sum}')


@timer
def part2(input_data):
    mask_regex = r'(mask\s=\s)(.*)'
    mem_regex = r'mem\[(\d+)]\s=\s(\d+)'
    mask_len = 36
    mask = 'X' * mask_len
    current_mem = defaultdict(int)
    for line in input_data:
        if (g := re.match(mask_regex, line)):
            mask = g[2]
        else:
            g = re.match(mem_regex, line)
            mem_addr, mem_value = bin(int(g[1]))[2:].zfill(mask_len), int(g[2])
            # if X or 1 take from mask else take from mem_addr
            masked_mem_addr = [mem_addr[i] if mask_bit ==
                               '0' else mask[i] for i, mask_bit in enumerate(mask)]
            for bits in itertools.product('01', repeat=masked_mem_addr.count('X')):
                replacement_bit_iter = iter(bits)
                new_addr_bits = (next(replacement_bit_iter) if c ==
                                 'X' else c for c in masked_mem_addr)
                current_mem[int(''.join(new_addr_bits), 2)] = mem_value

    mem_sum = sum(current_mem.values())
    print(f'part 2: {mem_sum}')


if __name__ == "__main__":
    part1(input_data)
    part2(input_data)

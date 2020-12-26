from collections import Counter
import os
import sys

sys.path.append('..\AOC')
from Utils.utils import timer
rel_path = "input.txt"
script_dir = os.path.dirname(__file__)
abs_file_path = os.path.join(script_dir, rel_path)

input_data = open(abs_file_path).read().splitlines()


@timer
def part1(data):
    public_key_card, public_key_door = data
    subject, modulus, loop = 7, 20201227, 0
    
    # Baby-Step Giant-Step Algorithm
    n = int(public_key_card ** 0.5)
    table = {pow(subject, j, modulus): j for j in range(n + 1)}
    
    # Fermat’s Little Theorem
    fermat = pow(subject, n * (modulus - 2), modulus)

    while public_key_card not in table.keys():
        loop += 1
        public_key_card = (public_key_card * fermat) % modulus

    encryption_key = pow(public_key_door, loop * n + table[public_key_card], modulus)
    print(f'part 1: {encryption_key}')


if __name__ == "__main__":
    # print(input_data)
    parsed_input = [int(x) for x in input_data]
    # print(parsed_input)
    part1(parsed_input)


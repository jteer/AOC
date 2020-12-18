import os
import sys
sys.path.append('..\AOC')
from Utils.utils import timer

rel_path = "input.txt"
script_dir = os.path.dirname(__file__)
abs_file_path = os.path.join(script_dir, rel_path)
input_data = open(abs_file_path).read().splitlines()


def two_sum(data, target):
    # return any((res := target - p) in data and res != p for p in data)
    seen = {}
    for i, v in enumerate(data):
        complement = target - v
        if complement in seen:
            return True
        else:
            seen[v] = i
    return False


def find(input_data, preamble_len):
    l, r = 0, preamble_len - 1
    i = r + 1
    while i <= len(input_data):
        has_sum = two_sum(input_data[l:r+1], input_data[i])
        if not has_sum:
            return input_data[i]
        i += 1
        l += 1
        r += 1


def get_weakness(data, target):
    l, r = 0, 0
    while l < len(data):
        temp_sum = sum(data[l:r])
        if temp_sum == target:
            break
        elif temp_sum > target:
            l += 1
        elif temp_sum < target:
            r += 1

    weakness_range = data[l:r]
    weakness_range.sort()
    return weakness_range[0] + weakness_range[-1]


@timer
def __main():
    # print(input_data)
    preamble_len = 25
    parsed_input = [int(i) for i in input_data]
    number_missing_sum = find(parsed_input, preamble_len)
    print(f'part 1: {number_missing_sum}')

    weak = get_weakness(parsed_input, number_missing_sum)
    print(f'part 2: {weak}')


if __name__ == '__main__':
    __main()

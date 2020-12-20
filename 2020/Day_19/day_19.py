import ast
import os
import sys

sys.path.append('..\AOC')
from Utils.utils import timer
rel_path = "input.txt"
script_dir = os.path.dirname(__file__)
abs_file_path = os.path.join(script_dir, rel_path)
input_data = open(abs_file_path).read().splitlines()


def check_possible(rules, seq, string):
    if not seq:
        yield string
    else:
        index, *seq = seq
        for string in check(rules, index, string):
            yield from check_possible(rules, seq, string)

def check_expansion(rules, possible, string):
    for seq in possible:
        yield from check_possible(rules, seq, string)


def check(rules, index, string):
    if isinstance(rules[index], list):
        yield from check_expansion(rules, rules[index], string)
    else:
        if string and string[0] == rules[index]:
            yield string[1:]

def does_match(rules, s):
    return any(m == '' for m in check(rules, '0', s))

@timer
def part1(data):
    # print(data)
    rules = data[0]
    test_cases = data[1]
    res = sum(does_match(rules, i) for i in test_cases)
    print(f'part 1: {res}')


@timer
def part2(data):
    rules = data[0]
    # print(data)
    rules = {**rules, '8': [['42'], ['42', '8']], '11': [['42', '31'], ['42', '11', '31']]}
    test_cases = data[1]
    res = sum(does_match(rules, i) for i in test_cases)
    print(f'part 2: {res}')

def parse_data(input_data):
    rule_break = input_data.index('')
    raw_rules = input_data[:rule_break]
    test_strings = input_data[rule_break+1:]
    rules = {}
    for i in raw_rules:
        k, rule = i.split(': ')
        if rule[0] == '"':
            rule = rule[1:-1]
        else:
            rule = [seq.split(' ') if ' ' in seq else [seq]
                for seq in (rule.split(' | ') if ' | ' in rule else [rule])]
        rules[k] = rule
    
    # print(rules)
    return [rules, test_strings]


if __name__ == "__main__":
    # print(input_data)
    parsed_data = parse_data(input_data)
    part1(parsed_data)
    part2(parsed_data)

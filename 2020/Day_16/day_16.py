import os
import sys
import re
from collections import defaultdict
from functools import reduce

sys.path.append('..\AOC')
from Utils.utils import timer

rel_path = "input.txt"
script_dir = os.path.dirname(__file__)
abs_file_path = os.path.join(script_dir, rel_path)
input_data = open(abs_file_path).read().splitlines()


@timer
def part1(data):
    # print(data)
    error_rate = 0
    valid_ranges = data[1]
    other_tickets = data[3]
    for i in other_tickets:
        for j in i:
            if j not in valid_ranges:
                error_rate += j
    print(f'part 1: {error_rate}')


@timer
def part2(data):
    rules = data[0]
    keys = [*data[0].keys()]
    other_tickets = data[3]
    valid_ticket_numbers = data[1]
    ticket_len = len(other_tickets[0])

    valid_tickets = [ticket for ticket in other_tickets if all(v in valid_ticket_numbers for v in ticket)]
    matrix = { i: set(keys[:]) for i in range(ticket_len) }
    cols = [set([row[i] for row in valid_tickets]) for i in range(ticket_len)]
    for i, col in enumerate(cols):
        for rule in rules:
            rules_possible_vals = rules[rule]
            if not col.issubset(rules_possible_vals):
                matrix[i].discard(rule)

    # print(matrix)
    my_ticket = [ int(i) for i in data[2].split(',')]
    my_ticket_parsed = []
    parsed_count = 0
    while parsed_count < ticket_len:
        for i, names in matrix.items():
            if len(names) == 1:
                matrix.pop(i)
                name = next(iter(names))
                for names in matrix.values():
                    names.discard(name)
                my_ticket_parsed.append((name, my_ticket[i]))
                parsed_count += 1
                break
    
    # print(my_ticket_parsed)
    result = reduce((lambda x, y: x * y), [v for k,v in my_ticket_parsed if k.startswith('departure')], 1)
    print(f'part 2: {result}')

def parse_input(data):
    """[summary]
        returns [
            rules  = [ some_rule1: set(), some_rule2: set() ],
            valid ticket numbers: set(all valid ticket numbers),
            my ticket = list(string), 
            other tickets = list(int)
        ]
    """
    my_ticket =  data[data.index("your ticket:") + 1]
    # print(my_ticket)
    ranges = data[:data.index("your ticket:") - 1]
    rules = defaultdict(set)
    r = r'(.*):\s(\d+)-(\d+)\sor\s(\d+)-(\d+)'
    for i in ranges:
        g = re.match(r, i).groups()
        s = set()
        s.update(list(range(int(g[1]),int(g[2])+1)))
        s.update(list(range(int(g[3]),int(g[4])+1)))
        rules[g[0]] = s
 
    # print(rules)
    other_tickets = [ list(map(int, i.split(','))) for i in data[data.index("nearby tickets:") + 1:]]
    
    valid_ticket_numbers = (set.union(*list(rules.values())))
    # print(other_tickets)
    return [rules, valid_ticket_numbers, my_ticket, other_tickets]

if __name__ == "__main__":
    # print(input_data)
    parsed_input = parse_input(input_data)
    part1(parsed_input)
    part2(parsed_input)

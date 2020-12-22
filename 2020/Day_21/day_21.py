from collections import defaultdict
import os
import re
import sys

sys.path.append('..\AOC')
from Utils.utils import timer
rel_path = "input.txt"
script_dir = os.path.dirname(__file__)
abs_file_path = os.path.join(script_dir, rel_path)
input_data = open(abs_file_path).read().splitlines()


def parse_data(data):
    allergen_matches = defaultdict(lambda: [0, set()])
    line_regex = r'(.*)\s\(contains(.*)\)'
    all_ingredients = []
    all_allergens = []
    for line in data:
        g = re.match(line_regex, line).groups()
        ingredients = g[0].split()
        possible_allergens = g[1].split(',')

        all_ingredients.extend(ingredients)
        all_allergens.extend(possible_allergens)

        for a in possible_allergens:
            if a not in allergen_matches:
                allergen_matches[a] = set(ingredients)
            else:
                allergen_matches[a] &= set(ingredients)

    return [all_ingredients, all_allergens, allergen_matches]


@timer
def part1(data):
    all_ingredients = data[0]
    allergen_matches = data[2]
    combined_allergen_matches = set().union(*allergen_matches.values())
    res = sum(
        1 for ingredient in all_ingredients if ingredient not in combined_allergen_matches)
    print(f'part 1: {res}')


@timer
def part2(data):
    allergen_matches = data[2]
    seen = set()
    matched = []
    while True:
        for allergen, food in allergen_matches.items():
            if len(food - seen) == 1:
                t = min(food - seen)
                matched.append((allergen, t))
                seen.add(t)
                break
        else:
            break

    res = ','.join(x[1] for x in sorted(matched))
    print(f'part 2: {res}')


if __name__ == "__main__":
    # print(input_data)
    parsed_data = parse_data(input_data)
    part1(parsed_data)
    part2(parsed_data)

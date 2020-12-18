import os
import sys
import re
import string

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

input_data = []
with open(abs_file_path, 'r') as f:
    for line in f:
        input_data.append(line.rstrip())

def get_passports(input_data):
    input_data.append('')
    passports = []
    temp_passport = {}
    for line in input_data:
        if line == '':
            passports.append(temp_passport)
            temp_passport = {}
        else:  
            fields = line.split(' ')
            for j in fields:
                field = j.split(':')
                temp_passport[field[0]] = field[1]
    return passports

def is_valid_passport1(passport, required_fields):
    if not all (k in passport for k in required_fields):
        return False    
    return True

def is_valid_passport2(passport, required_fields):
    if not all (k in passport for k in required_fields):
        return False    
    
    validations = {
        'byr': (lambda x: len(x) == 4 and 1920 <= int(x) <= 2002),
        'iyr': (lambda x: len(x) == 4 and 2010 <= int(x) <= 2020),
        'eyr': (lambda x: len(x) == 4 and 2020 <= int(x) <= 2030),
        'hgt': (lambda x: (x[-2:] == 'cm' and (150 <= int(x[:-2]) <= 193)) or ( x[-2:]=='in' and (59 <= int(x[:-2]) <= 76))),
        'hcl': (lambda x: bool(re.match(r'#[a-f0-9]{6}', x))),
        'ecl': (lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']),
        'pid': (lambda x: len(x) == 9 and all([i in string.digits for i in x]))
    }

    for k in passport.keys():
        if k in validations:
            ans = validations[k](passport[k])
            if ans == False:
                return False
    
    return True

def count_valid_passports(passports, required_fields, part):
    if part == 1:
        ans = 0
        for passport in passports:
            if(is_valid_passport1(passport, required_fields)):
                ans+=1
        return ans
    elif part == 2:
        ans = 0
        for passport in passports:
            if(is_valid_passport2(passport, required_fields)):
                ans+=1
        return ans


parsed_passports = get_passports(input_data)

valid_passports = count_valid_passports(parsed_passports, ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'], part=1)
print(f'part1: {valid_passports}')

valid_passports2 = count_valid_passports(parsed_passports, ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'], part=2)
print(f'part2: {valid_passports2}')
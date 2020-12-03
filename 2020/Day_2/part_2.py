import os
import sys
import re
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

input_data = []
with open(abs_file_path, 'r') as f:
    for line in f:
        input_data.append(line.rstrip())


def valid_passwords(input_data):
    line_regex = r'(\d+)-(\d+)\s([a-z]):\s([a-z]+)'
    valid_passwords = 0
    for i in input_data:
        groups = re.search(line_regex, i)
        min_count = int(groups[1])
        max_count = int(groups[2])
        char_to_count = groups[3]
        password = groups[4]
        if is_valid_password(char_to_count, min_count, max_count, password):
            valid_passwords += 1
    return valid_passwords

def is_valid_password(char, first_index, last_index, password):
    return (password[first_index-1]==char) != (password[last_index-1] == char)

print(valid_passwords(input_data))
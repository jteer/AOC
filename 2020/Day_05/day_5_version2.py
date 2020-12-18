import os
import sys

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

input_data = []
with open(abs_file_path, 'r') as f:
    for line in f:
        input_data.append(line.rstrip())


def decode(i):
    row = int(i[:7].replace('F', '0').replace('B', '1') ,2 )
    seat = int(i[7:].replace('L', '0').replace('R', '1') ,2 )
    return row,seat

if __name__ == '__main__':
    decoded_boarding_passes = [decode(i) for i in input_data]
    print(decoded_boarding_passes)

    seat_ids = [r * 8 + c for r,c in decoded_boarding_passes]
    print(f'part 1: {max(seat_ids)}')
    
    missing_seat_ids = set(range(min(seat_ids), max(seat_ids))) - set(seat_ids)
    print(f'part 2: {missing_seat_ids}')

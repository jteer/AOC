import os
import sys

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

input_data = []
with open(abs_file_path, 'r') as f:
    for line in f:
        input_data.append(line.rstrip())


def decode_boarding_pass(boarding_pass):
    l, r = 0, 128
    for c in boarding_pass[:7]:
        mid = (l + r) // 2
        if c == 'F':
            r = mid
        elif c == 'B':
            l = mid

    l2, r2 = 0, 8
    for c in boarding_pass[7:]:
        mid = (l2 + r2) // 2
        if c == 'L':
            r2 = mid
        elif c == 'R':
            l2 = mid

    col = l2
    row = l
    seat_id = row * 8 + col
    # print(f'r:{row} c:{col} id:{seat_id}')
    return [row, col, seat_id]


def decode_boarding_passes(boarding_passes):
    decoded = [decode_boarding_pass(i) for i in boarding_passes]
    return decoded


def find_missing_seat(seat_ids):
    seat_ids.sort()
    return [x for x in range(seat_ids[0], seat_ids[-1]+1) if x not in seat_ids]


if __name__ == '__main__':
    decoded_boarding_passes = decode_boarding_passes(input_data)
    # print(decoded_boarding_passes)

    max_seat_id_boardingpass = max(decoded_boarding_passes, key=lambda x: x[2])
    print(f'part1: {max_seat_id_boardingpass[2]}')

    # seat_ids = list(list(zip(*decoded_boarding_passes))[2])
    seat_ids = [row[2] for row in decoded_boarding_passes]
    my_seat = find_missing_seat(seat_ids)
    print(f'part2: {my_seat[0]}')

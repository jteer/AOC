import copy
import os
import sys
from collections import defaultdict
sys.path.append('..\AOC')
from Utils.utils import timer
rel_path = "input.txt"
script_dir = os.path.dirname(__file__)
abs_file_path = os.path.join(script_dir, rel_path)
input_data = open(abs_file_path).read().splitlines()


@timer
def part1(departure_time, bus_ids):
    bus_times = defaultdict(str)
    for bus in bus_ids:
        if bus % departure_time == 0:
            target_bus_id = bus
            break
        else:
            # closest that is greater than departure_time
            bus_times[bus] = (departure_time + bus) - (departure_time % bus)

    target_bus_id = min(bus_times, key=bus_times.get)
    wait_minutes = bus_times[target_bus_id] - departure_time
    print(f'part 1: {target_bus_id * wait_minutes}')


@timer
def part2(bus_ids):
    bus_times = [(i, int(v)) for i, v in enumerate(bus_ids) if v != 'x']
    timestamp, lcm = 0,  1
    for start, step in bus_times:
        while (timestamp + start) % step != 0:
            timestamp += lcm
        lcm *= step
    print(f'part 2: {timestamp}')


if __name__ == "__main__":
    earliest_dep_time = int(input_data[0])
    bus_ids = [i for i in input_data[1].split(',')]
    bus_ids_trimmed = [int(i) for i in input_data[1].split(',') if i != 'x']

    part1(earliest_dep_time, bus_ids_trimmed)
    part2(bus_ids)

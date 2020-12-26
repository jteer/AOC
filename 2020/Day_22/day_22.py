from collections import defaultdict, deque
import os
import re
import sys

sys.path.append('..\AOC')
from Utils.utils import timer
rel_path = "input.txt"
script_dir = os.path.dirname(__file__)
abs_file_path = os.path.join(script_dir, rel_path)

# input_data = open(abs_file_path).read().splitlines()
input_data = open(abs_file_path).read().split("\n\n")

def parse_data(data):
    players = defaultdict(list)
    for line in data:
        player, *cards = line.split('\n')
        players[player] = list(map(int, cards))  
        # print(cards)
    return players

@timer
def part1(data):
    # print(data)
    all_cards = [item for sublist in data.values() for item in sublist]
    player_1, player_2 = map(deque, (data['Player 1:'], data['Player 2:']))

    while player_1 and player_2:
        p1, p2 = player_1.popleft(), player_2.popleft()
        if p1 > p2:
            player_1.extend([p1,p2])
        else:
            player_2.extend([p2,p1])

    winning_player = player_1 or player_2
    t = len(all_cards)
    res = sum(c * (t-i) for i, c in enumerate(winning_player))
    print(f'part 1: {res}')

@timer
def part2(data):
    all_cards = [item for sublist in data.values() for item in sublist]
    player_1, player_2 = map(deque, (data['Player 1:'], data['Player 2:']))
    played_hands = set()

    def play_game(player_1, player_2, game=1):
        player_1, player_2 = map(deque, (player_1, player_2))
        r = 1
        while player_1 and player_2:
            if (sha := hash((tuple(player_1), tuple(player_2), game))) in played_hands:
                return 1, player_1
            else:
                played_hands.add(sha)

            c1, c2 = player_1.popleft(), player_2.popleft()

            if len(player_1) >= c1 and len(player_2) >= c2:
                winner, _ = play_game(list(player_1)[:c1], list(player_2)[:c2], game + 1)
            elif c1 > c2:
                winner = 1
            else:
                winner = 2

            if winner == 1:
                player_1.extend([c1, c2])
            else:
                player_2.extend([c2, c1])

            r += 1
        return 1 if player_1 else 2, player_1 if player_1 else player_2

    winning_player, winning_player_cards = play_game(player_1, player_2, game=1)
    t = len(all_cards)
    winning_score = sum(c * (t-i) for i, c in enumerate(winning_player_cards))
    print(f'part 2: {winning_score}')


if __name__ == "__main__":
    # print(input_data)
    parsed_data = parse_data(input_data)
    part1(parsed_data)
    part2(parsed_data)

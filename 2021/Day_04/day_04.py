import os
import sys
sys.path.append('..\AOC')
from Utils.utils import timer
rel_path = "input.txt"
script_dir = os.path.dirname(__file__)
abs_file_path = os.path.join(script_dir, rel_path)

input_data = []
with open(abs_file_path, 'r') as f:
    for line in f:
        input_data.append(line.rstrip())

def set_x(board,x):
    for i,row in enumerate(board):
        for j,v in enumerate(row):
            if x == v:
                board[i][j] = None

def check_win(board):
    for col in range(5):
      if all([board[col][x] == None for x in range(5)]):
        return True
    for row in range(5):
      if all([board[y][row] == None for y in range(5)]):
        return True
    
def find_score(board):
    # print(list(filter(None, board)))
    # t = sum(map(filter, board))
    s = 0
    for i,_ in enumerate(board):
        for j,_ in enumerate(board):
            if board[i][j] != None:
                s += board[i][j]
    return s

def get_scores(input_data, stop_after=1):
    lines = input_data[:]
    calls = [int(x) for x in lines[0].split(",")]

    boards = []
    for i in range(2, len(lines), 6):
        board = []
        for n in range(5):
            board.append([int(x) for x in lines[i + n].split(" ") if x != ""])
        boards.append(board)

    scores = []
    complete_boards = [False for i in range(len(boards))]
    for call in calls:
        for bn, board in enumerate(boards):
            set_x(board, call)
            if not complete_boards[bn]:
                if(check_win(board)):
                    complete_boards[bn] = True
                    scores.append(find_score(board) * call)
                    if len(scores) == stop_after:
                        return scores
    # print(scores)
    return scores

@timer
def part1(input_data):
    scores = get_scores(input_data, 1)
    return scores[0]
                
@timer
def part2(input_data):
    scores = get_scores(input_data, -1)
    return scores[-1]

# https://adventofcode.com/2021/day/4
if __name__ == "__main__":
    print(part1(input_data))
    print(part2(input_data))
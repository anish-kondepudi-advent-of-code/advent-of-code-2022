from enum import Enum

class Move(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

class Decision(Enum):
    LOSE = 1
    DRAW = 2
    WIN = 3

move_map = {
    "A": Move.ROCK,
    "B": Move.PAPER,
    "C": Move.SCISSORS,
    "X": Move.ROCK,
    "Y": Move.PAPER,
    "Z": Move.SCISSORS
}

decision_map = {
    "X": Decision.LOSE,
    "Y": Decision.DRAW,
    "Z": Decision.WIN
}

winning_move_map = {
    Move.ROCK: Move.SCISSORS,
    Move.PAPER: Move.ROCK,
    Move.SCISSORS: Move.PAPER
}

losing_move_map = dict((v, k) for k, v in winning_move_map.items())

def solve_part_1(lines):
    moves = [(move_map[x], move_map[y]) for x, y in lines]

    totalScore = 0
    for opponent_move, my_move in moves:

        if losing_move_map[my_move] == opponent_move:
            totalScore += my_move.value
        elif winning_move_map[my_move] == opponent_move:
            totalScore += 6 + my_move.value
        else:
            totalScore += 3 + my_move.value

    return totalScore

def solve_part_2(lines):
    moves = [(move_map[x], decision_map[y]) for x, y in lines]

    totalScore = 0
    for opponent_move, my_move in moves:

        if my_move == Decision.WIN:
            totalScore += 6 + losing_move_map[opponent_move].value
        if my_move == Decision.DRAW:
            totalScore += 3 + opponent_move.value
        if my_move == Decision.LOSE:
            totalScore += winning_move_map[opponent_move].value

    return totalScore

with open("input.txt") as file:
    lines = [line.rstrip().split() for line in file]

    print(solve_part_1(lines))
    print(solve_part_2(lines))
# https://adventofcode.com/2022/day/2

from enum import Enum
from get_input import get_input

games = get_input("https://adventofcode.com/2022/day/2/input")


class Option(Enum):
    ROCK = "A"
    PAPER = "B"
    SCISSORS = "C"


class ResponseOption(Enum):
    ROCK = "X"
    PAPER = "Y"
    SCISSORS = "Z"


class Score(Enum):
    WIN = 6
    DRAW = 3
    LOOSE = 0


rock_results = {
    ResponseOption.PAPER.value: Score.WIN.value,
    ResponseOption.ROCK.value: Score.DRAW.value,
    ResponseOption.SCISSORS.value: Score.LOOSE.value,
}

paper_results = {
    ResponseOption.SCISSORS.value: Score.WIN.value,
    ResponseOption.PAPER.value: Score.DRAW.value,
    ResponseOption.ROCK.value: Score.LOOSE.value
}

scissors_results = {
    ResponseOption.PAPER.value: Score.LOOSE.value,
    ResponseOption.SCISSORS.value: Score.DRAW.value,
    ResponseOption.ROCK.value: Score.WIN.value,
}

response = {
    Option.ROCK.value: rock_results,
    Option.PAPER.value: paper_results,
    Option.SCISSORS.value: scissors_results
}

option_score = {
    ResponseOption.ROCK.value: 1,
    ResponseOption.PAPER.value: 2,
    ResponseOption.SCISSORS.value: 3
}


def calculate_response_result(option_value, response_value):
    return response[option_value][response_value] + option_score[response_value]

sum = 0

for game in games:
    options = game.split(" ")

    if (options[0] == ""):
        break

    sum = sum + calculate_response_result(options[0], options[1])

print(sum)

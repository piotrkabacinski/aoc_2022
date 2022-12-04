# https://adventofcode.com/2022/day/2

from enum import Enum
from get_input import get_input

games = get_input("https://adventofcode.com/2022/day/2/input")


class Option(Enum):
    A = 0  # Rock
    B = 1  # Paper
    C = 2  # Scissors


class ResponseOption(Enum):
    X = 0  # Rock
    Y = 1  # Paper
    Z = 2  # Scissors


class Score(Enum):
    WIN = 6
    DRAW = 3
    LOOSE = 0


response_option_results = (
    (Score.DRAW.value, Score.WIN.value, Score.LOOSE.value),  # Rock
    (Score.LOOSE.value, Score.DRAW.value, Score.WIN.value),  # Paper
    (Score.WIN.value, Score.LOOSE.value, Score.DRAW.value) # Scissors
)

option_scores = (1, 2, 3)


def calculate_response_result(option_value, response_value):
    player_1_option_index = Option[option_value].value
    player_2_option_index = ResponseOption[response_value].value

    return response_option_results[player_1_option_index][player_2_option_index] + option_scores[player_2_option_index]


sum = 0

for game in games:
    options = game.split(" ")

    if (options[0] == ""):
        break

    sum = sum + calculate_response_result(options[0], options[1])

print(sum)

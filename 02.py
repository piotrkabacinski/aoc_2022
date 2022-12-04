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


# Rock, Paper, Scissors
option_scores = (1, 2, 3)

response_option_results = (
    # Rock, Paper, Scissors vs...
    (Score.DRAW.value, Score.WIN.value, Score.LOOSE.value),  # Rock
    (Score.LOOSE.value, Score.DRAW.value, Score.WIN.value),  # Paper
    (Score.WIN.value, Score.LOOSE.value, Score.DRAW.value)  # Scissors
)


strategy_response_option = [
    # Loose, Draw, Win
    (option_scores[2], option_scores[0], option_scores[1]),  # Rock
    (option_scores[0], option_scores[1], option_scores[2]),  # Paper
    (option_scores[1], option_scores[2], option_scores[0])  # Scissors
]


def calculate_response_result(player_1_option_index, player_2_option_index):
    return response_option_results[player_1_option_index][player_2_option_index] + option_scores[player_2_option_index]


def calculate_strategy_response_result(player_1_option_index, player_2_option_index):
    return strategy_response_option[player_1_option_index][player_2_option_index] + [Score.LOOSE.value, Score.DRAW.value, Score.WIN.value][player_2_option_index]


sum = 0
secret_strategy_sum = 0

for game in games:
    if game == "":
        break

    options = game.split(" ")

    player_1_option_index = Option[options[0]].value
    player_2_option_index = ResponseOption[options[1]].value

    sum = sum + \
        calculate_response_result(player_1_option_index, player_2_option_index)

    secret_strategy_sum = secret_strategy_sum + \
        calculate_strategy_response_result(
            player_1_option_index, player_2_option_index)

print("Sum:", sum)
print("Secret strategy sum:", secret_strategy_sum)

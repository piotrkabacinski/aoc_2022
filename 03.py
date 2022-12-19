# https://adventofcode.com/2022/day/3

from get_input import get_input
from enum import Enum

pairs = get_input("https://adventofcode.com/2022/day/3/input")


class CharSubsract(Enum):
    UPPER_CASE = 96
    LOWER_CASE = 38


def is_occuring(character, rucksack):
    for item in rucksack:
        if item == character:
            return True

    return False


checked_characters = []
sum = 0

for pair in pairs:
    if pair == "":
        break

    items_count = int(len(pair) / 2)

    first = pair[0:items_count]
    second = pair[items_count * -1:]

    for index in range(int(len(first))):
        character = first[index]

        if not character in checked_characters:
            checked_characters.append(character)

            if is_occuring(character, second):
                value = ord(
                    character) - CharSubsract.UPPER_CASE.value if character.isupper() else ord(character) - CharSubsract.LOWER_CASE.value
                sum = sum + value

    checked_characters.clear()

print(sum)  # 8153

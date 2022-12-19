# https://adventofcode.com/2022/day/3

from functools import reduce
from get_input import get_input

pairs = get_input("https://adventofcode.com/2022/day/3/input")


def sum_similar_values(group):
    dict = {}

    for character in group[0]:
        dict[character] = [0, 0]

    for index in range(1, 3):
        for character in group[index]:
            if character in dict and dict[character][index - 1] != 1:
                dict[character][index - 1] = 1

    similars = []

    for item in dict.items():
        if reduce(lambda a, b: a + b, item[1]) == 2:
            similars.append(item[0])

    sum = 0

    for character in similars:
        value = ord(
            character) - 38 if character.isupper() else ord(character) - 96
        sum = sum + value

    return sum


group = []
sum = 0

for pair in pairs:
    group.append(pair)

    if len(group) == 3:
        sum = sum + sum_similar_values(group)
        group.clear()

print(sum)  # 2342

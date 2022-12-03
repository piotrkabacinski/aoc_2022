# https://adventofcode.com/2022/day/1

from get_input import get_input

calories = get_input("https://adventofcode.com/2022/day/1/input")

highest_calories = 0

current_sum = 0

for calory in calories:
    if calory == "":
        if current_sum > highest_calories:
            highest_calories = current_sum

        current_sum = 0
    else:
        current_sum = current_sum + int(calory)

print(highest_calories)

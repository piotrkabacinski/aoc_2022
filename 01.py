# https://adventofcode.com/2022/day/1

from functools import reduce
from get_input import get_input

calories = get_input("https://adventofcode.com/2022/day/1/input")

top_3_sums = [0, 0, 0]

for calory in calories:
    if calory == "":
        if current_sum > top_3_sums[2]:
            for i in range(3):
                if current_sum > top_3_sums[i]:
                    top_3_sums.insert(i, current_sum)
                    top_3_sums.pop(3)
                    break

        current_sum = 0
    else:
        current_sum = current_sum + int(calory)


print("Top value:", top_3_sums[0]) # 70369
print("Top 3 sum:", reduce(lambda a, b: a + b, top_3_sums)) # 203002

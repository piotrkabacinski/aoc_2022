# https://adventofcode.com/2022/day/1

from get_input import get_input

calories = get_input("https://adventofcode.com/2022/day/1/input")

current_sum = 0

top_3_sums = [0, 0, 0]

for calory in calories:
    if calory == "":
        if current_sum > top_3_sums[0]:
            for i in reversed(range(3)):
                if current_sum > top_3_sums[i]:
                    top_3_sums.insert(i + 1, current_sum)
                    top_3_sums.pop(0)
                    break

        current_sum = 0
    else:
        current_sum = current_sum + int(calory)

sum = 0

for i in range(3):
    sum = sum + top_3_sums[i]

print(sum)  # 203002

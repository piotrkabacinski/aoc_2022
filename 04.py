# https://adventofcode.com/2022/day/4

from get_input import get_input

pairs = get_input("https://adventofcode.com/2022/day/4/input")

subset_count = 0
overlap_count = 0


def parse_scope(input):
    return list(map(lambda v: int(v), input.split("-")))


for pair in pairs:
    if pair == "":
        break

    assignments = pair.split(",")

    scope_1 = parse_scope(assignments[0])
    scope_2 = parse_scope(assignments[1])

    if scope_1[0] >= scope_2[0] and scope_1[1] <= scope_2[1]:
        subset_count = subset_count + 1
    elif scope_2[0] >= scope_1[0] and scope_2[1] <= scope_1[1]:
        subset_count = subset_count + 1

    if (
        (scope_1[0] >= scope_2[0] and scope_1[1] <= scope_2[1])
        or (scope_2[0] >= scope_1[0] and scope_2[1] <= scope_1[1])
        or (
            scope_1[0] >= scope_2[0]
            and scope_1[0] <= scope_2[1]
            and scope_1[1] > scope_2[1]
        )
        or (scope_1[1] <= scope_2[1] and scope_1[1] >= scope_2[0])
    ):
        overlap_count = overlap_count + 1


print(subset_count)  # 518
print(overlap_count)  # 909

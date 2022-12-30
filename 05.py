# https://adventofcode.com/2022/day/4

from re import findall
from get_input import get_input


input = get_input("https://adventofcode.com/2022/day/5/input")


def parse_stack(lines):
    stacks_amount = int(findall("[0-9]+", lines[len(lines) - 1]).pop())

    stack = []

    for index in range(0, len(lines) - 1):
        characters = [*lines[index]]

        for id in range(0, stacks_amount):
            start = id * 4
            offset = start + 4

            crate = characters[start:offset][1]

            if len(stack) - 1 < id:
                stack.append([])

            if crate == " ":
                continue
            else:
                stack[id].append(crate)

    return stack


parsed_stack = None

for index, line in enumerate(input):
    if line == "":
        parsed_stack = parse_stack(input[0:index])

        for command in input[index + 1:]:
            if command == "":
                break

            print(command)

        break

# https://adventofcode.com/2022/day/4

from re import findall
from get_input import get_input


input = get_input("https://adventofcode.com/2022/day/5/input")


def parse_stack(lines):
    stacks_amount = int(findall("[0-9]+", lines[len(lines) - 1]).pop())

    stack = []

    for index in range(0, len(lines) - 1):
        characters = [*lines[index]]

        step = 4

        for id in range(0, stacks_amount):
            start = id * step
            offset = start + step

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

            tokens = command.split(" ")

            amount = int(tokens[1])
            source_index = int(tokens[3]) - 1
            target_index = int(tokens[5]) - 1

            crates = parsed_stack[source_index][0:amount]
            # Comment out for part 2 solution:
            crates.reverse()

            parsed_stack[target_index] = crates + parsed_stack[target_index]

            del parsed_stack[source_index][0:amount]

        break

print("".join(list(map(lambda a: a[0], parsed_stack))))  # TLFGBZHCN, QRQFHFWCL

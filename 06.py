# https://adventofcode.com/2022/day/6


from enum import Enum
from get_input import get_input


stream = get_input("https://adventofcode.com/2022/day/6/input")[0]

characters = enumerate([*stream])


class CharacterAmount(Enum):
    START_OF_PACKET = 4
    START_OF_MESSAGE = 14


amount = CharacterAmount.START_OF_PACKET.value

for index, _ in characters:
    sequence = stream[index:index + amount]

    if (len(set(sequence)) == amount):
        print(index + amount)  # 1766, 2383
        break

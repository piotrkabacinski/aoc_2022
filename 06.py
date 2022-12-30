# https://adventofcode.com/2022/day/6


from enum import Enum
from get_input import get_input


stream = get_input("https://adventofcode.com/2022/day/6/input")[0]


class CharacterAmount(Enum):
    START_OF_PACKET = 4
    START_OF_MESSAGE = 14


packet_start_index = 0

for index, _ in enumerate([*stream]):
    sequence = stream[index:index + CharacterAmount.START_OF_PACKET.value]

    if (len(set(sequence)) == CharacterAmount.START_OF_PACKET.value):
        packet_start_index = index

        print(packet_start_index + CharacterAmount.START_OF_PACKET.value)  # 1766
        break


for index in range(packet_start_index + CharacterAmount.START_OF_PACKET.value, len([*stream])):
    sequence = stream[index:index + CharacterAmount.START_OF_MESSAGE.value]

    if (len(set(sequence)) == CharacterAmount.START_OF_MESSAGE.value):
        print(index + CharacterAmount.START_OF_MESSAGE.value)  # 2383
        break

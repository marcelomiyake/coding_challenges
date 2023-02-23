import math


def binary_search(array: list, target: int) -> int:
    pointer = len(array) // 2
    tries = math.ceil(math.log2(len(array)))
    half = pointer

    while array[pointer] != target:
        half = half // 2 if half // 2 > 0 else 1

        if half == 0:
            return -1

        if array[pointer] < target:
            pointer += half
        else:
            pointer -= half
        tries -= 1
        if tries < 0 or pointer < 0 or pointer >= len(array):
            return -1

    return pointer

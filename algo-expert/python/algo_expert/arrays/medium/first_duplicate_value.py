def first_duplicate_value(array: list) -> int:
    first = -1
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            if array[i] == array[j]:
                if first < 0 or j < first:
                    first = j
    return first if first < 0 else array[first]

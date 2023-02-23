def find_three_largest_numbers(array: list) -> list:
    largest = []

    for n in array:
        length = len(largest)

        if length == 3 and n > largest[2]:
            largest.append(n)
        elif length >= 2 and n > largest[1]:
            largest.insert(2, n)
        elif length >= 1 and n > largest[0]:
            largest.insert(1, n)
        elif length >= 0:
            largest.insert(0, n)
        if len(largest) > 3:
            del largest[0]

    return largest

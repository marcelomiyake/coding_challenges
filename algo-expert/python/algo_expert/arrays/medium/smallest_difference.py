def smallest_difference(array_one: list, array_two: list) -> list:
    sorted_one = sorted(array_one)
    sorted_two = sorted(array_two)
    pointer_one = 0
    pointer_two = 0
    len_one = len(sorted_one)
    len_two = len(sorted_two)

    differences = {}
    while pointer_one < len_one and pointer_two < len_two:
        if sorted_one[pointer_one] == sorted_two[pointer_two]:
            return [sorted_one[pointer_one], sorted_two[pointer_two]]
        elif sorted_one[pointer_one] < sorted_two[pointer_two]:
            pointer_one += 1
        else:
            pointer_two += 1
        if pointer_one < len_one and pointer_two < len_two:
            differences[(sorted_one[pointer_one], sorted_two[pointer_two])] = abs(
                sorted_one[pointer_one] - sorted_two[pointer_two])
    return list(min(differences, key=differences.get))

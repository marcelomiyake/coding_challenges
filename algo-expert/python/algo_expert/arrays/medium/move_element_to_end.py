def move_element_to_end(array: list, to_move: int) -> list:
    inserts = 0
    i = len(array) - 1
    while i >= 0:
        if i == inserts:
            break
        if array[i] != to_move:
            element = array[i]
            del array[i]
            array.insert(0, element)
            inserts += 1
        else:
            i -= 1
    return array

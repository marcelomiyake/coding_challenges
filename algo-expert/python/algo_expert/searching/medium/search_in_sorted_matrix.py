def search_in_sorted_matrix(matrix: list, target: int) -> list:
    max_y = len(matrix) - 1
    max_x = len(matrix[0]) - 1
    for y in list(reversed(range(len(matrix)))):
        if matrix[y][0] == target:
            return [y, 0]
        elif matrix[y][0] < target:
            max_y = y
            break
    for x in list(reversed(range(len(matrix[0])))):
        if matrix[0][x] == target:
            return [0, x]
        if matrix[0][x] < target:
            max_x = x
            break
    for y in list(reversed(range(max_y + 1))):
        for x in list(reversed(range(max_x + 1))):
            if matrix[y][x] == target:
                return [y, x]
            elif matrix[y][x] < target:
                break

    return [-1, -1]

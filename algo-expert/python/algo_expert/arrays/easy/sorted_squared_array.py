def sorted_squared_array(array: list) -> list:
    return sorted(list(map(lambda x: pow(x, 2), array)))

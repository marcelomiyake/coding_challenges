from functools import reduce


def array_of_products(array: list) -> list:
    result = []
    for i in range(len(array)):
        value = array.pop(i)
        result.append(reduce(lambda a, b: a * b, array))
        array.insert(i, value)
    return result

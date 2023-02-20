def is_monotonic(array: list) -> bool:
    len_array = len(array)
    if len_array <= 1:
        return True
    direction = array[len_array - 1] >= array[0]
    for i in range(1, len_array):
        if direction and array[i] < array[i - 1] or not direction and array[i] > array[i - 1]:
            return False
    return True

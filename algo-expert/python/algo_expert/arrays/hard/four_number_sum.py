def four_number_sum(array: list, target_sum: int) -> list:
    result = []
    len_array = len(array)
    if len_array < 4:
        return result
    for i in range(len_array - 3):
        for j in range(i + 1, len_array - 2):
            for k in range(j + 1, len_array - 1):
                for l in range(k + 1, len_array):
                    if array[i] + array[j] + array[k] + array[l] == target_sum:
                        result.append([array[i], array[j], array[k], array[l]])
    return result

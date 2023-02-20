def three_number_sum(array: list, target_sum: list) -> int:
    result = []
    sorted_array = sorted(array)
    len_array = len(sorted_array)
    for i in range(len_array - 2):
        for j in range(i + 1, len_array - 1):
            for k in range(j + 1, len_array):
                if sorted_array[i] + sorted_array[j] + sorted_array[k] == target_sum:
                    result.append([sorted_array[i], sorted_array[j], sorted_array[k]])
    return result

def two_number_sum(array: list, target_sum: int):
    complement = {}
    for i in range(len(array)):
        if target_sum - array[i] in complement:
            return [array[i], target_sum - array[i]]
        complement[array[i]] = target_sum - array[i]
    return []

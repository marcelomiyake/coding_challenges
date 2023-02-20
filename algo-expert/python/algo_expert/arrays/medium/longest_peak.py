def longest_peak(array: list) -> int:
    increase_peak = 1
    decrease_peak = 0
    highest_peak = 0

    for i in range(1, len(array)):
        if array[i] > array[i - 1]:
            if decrease_peak > 0:
                increase_peak = 2
                decrease_peak = 0
            else:
                increase_peak += 1
        elif array[i] < array[i - 1] and increase_peak > 1:
            decrease_peak += 1
        else:
            decrease_peak = 0
            increase_peak = 1
        if decrease_peak > 0:
            if increase_peak + decrease_peak > highest_peak:
                highest_peak = increase_peak + decrease_peak

    return highest_peak


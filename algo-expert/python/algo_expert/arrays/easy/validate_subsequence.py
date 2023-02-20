def isValidSubsequence(array: list, sequence: list):
    if len(sequence) > len(array):
        return False

    i = 0
    for num in sequence:
        while i < len(array) and array[i] != num:
            i += 1
        if i >= len(array):
            return False
        i += 1
    return True

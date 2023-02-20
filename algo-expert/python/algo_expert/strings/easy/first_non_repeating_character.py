def first_non_repeating_character(string: str) -> int:
    for i, _ in enumerate(string):
        if string.count(string[i]) > 1:
            continue
        return i
    return -1

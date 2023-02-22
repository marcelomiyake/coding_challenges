def one_edit(string_one: str, string_two: str) -> bool:
    string_one_size = len(string_one)
    string_two_size = len(string_two)

    editions = 0
    idx_one = 0
    idx_two = 0
    while idx_one < string_one_size or idx_two < string_two_size:
        if idx_one >= string_one_size or idx_two >= string_two_size or string_one[idx_one] != string_two[idx_two]:
            editions += 1
            if editions > 1:
                return False

            if string_one_size > string_two_size:
                idx_one += 1
                continue
            elif string_one_size < string_two_size:
                idx_two += 1
                continue
        idx_one += 1
        idx_two += 1

    return True

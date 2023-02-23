def longest_substring_without_duplication(string: str) -> str:
    if len(string) <= 1:
        return string

    longest = ""
    for i in range(len(string) - 1):
        for j in range(i + 1, len(string) + 1):
            if j - i > len(longest) and not has_duplication(string[i:j]):
                longest = string[i:j]
    return longest


def has_duplication(string: str) -> bool:
    for i in range(len(string) - 1):
        for j in range(i + 1, len(string)):
            if string[i] == string[j]:
                return True
    return False

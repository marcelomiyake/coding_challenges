def longest_palindromic_substring(string: str) -> str:
    max_size = 1
    longest = ""
    if len(string) == 1:
        return string
    for i in range(len(string) - 1):
        j = 0
        if string[i] == string[i + 1]:
            j = i + 1
            while j + 1 < len(string) and string[i] == string[j + 1]:
                j += 1
        elif i + 2 < len(string) and string[i] == string[i + 2]:
            j = i + 2
        if j > 0:
            size = 1
            while i - size >= 0 and j + size < len(string) and string[i - size] == string[j + size]:
                size += 1
            palindrome_size = 2 * size + j - i - 1
            if palindrome_size > max_size:
                max_size = palindrome_size
                longest = string[i - size + 1:j + size]
    return longest

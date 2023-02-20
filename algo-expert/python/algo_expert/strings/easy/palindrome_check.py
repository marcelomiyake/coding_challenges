def is_palindrome(string):
    len_string = len(string)
    for i in range(len_string // 2):
        if string[i] != string[len_string - i - 1]:
            return False
    return True

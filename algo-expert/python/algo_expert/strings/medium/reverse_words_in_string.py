def reverse_words_in_string(string: str) -> str:
    result = []
    word = []
    for i in range(1, len(string) + 1):
        if string[-i] == " ":
            if len(word) > 0:
                result += word
                word = []
            result.append(string[-i])
        else:
            word.insert(0, string[-i])
    if len(word) > 0:
        result += word
    return ''.join(result)

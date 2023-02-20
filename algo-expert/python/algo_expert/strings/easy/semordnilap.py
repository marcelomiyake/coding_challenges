def semordnilap(words: list) -> list:
    result = []
    for i in range(len(words) - 1):
        palindrome = words[i][::-1]
        for j in range(i + 1, len(words)):
            if palindrome == words[j]:
                result.append([words[i], words[j]])
    return result

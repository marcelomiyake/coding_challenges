from collections import defaultdict


def minimum_characters_for_words(words: list) -> list:
    letters = defaultdict(int)

    for word in words:
        word_letters = defaultdict(int)
        for c in word:
            word_letters[c] += 1
            if letters[c] < word_letters[c]:
                letters[c] = word_letters[c]

    result = []
    for letter, quantity in letters.items():
        for _ in range(quantity):
            result.append(letter)
    return result

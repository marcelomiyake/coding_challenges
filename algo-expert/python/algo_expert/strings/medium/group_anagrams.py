def group_anagrams(words: list) -> list:
    ordered = set(map(lambda word: "".join(sorted(word)), words))
    result = []
    for o in ordered:
        item = []
        for w in words:
            if o == "".join(sorted(w)):
                item.append(w)
        result.append(item)
    return result

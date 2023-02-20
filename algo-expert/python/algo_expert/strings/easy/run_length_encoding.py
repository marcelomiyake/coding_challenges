def run_length_encoding(string: str) -> str:
    encoded = []
    character = ""
    counter = 0
    for c in string:
        if c != character or counter == 9:
            if counter > 0:
                encoded.append(f"{counter}{character}")
            character = c
            counter = 1
        else:
            counter += 1
    encoded.append(f"{counter}{character}")
    return "".join(encoded)

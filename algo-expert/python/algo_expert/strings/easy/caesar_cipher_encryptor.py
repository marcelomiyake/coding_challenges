def caesar_cipher_encryptor(string: list, key: int) -> str:
    crypt_string = []
    for c in string:
        c_shifted = ord(c) + key
        while c_shifted > ord("z"):
            c_shifted -= ord("z") - ord("a") + 1
        crypt_string.append(chr(c_shifted))
    return ''.join(crypt_string)

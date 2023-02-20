from algo_expert.strings.easy.caesar_cipher_encryptor import caesar_cipher_encryptor


class TestCaesarCipherEncryptor:
    def test_case_0(self):
        string = "xyz"
        key = 2

        expected = "zab"

        assert caesar_cipher_encryptor(string, key) == expected

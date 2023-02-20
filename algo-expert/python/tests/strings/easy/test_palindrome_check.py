from algo_expert.strings.easy.palindrome_check import is_palindrome


class TestPalindromeCheck:
    def test_case_0(self):
        string = "abcdcba"

        expected = True

        assert is_palindrome(string) == expected

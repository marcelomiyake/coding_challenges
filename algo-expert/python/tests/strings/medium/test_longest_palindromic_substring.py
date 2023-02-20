from algo_expert.strings.medium.longest_palindromic_substring import longest_palindromic_substring


class TestLongestPalindromicSubstring:
    def test_case_0(self):
        string = "abaxyzzyxf"

        expected = "xyzzyx"

        assert longest_palindromic_substring(string) == expected

    def test_case_6(self):
        string = "abcdefgfedcbazzzzzzzzzzzzzzzzzzzz"

        expected = "zzzzzzzzzzzzzzzzzzzz"

        assert longest_palindromic_substring(string) == expected

    def test_case_12(self):
        string = "z234a5abbba54a32z"

        expected = "5abbba5"

        assert longest_palindromic_substring(string) == expected

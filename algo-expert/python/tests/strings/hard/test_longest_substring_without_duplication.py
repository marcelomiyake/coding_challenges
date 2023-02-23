from algo_expert.strings.hard.longest_substring_without_duplication import longest_substring_without_duplication


class TestLongestSubstringWithoutDuplication:
    def test_case_0(self):
        string = "clementisacap"

        expected = "mentisac"

        assert longest_substring_without_duplication(string) == expected

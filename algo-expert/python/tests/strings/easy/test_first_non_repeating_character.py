from algo_expert.strings.easy.first_non_repeating_character import first_non_repeating_character


class TestFirstNonRepeatingCharacter:
    def test_case_0(self):
        string = "abcdcaf"

        expected = 1

        assert first_non_repeating_character(string) == expected

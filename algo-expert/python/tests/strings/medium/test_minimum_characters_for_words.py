from algo_expert.strings.medium.minimum_characters_for_words import minimum_characters_for_words


class TestMinimumCharactersForWords:
    def test_case_0(self):
        words = ["this", "that", "did", "deed", "them!", "a"]

        expected = ["t", "t", "h", "i", "s", "a", "d", "d", "e", "e", "m", "!"]

        assert minimum_characters_for_words(words) == expected

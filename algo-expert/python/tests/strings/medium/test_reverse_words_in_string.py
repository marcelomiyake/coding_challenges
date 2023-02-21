from algo_expert.strings.medium.reverse_words_in_string import reverse_words_in_string


class TestReverseWordsInString:
    def test_case_0(self):
        string = "AlgoExpert is the best!"

        expected = "best! the is AlgoExpert"

        assert reverse_words_in_string(string) == expected

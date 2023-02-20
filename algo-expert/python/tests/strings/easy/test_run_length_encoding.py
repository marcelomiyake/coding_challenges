from algo_expert.strings.easy.run_length_encoding import run_length_encoding


class TestRunLengthEncoding:
    def test_case_0(self):
        string = "AAAAAAAAAAAAABBCCCCDD"

        expected = "9A4A2B4C2D"

        assert run_length_encoding(string) == expected

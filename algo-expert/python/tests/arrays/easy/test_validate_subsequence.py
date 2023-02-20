from algo_expert.arrays.easy.validate_subsequence import isValidSubsequence


class TestValidateSubsequence:
    def test_case_0(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [1, 6, -1, 10]

        expected = True

        assert isValidSubsequence(array, sequence) == expected

    def test_case_10(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10],
        sequence = [5, 1, 22, 25, 6, -1, 8, 10, 12]

        expected = False

        assert isValidSubsequence(array, sequence) == expected

    def test_case_12(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10],
        sequence = [5, 1, 22, 23, 6, -1, 8, 10]

        expected = False

        assert isValidSubsequence(array, sequence) == expected

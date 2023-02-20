from algo_expert.arrays.medium.first_duplicate_value import first_duplicate_value


class TestFirstDuplicateValue:
    def test_case_0(self):
        array = [2, 1, 5, 2, 3, 3, 4]

        expected = 2

        assert first_duplicate_value(array) == expected

    def test_case_11(self):
        array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        expected = -1

        assert first_duplicate_value(array) == expected

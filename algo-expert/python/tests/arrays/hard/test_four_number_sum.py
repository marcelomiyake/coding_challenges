from algo_expert.arrays.hard.four_number_sum import four_number_sum


class TestFourNumberSum:
    def test_case_0(self):
        array = [7, 6, 4, -1, 1, 2]
        target_sum = 16

        expected = [
            [7, 6, 4, -1],
            [7, 6, 1, 2]
        ]

        assert four_number_sum(array, target_sum) == expected

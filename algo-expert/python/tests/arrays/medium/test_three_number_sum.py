from algo_expert.arrays.medium.three_number_sum import three_number_sum


class TestThreeNumberSum:

    def test_case_0(self):
        array = [12, 3, 1, 2, -6, 5, -8, 6]
        target_sum = 0

        expected = [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]

        assert three_number_sum(array, target_sum) == expected

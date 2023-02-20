from algo_expert.arrays.easy.two_number_sum import two_number_sum


class TestTwoNumberSum:
    def test_case_0(self):
        array = [3, 5, -4, 8, 11, 1, -1, 6]
        target_sum = 10

        expected = [-1, 11]

        assert two_number_sum(array, target_sum) == expected

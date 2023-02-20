from algo_expert.arrays.medium.zero_sum_subarray import zero_sum_subarray


class TestZeroSumSubarray:
    def test_case_0(self):
        nums = [-5, -5, 2, 3, -2]

        expected = True

        assert zero_sum_subarray(nums) == expected

    def test_case_9(self):
        nums = [-2, 2]

        expected = True

        assert zero_sum_subarray(nums) == expected

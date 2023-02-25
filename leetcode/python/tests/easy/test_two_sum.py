from src.easy.two_sum import Solution


class TestTwoSum:
    def test_case_1(self):
        nums = [2, 7, 11, 15]
        target = 9

        expected = [0, 1]

        assert sorted(Solution().twoSum(nums, target)) == sorted(expected)

    def test_case_2(self):
        nums = [3, 2, 4]
        target = 6

        expected = [1, 2]

        assert sorted(Solution().twoSum(nums, target)) == sorted(expected)

    def test_case_3(self):
        nums = [3, 3]
        target = 6

        expected = [0, 1]

        assert sorted(Solution().twoSum(nums, target)) == sorted(expected)

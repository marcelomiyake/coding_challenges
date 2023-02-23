from algo_expert.searching.easy.find_three_largest_numbers import find_three_largest_numbers


class TestFindThreeLargestNumbers:
    def test_case_0(self):
        array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]

        expected = [18, 141, 541]

        assert find_three_largest_numbers(array) == expected

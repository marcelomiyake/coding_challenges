from algo_expert.arrays.medium.smallest_difference import smallest_difference


class TestSmallestDifference:
    def test_case_0(self):
        array_one = [-1, 5, 10, 20, 28, 3]
        array_two = [26, 134, 135, 15, 17]

        expected = [28, 26]

        assert smallest_difference(array_one, array_two) == expected

from algo_expert.arrays.easy.sorted_squared_array import sorted_squared_array


class TestSortedSquaredArray:
    def test_case_0(self):
        array = [1, 2, 3, 5, 6, 8, 9]

        expected = [1, 4, 9, 25, 36, 64, 81]

        assert sorted_squared_array(array) == expected

    def test_case_8(self):
        array = [-2, -1]

        expected = [1, 4]

        assert sorted_squared_array(array) == expected

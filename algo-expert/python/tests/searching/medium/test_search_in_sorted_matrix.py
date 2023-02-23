from algo_expert.searching.medium.search_in_sorted_matrix import search_in_sorted_matrix


class TestSearchInSortedMatrix:
    def test_case_0(self):
        matrix = [
            [1, 4, 7, 12, 15, 1000],
            [2, 5, 19, 31, 32, 1001],
            [3, 8, 24, 33, 35, 1002],
            [40, 41, 42, 44, 45, 1003],
            [99, 100, 103, 106, 128, 1004]
        ]
        target = 44

        expected = [3, 3]

        assert search_in_sorted_matrix(matrix, target) == expected

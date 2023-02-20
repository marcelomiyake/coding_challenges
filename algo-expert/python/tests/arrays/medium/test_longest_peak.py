from algo_expert.arrays.medium.longest_peak import longest_peak


class TestLongestPeak:
    def test_case_0(self):
        array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]

        expected = 6

        assert longest_peak(array) == expected

    def test_case_3(self):
        array = [1, 3, 2]

        expected = 3

        assert longest_peak(array) == expected

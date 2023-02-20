from algo_expert.arrays.medium.monotonic_array import is_monotonic


class TestMonotonicArray:
    def test_case_0(self):
        array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]

        expected = True

        assert is_monotonic(array) == expected

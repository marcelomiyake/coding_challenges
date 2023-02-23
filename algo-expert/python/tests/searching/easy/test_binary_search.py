from algo_expert.searching.easy.binary_search import binary_search


class TestBinarySearch:
    def test_case_0(self):
        array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
        target = 33

        expected = 3

        assert binary_search(array, target) == expected

    def test_case_5(self):
        array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
        target = 0

        expected = 0

        assert binary_search(array, target) == expected

    def test_case_11(self):
        array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
        target = 72

        expected = 8

        assert binary_search(array, target) == expected

    def test_case_12(self):
        array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
        target = 73

        expected = 9

        assert binary_search(array, target) == expected

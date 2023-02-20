from algo_expert.arrays.medium.array_of_products import array_of_products


class TestArrayOfProducts:
    def test_case_0(self):
        array = [5, 1, 4, 2]

        expected = [8, 40, 10, 20]

        assert array_of_products(array) == expected

    def test_case_3(self):
        array = [-5, 2, -4, 14, -6]

        expected = [672, -1680, 840, -240, 560]

        assert array_of_products(array) == expected

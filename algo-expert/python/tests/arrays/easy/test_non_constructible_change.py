from algo_expert.arrays.easy.non_constructible_change import non_constructible_change


class TestNonConstructibleChange:
    def test_case_0(self):
        coins = [5, 7, 1, 1, 2, 3, 22]

        expected = 20

        assert non_constructible_change(coins) == expected

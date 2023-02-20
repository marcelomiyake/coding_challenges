from algo_expert.arrays.medium.move_element_to_end import move_element_to_end


class TestMoveElementToEnd:
    def test_case_0(self):
        array = [2, 1, 2, 2, 2, 3, 4, 2]
        to_move = 2

        expected = [1, 3, 4, 2, 2, 2, 2, 2]

        assert move_element_to_end(array, to_move) == expected

    def test_case_5(self):
        array = [3, 1, 2, 4, 5]
        to_move = 3

        expected = [1, 2, 4, 5, 3]

        assert move_element_to_end(array, to_move) == expected

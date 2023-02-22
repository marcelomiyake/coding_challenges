from algo_expert.strings.medium.one_edit import one_edit


class TestOneEdit:
    def test_case_0(self):
        string_one = "hello"
        string_two = "hollo"

        expected = True

        assert one_edit(string_one, string_two) == expected

    def test_case_4(self):
        string_one = "ab"
        string_two = "a"

        expected = True

        assert one_edit(string_one, string_two) == expected

    def test_case_31(self):
        string_one = "abcdefghijklmnopqrstuvwxyz"
        string_two = "abcdefghijklnopqrstuvwxyz"

        expected = True

        assert one_edit(string_one, string_two) == expected

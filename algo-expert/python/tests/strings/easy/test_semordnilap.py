from algo_expert.strings.easy.semordnilap import semordnilap


class TestSemordnilap:
    def test_case_0(self):
        words = ["diaper", "abc", "test", "cba", "repaid"]

        expected = [
            ["diaper", "repaid"],
            ["abc", "cba"]
        ]

        assert semordnilap(words) == expected

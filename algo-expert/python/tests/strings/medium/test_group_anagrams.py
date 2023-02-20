from algo_expert.strings.medium.group_anagrams import group_anagrams


class TestGroupAnagrams:
    def test_case_0(self):
        words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]

        expected = [
            ["yo", "oy"],
            ["flop", "olfp"],
            ["act", "tac", "cat"],
            ["foo"]
        ]

        assert sorted(group_anagrams(words)) == sorted(expected)

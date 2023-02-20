from algo_expert.arrays.easy.tournament_winner import tournament_winner


class TestTournamentWinner:
    def test_case_0(self):
        competitions = [
            ["HTML", "C#"],
            ["C#", "Python"],
            ["Python", "HTML"]
        ]
        results = [0, 0, 1]

        expected = "Python"

        assert tournament_winner(competitions, results) == expected

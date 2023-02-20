from collections import defaultdict


def tournament_winner(competitions: list, results: list) -> str:
    scoreboard = defaultdict(int)
    for i in range(len(results)):
        winner = 0 if results[i] == 1 else 1
        scoreboard[competitions[i][winner]] += 3
    return max(scoreboard, key=scoreboard.get)

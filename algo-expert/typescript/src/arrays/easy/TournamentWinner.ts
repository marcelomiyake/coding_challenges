export function tournamentWinner(competitions: string[][], results: number[]) {
  let score = new Map<string, number>();
  let maxScore = 0;
  let champion = '';
  for (let i in results) {
    const loser = competitions[i][results[i]];
    const winner = competitions[i][results[i] === 1 ? 0 : 1];
    const winnerScore = score.has(winner) ? score.get(winner)! : 0;
    const loserScore = score.has(loser) ? score.get(loser)! : 0;
    score.set(winner, winnerScore + 3);
    score.set(loser, loserScore);
    if (score.get(winner)! > maxScore) {
      maxScore = score.get(winner)!;
      champion = winner;
    }
  }
  return champion;
}

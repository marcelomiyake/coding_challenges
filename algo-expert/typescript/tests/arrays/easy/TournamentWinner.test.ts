import {tournamentWinner} from '../../../src/arrays/easy/TournamentWinner'

describe('Tournament Winner', () => {
  test('Test Case 0', () => {
    const competitions = [['HTML', 'C#'], ['C#', 'Python'], ['Python', 'HTML']]
    const results = [0, 0, 1]

    const expected = 'Python'

    expect(tournamentWinner(competitions, results)).toBe(expected)
  })
})

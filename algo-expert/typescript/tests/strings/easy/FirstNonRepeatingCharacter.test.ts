import {firstNonRepeatingCharacter} from '../../../src/strings/easy/FirstNonRepeatingCharacter'

describe('First Non-Repeating Character', () => {
  test('Test Case 0', () => {
    const string = 'abcdcaf'

    const expected = 1

    expect(firstNonRepeatingCharacter(string)).toBe(expected)
  }),
  test('Test Case 2', () => {
    const string = 'faadabcbbebdf'

    const expected = 6

    expect(firstNonRepeatingCharacter(string)).toBe(expected)
  })
})

import {isValidSubsequence} from '../../../src/arrays/easy/ValidateSubSequence'

describe('Validate Subsequence', () => {
  test('Test Case 0', () => {
    const array = [5, 1, 22, 25, 6, -1, 8, 10]
    const sequence = [1, 6, -1, 10]

    const expected = true

    expect(isValidSubsequence(array, sequence)).toBe(expected)
  })
})

import {twoNumberSum} from '../../../src/arrays/easy/TwoNumberSum'

describe('Two Number Sum', () => {
  test('Test Case 0', () => {
    const array: number[] = [3, 5, -4, 8, 11, 1, -1, 6]
    const targetSum = 10

    const expected = [11, -1]

    expect(twoNumberSum(array, targetSum)).toStrictEqual(expected)
  })
})

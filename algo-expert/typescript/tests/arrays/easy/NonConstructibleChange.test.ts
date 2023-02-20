import {nonConstructibleChange} from '../../../src/arrays/easy/NonConstructibleChange';

describe('Non-Constructible Change', () => {
  test('Test Case 0', () => {
    const coins = [5, 7, 1, 1, 2, 3, 22]

    const expected = 20

    expect(nonConstructibleChange(coins)).toBe(expected)
  })

  test('Test Case 2', () => {
    const coins = [1, 1, 1, 1, 1]

    const expected = 6

    expect(nonConstructibleChange(coins)).toBe(expected)
  })
})

import {sortedSquaredArray} from '../../../src/arrays/easy/SortedSquaredArray'

describe('Sorted Squared Array', () => {
  test('Test Case 0', () => {
    const array = [1, 2, 3, 5, 6, 8, 9]

    const expected = [1, 4, 9, 25, 36, 64, 81]

    expect(sortedSquaredArray(array)).toStrictEqual(expected)
  })
})

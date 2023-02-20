import {semordnilap} from '../../../src/strings/easy/Semordnilap'

describe('Semordnilap', () => {
  test('Test Case 0', () => {
    const words = ['diaper', 'abc', 'test', 'cba', 'repaid']

    const expected = [['diaper', 'repaid'], ['abc', 'cba']]

    expect(semordnilap(words)).toStrictEqual(expected)
  })
})

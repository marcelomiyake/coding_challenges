import {runLengthEncoding} from '../../../src/strings/easy/RunLengthEncoding'

describe('Run-Length Encoding', () => {
  test('Test Case 0', () => {
    const string = 'AAAAAAAAAAAAABBCCCCDD'

    const expected = '9A4A2B4C2D'

    expect(runLengthEncoding(string)).toBe(expected)
  })
})

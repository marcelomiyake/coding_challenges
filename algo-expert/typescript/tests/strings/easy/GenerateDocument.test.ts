import {generateDocument} from '../../../src/strings/easy/GenerateDocument'

describe('Generate Document', () => {
  test('Test Case 0', () => {
    const characters = 'Bste!hetsi ogEAxpelrt x '
    const document = 'AlgoExpert is the Best!'

    const expected = true

    expect(generateDocument(characters, document)).toBe(expected)
  })
})

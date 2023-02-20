import {caesarCipherEncryptor} from '../../../src/strings/easy/CaesarCipherEncryptor'

describe('Caesar Cipher Encryptor', () => {
  test('Test Case 0', () => {
    const string = 'xyz'
    const key = 2

    const expected = 'zab'

    expect(caesarCipherEncryptor(string, key)).toBe(expected)
  })
})

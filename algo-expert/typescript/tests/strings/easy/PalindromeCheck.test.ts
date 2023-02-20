import {isPalindrome} from '../../../src/strings/easy/PalindromeCheck'

describe('Palindrome Check', () => {
  test('Test Case 0', () => {
    const string = 'abcdcba'

    const expected = true

    expect(isPalindrome(string)).toBe(expected)
  })
})

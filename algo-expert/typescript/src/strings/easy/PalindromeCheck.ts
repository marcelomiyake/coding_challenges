export function isPalindrome(string: string) {
  const chars = string.split('');

  for (let i = 0; i < string.length / 2; i++) {
    if (chars[i] != chars[string.length - 1 - i]) {
      return false;
    }
  }
  return true;
}

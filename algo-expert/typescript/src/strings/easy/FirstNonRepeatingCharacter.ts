export function firstNonRepeatingCharacter(string: string): number {
  const chars = string.split('');
  for (let i in chars) {
    const charsWithoutChar = string.split('');
    const char = chars[i];
    delete charsWithoutChar[i];
    if (!charsWithoutChar.includes(char)) {
      return +i;
    }
  }
  return -1;
}

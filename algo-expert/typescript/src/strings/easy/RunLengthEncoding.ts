export function runLengthEncoding(string: string) {
  const chars = string.split('');
  let encodedChars = [];
  let counter = 1;
  let lastChar = chars[0];
  for (let i = 1; i < string.length; i++) {
    if (chars[i] != lastChar || counter == 9) {
      encodedChars.push(counter);
      encodedChars.push(lastChar);
      counter = 1;
      lastChar = chars[i];
    } else {
      counter++;
    }
  }
  encodedChars.push(counter);
  encodedChars.push(lastChar);
  return encodedChars.join('');
}

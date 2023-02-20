export function caesarCipherEncryptor(string: string, key: number) {
  const chars = string.split('');
  let cryptedChars = [];
  const maxCode = 'z'.charCodeAt(0);
  for (let c of chars) {
    let code = c.charCodeAt(0) + key;
    while (code > maxCode) {
      code -= 'z'.charCodeAt(0) - 'a'.charCodeAt(0) + 1;
    }
    cryptedChars.push(String.fromCharCode(code));
  }
  return cryptedChars.join('');
}

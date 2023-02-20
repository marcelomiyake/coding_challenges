export function semordnilap(words: string[]) {
  let palindromes = new Map<string, string>();
  for (let i = 0; i < words.length - 1; i++) {
    if (palindromes.get(words[i]) != undefined) {
      continue;
    }
    for (let j = i + 1; j < words.length; j++) {
      let reverse = "";
      for (let char of words[j]) {
        reverse = char.concat(reverse);
      }
      if (words[i] === reverse) {
        palindromes.set(words[j], words[i]);
      }
    }
  }
  let result = [];
  const iterator = palindromes.keys();
  let key;
  while (!(key = iterator.next()).done) {
    result.push([palindromes.get(key.value), key.value])
  }
  return result;
}

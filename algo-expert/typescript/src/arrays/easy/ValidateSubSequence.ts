export function isValidSubsequence(array: number[], sequence: number[]): boolean {
  let j = 0;
  for (let i in sequence) {
    let isInArray = false;
    while (j < array.length) {
      if (sequence[i] === array[j]) {
        array.splice(j, 1);
        isInArray = true;
        break;
      }
      j++;
    }
    if (!isInArray) {
      return false;
    }
  }
  return true;
}


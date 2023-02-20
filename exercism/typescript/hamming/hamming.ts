export function compute(left: string, right: string): number {
  if (left.length != right.length) {
    throw Error("DNA strands must be of equal length.");
  }
  let distance = 0;
  let leftLetters = left.split('');
  let rightLetters = right.split('');
  for (let i in leftLetters) {
    if (leftLetters[i] != rightLetters[i]) {
      distance++;
    }
  }
  return distance;
}

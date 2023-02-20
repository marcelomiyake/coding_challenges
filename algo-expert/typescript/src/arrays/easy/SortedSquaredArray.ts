export function sortedSquaredArray(array: number[]) {
  return array.map(n => Math.pow(n, 2)).sort((a, b) => a - b);
}

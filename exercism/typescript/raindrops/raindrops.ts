export function convert(drops: number): string {
  let result = "";
  if (drops % 3 == 0) {
    result += 'Pling';
  }
  if (drops % 5 == 0) {
    result += 'Plang';
  }
  if (drops % 7 == 0) {
    result += 'Plong';
  }
  if (drops % 3 != 0 && drops % 5 != 0 && drops % 7 != 0) {
    result = drops.toString();
  }
  return result;
}

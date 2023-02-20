export function isArmstrongNumber(number: number): boolean {
  return number === number.toString()
    .split('')
    .map(digit => Math.pow(+digit, number.toString().length))
    .reduce((acc, partial) => acc + partial);
}

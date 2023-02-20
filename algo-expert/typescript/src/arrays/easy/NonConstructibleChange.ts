export function nonConstructibleChange(coins: number[]) {
  const totalCoins = coins.length;
  if (totalCoins == 0) {
    return 1;
  }
  coins.sort((a, b) => a - b);
  let change = 0;
  for (let i in coins) {
    if (coins[i] > change + 1) {
      return change + 1;
    }
    change += coins[i];
  }
  return change + 1;
}

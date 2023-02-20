def non_constructible_change(coins: list) -> int:
    sum_coins = 1

    if len(coins) == 0:
        return sum_coins

    sorted_coins = sorted(coins)
    for c in sorted_coins:
        if c > sum_coins:
            return sum_coins
        sum_coins += c
    return sum_coins

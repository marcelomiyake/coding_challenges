import sys


# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        min_price = sys.maxsize
        len_prices = len(prices)
        for i in range(len_prices):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
        return max_profit

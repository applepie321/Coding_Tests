# 2706. Buy Two Chocolates

# https://leetcode.com/problems/buy-two-chocolates/description/?envType=daily-question&envId=2023-12-20


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        sorted_prices = sorted(prices)
        if sorted_prices[0] + sorted_prices[1] > money:
            return money
        else:
            return money - (sorted_prices[0]+sorted_prices[1])

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = float('inf')
        maxi = 0
        for price in prices:
            if price < mini:
                mini = price
            elif price - mini > maxi:
                maxi = price - mini
        return maxi
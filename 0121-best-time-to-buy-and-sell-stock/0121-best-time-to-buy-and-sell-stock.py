class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp = prices[0]
        maxp = 0

        for i in range(1, len(prices)):
            if prices[i] < minp:
                minp = prices[i]
            
            profit = prices[i] - minp
            maxp = max(maxp, profit)

        return maxp
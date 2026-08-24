class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0

        l = 0
        r = (l + 1)
        
        lowest = prices[l]

        while r < len(prices):
            if prices[r] < lowest:
                lowest = prices[r]
                r += 1
            else:
                profit = prices[r] - lowest
                max_p = max(max_p, profit)
                r += 1
        
        return max_p


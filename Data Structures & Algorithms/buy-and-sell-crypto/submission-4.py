class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0

        
        r = 1
        lowest = prices[0]

        while r < len(prices):
            if prices[r] < lowest:
                lowest = prices[r]
            else:
                diff = prices[r] - lowest
                max_p = max(max_p, diff)
                r += 1

        return max_p


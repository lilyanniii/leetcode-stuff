class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0

        l, r = 0, 1

        lowest_val = prices[l]

        while r < len(prices):
            if prices[r] < lowest_val:
                lowest_val = prices[r]
                
            else:
                profit = prices[r] - lowest_val
                max_p = max(max_p, profit)
            
                r += 1

        return max_p


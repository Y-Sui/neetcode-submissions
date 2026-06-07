class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sliding window (two pointers)
        l = 0
        res = 0

        for r in range(len(prices)):
            if prices[r] > prices[l]:
                # 说明有profit
                profit = prices[r] - prices[l]
                res = max(res, profit)
            else:
                l = r
            # r += 1

        return res
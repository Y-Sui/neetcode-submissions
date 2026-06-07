class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sliding window

        left, right = 0, 1
        res = 0

        while right < len(prices):
            if prices[right] > prices[left]:
                # 说明有profit
                profit = prices[right] - prices[left]
                res = max(res, profit)
            else:
                left = right
            right += 1

        return res
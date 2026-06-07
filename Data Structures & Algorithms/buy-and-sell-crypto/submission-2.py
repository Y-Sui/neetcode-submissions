class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # two pointers

        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                # 这里比较巧妙，只要r发现一个比l低的新低点，l就会直接跳到那个最低点
                l = r
            r += 1

        return maxP
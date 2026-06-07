class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])

        # dp[0] = 0
        # dp[1] = 0

        n = len(cost)

        prev2 = 0
        prev1 = 0

        for i in range(2, n + 1):
            curr = min(prev1 + cost[i-1], prev2 + cost[i-2])

            prev2 = prev1
            prev1 = curr

        return prev1


# O(n), O(1)
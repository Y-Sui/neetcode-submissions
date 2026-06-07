class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        # dp[0] = nums[0]
        # dp[1] = max(nums[0], nums[1])

        if not nums:
            return 0

        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        
        prev2 = nums[0]
        prev1 = max(nums[0], nums[1])

        for i in range(2, n):
            curr = max(prev1, prev2 + nums[i])

            prev2 = prev1
            prev1 = curr

        return prev1
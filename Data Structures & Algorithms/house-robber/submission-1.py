class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        # dp[0] = nums[0]
        # dp[1] = max(nums[0], nums[1])

        # 写法1
        # if not nums:
        #     return 0

        # n = len(nums)
        # if n == 1:
        #     return nums[0]
        # if n == 2:
        #     return max(nums[0], nums[1])
        
        # prev2 = nums[0]
        # prev1 = max(nums[0], nums[1])

        # for i in range(2, n):
        #     curr = max(prev1, prev2 + nums[i])
        #     prev2 = prev1
        #     prev1 = curr

        # return prev1


        # 写法2
        # 含义：假装在第一间房子之前，有两间金额为 0 的“虚拟房子”
        # prev2 代表 dp[i-2], prev1 代表 dp[i-1]
        prev2 = 0
        prev1 = 0

        # 2. 遍历每一个房子 (直接遍历数值 x，不用索引 i)
        for x in nums:
            # 3. 核心公式：偷这间(x + prev2) vs 不偷这间(prev1)
            curr = max(prev1, prev2 + x)
            
            # 4. 滚动更新
            prev2 = prev1
            prev1 = curr
            
        # 5. 循环结束，prev1 就是最大值
        return prev1



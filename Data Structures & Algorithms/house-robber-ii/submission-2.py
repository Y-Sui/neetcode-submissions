class Solution:
    def rob(self, nums: List[int]) -> int:
        # the case is the dp[n] and dp[0] cannot been robbed at the same time, they are adjacent.
        # case 1: range -> 0: n-2
        # case 2: range -> 1: n-1
        # max(case1, case2)

        n = len(nums)
        # 1. Edge Cases (必须单独处理)
        # 如果只有一间房子，圈不圈无所谓，只能偷它
        if n == 0: return 0
        if n == 1: return nums[0]
        
        # 2. 定义复用的线性 DP 函数 (就是上一题的代码)
        def rob_linear(arr):
            prev2, prev1 = 0, 0
            for x in arr:
                # 滚动数组逻辑
                current = max(prev1, prev2 + x)
                prev2 = prev1
                prev1 = current
            return prev1
        
        # 3. 破圈：比较两种情况
        # 情况 A: 去掉尾巴 (nums[:-1])
        result1 = rob_linear(nums[:-1])
        
        # 情况 B: 去掉头部 (nums[1:])
        result2 = rob_linear(nums[1:])
        
        return max(result1, result2)
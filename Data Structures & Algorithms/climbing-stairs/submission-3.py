class Solution:
    def climbStairs(self, n: int) -> int:
        
        """
        dp 问题，倒推法

        假设你要走到第 n 级台阶。你的最后一步只有两种可能：
        从第 n-1 级迈 1 步上来。从第 n-2 级迈 2 步上来。
        这意味着：走到第 n 级的方案数 = 走到第 n-1 级的方案数 + 走到第 n-2 级的方案数写成公式就是：
        $$f(n) = f(n-1) + f(n-2)$$
        """

        # # base cases
        # if n == 1: return 1
        # if n == 2: return 2

        # # init two states dp[0], dp[1]
        # prev2 = 1  # 代表 f(i-2)，初始为第一级台阶的走法, dp[i-2]
        # prev1 = 2  # 代表 f(i-1)，初始为第二级台阶的走法, dp[i-1]
    
        # for i in range(3, n + 1):
        #     current = prev1 + prev2  # f(n) = f(n-1) + f(n-2)
            
        #     # 往前滚动变量, 不需要改
        #     prev2 = prev1
        #     prev1 = current
        
        # # 通常是prev1，因为循环结束时prev1 == current
        # return prev1



        # (Top-down DP) 带备忘录的递归
        memo = {}
        if n == 1: return 1
        if n == 2: return 2
            
        # 查备忘录：如果以前算过，直接返回，别再算了！
        if n in memo:
            return memo[n]

        # 没算过？那算一遍，并且记在小本本上
        result = self.climbStairs(n-1) + self.climbStairs(n-2)
        memo[n] = result

        return result
            















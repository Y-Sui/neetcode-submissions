class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Unbounded Knapsack Problem 完全背包问题

        # 1. 定义 DP 数组，长度为 amount + 1
        # 初始化为一个"不可能达到的最大值"，比如 amount + 1
        # (注意：不能初始化为 -1 或 0，否则 min() 函数会失效)
        dp = [amount + 1] * (amount + 1)
        
        # 2. Base Case
        dp[0] = 0
        
        # 3. 外层循环：遍历所有从 1 到 amount 的金额
        for i in range(1, amount + 1):
            # 4. 内层循环：尝试每一种硬币
            for coin in coins:
                # 如果当前金额 i 比硬币面值大，才可能凑得出来
                if i >= coin:
                    # 核心公式：
                    # dp[i] = min(当前已知的最少方案, 拿了这个硬币之后的方案)
                    dp[i] = min(dp[i], dp[i - coin] + 1)
                    
        # 5. 检查结果
        # 如果 dp[amount] 还是初始值，说明无法凑出，返回 -1
        if dp[amount] == amount + 1:
            return -1
        else:
            return dp[amount]
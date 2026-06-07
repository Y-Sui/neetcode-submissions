class Solution:
    def countBits(self, n: int) -> List[int]:
        # 初始化 dp 数组，长度为 n + 1，初始值全为 0
        dp = [0] * (n + 1)
        
        # 从 1 开始遍历到 n
        for i in range(1, n + 1):
            # 利用之前的计算结果
            # i >> 1 就是 i的一半
            # i & 1 就是看 i 是奇数还是偶数
            dp[i] = dp[i >> 1] + (i & 1)
            
        return dp
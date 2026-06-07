class Solution:
    def numDecodings(self, s: str) -> int:
        # dp[i] 表示字符串的前i个字符 一共有多少种解码方式
        if s[0] == "0": return 0

        n = len(s)
        
        # prev2 代表 dp[i-2] (初始为 dp[0])
        prev2 = 1
        # prev1 代表 dp[i-1] (初始为 dp[1])
        prev1 = 1
        
        for i in range(1, n):
            current = 0
            
            # 情况 A: 看当前一位 s[i]
            # 只要不是 '0'，就可以继承 prev1
            if s[i] != "0":
                current += prev1
            
            # 情况 B: 看最后两位 s[i-1]s[i]
            # 组合起来必须在 10 到 26 之间
            two_digits = int(s[i-1 : i+1])
            if 10 <= two_digits <= 26:
                current += prev2
            
            # 滚动更新
            prev2 = prev1
            prev1 = current
            
        return prev1
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 1. 处理特殊情况
        if not s:
            return ""
        
        # 记录最长回文串的起始位置和长度
        start = 0
        max_len = 0
        
        for i in range(len(s)):
            # 2. 情况A: 奇数长度 (以 s[i] 为中心)
            len1 = self.expand(s, i, i)
            
            # 3. 情况B: 偶数长度 (以 s[i], s[i+1] 为中心)
            len2 = self.expand(s, i, i + 1)
            
            # 4. 取两者较长的一个
            curr_len = max(len1, len2)
            
            # 5. 如果找到了更长的，更新 start 和 max_len
            if curr_len > max_len:
                max_len = curr_len
                # 核心数学公式：根据中心点 i 和长度算出起始点 start
                # 例子：aba (i=1, len=3) -> start = 1 - (2)//2 = 0
                # 例子：abba (i=1, len=4) -> start = 1 - (3)//2 = 0
                start = i - (curr_len - 1) // 2
                
        # 6. 截取并返回
        return s[start : start + max_len]

    def expand(self, s, left, right):
        # 向外扩散的 helper function
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        # 注意返回值：
        # 跳出循环时，s[left] != s[right]，实际回文不包含 left 和 right
        # 长度公式 = (right - 1) - (left + 1) + 1 = right - left - 1
        return right - left - 1
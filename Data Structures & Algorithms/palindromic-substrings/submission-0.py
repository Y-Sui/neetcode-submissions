class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        
        for i in range(len(s)):
            # 1. 以 s[i] 为中心的奇数长度回文串
            result += self.extend(s, i, i)
            
            # 2. 以 s[i]和s[i+1] 之间为中心的偶数长度回文串
            result += self.extend(s, i, i + 1)
            
        return result
    
    def extend(self, s, left, right):
        count = 0
        # 只要没越界，且左右相等，就是一个回文
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1      # 发现回文，计数 +1
            left -= 1       # 向左扩
            right += 1      # 向右扩
        return count
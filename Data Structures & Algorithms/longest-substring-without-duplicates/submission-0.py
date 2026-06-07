class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        l = 0
        res = 0
        charSet = set()

        for r in range(len(s)):

            # 发现有重复，收缩左侧边界l
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1

            # while 结束后，s[r]已经不重复了，加入set
            charSet.add(s[r])

            # 更新最大长度
            res = max(res, r -l + 1)
        
        return res
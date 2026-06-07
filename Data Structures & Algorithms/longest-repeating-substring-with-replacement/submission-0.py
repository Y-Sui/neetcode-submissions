class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # 目标需要找到一个最长的窗口【l，r】
        # 窗口需要满足 条件：需要替换的次数 小于k，(r - l + 1) - max_freq <= k，max_freq是窗口里出现次数最多的字符

        res = 0
        charSet = set(s)

        for c in charSet:
            count = l = 0
            for r in range(len(s)):
                if s[r] == c:
                    count += 1

                while (r - l + 1) - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1

                res = max(res, r - l + 1)
        return res
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # 整体的思路应该是保留出现次数最多的那个字符，把其他所有字符都替换掉
        # 只要满足 窗口长度 - 窗口内出现次数最多的字符数 <= k
        # 如果满足，说明可以通过<=k次替换，把窗口里的所有字符数变成一样的，此时，尝试扩大窗口
        # 如果不满足，说明即使把k次机会全用光，也无法把剩余的杂乱字符全换掉，此时需要缩小窗口
        count = {} # 每个字符的频次
        res = 0
        l = 0
        max_f = 0 # 窗口内单个字符出现的历史最大频次
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            max_f = max(max_f, count[s[r]])

            # 如果当前窗口的长度 - 历史最大频次 > k，说明窗口不合法
            while (r - l + 1) - max_f > k:
                count[s[l]] -= 1
                l += 1

            # 此时窗口是合法的，更新最大长度
            res = max(res, r - l + 1)

        return res

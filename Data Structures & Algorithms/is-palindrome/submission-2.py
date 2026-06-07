class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            # 处理edge cases，比方说句子带？等，遇到就避开
            while l < r and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r -= 1
            
            # more efficient
            if l >= r:
                break

            # 核心：判断两边的文本/数字是不是一致
            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1
        return True
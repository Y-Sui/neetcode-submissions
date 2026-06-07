class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        l, r = 0, len(s) -1
        while l < r:
            if s[l] != s[r]:
                left_valid = is_palindrome(l + 1, r)
                right_valid = is_palindrome(l, r - 1)
                return left_valid or right_valid

            l += 1
            r -= 1
        return True
        

                
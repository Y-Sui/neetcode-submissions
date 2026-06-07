class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointers, "Was it a car or a cat I saw?", l -> "W", and r -> "w"
        l, r = 0, len(s) - 1

        # isalnum() check whether it is char or num;
        # isnumeric() check whether it is num;
        # isalpha() check whether it is char
        while l < r:
            while l < r and not s[r].isalnum():
                r -= 1
            while l < r and not s[l].isalnum():
                l += 1

            # case: s= "0P",
            if l >= r:
                break

            # core logic is to compare the s[l] and s[r]
            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1
        
        return True
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid_map = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        for char in s:
            if char in valid_map.keys():
                if stack and valid_map[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        if stack:
            return False
        else:
            return True

        
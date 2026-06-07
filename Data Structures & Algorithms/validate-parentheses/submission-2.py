class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for c in s:
            if c not in close_to_open:
                stack.append(c)

            else:
                if stack and close_to_open[c] == stack[-1]:
                    stack.pop()
                else:
                    return False

        return True if not stack else False
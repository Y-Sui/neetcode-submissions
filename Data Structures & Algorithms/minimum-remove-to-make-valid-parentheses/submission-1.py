class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        if not s:
            return s
        s_list = list(s)
        stack = []
        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            elif char == ")":
                if stack:
                    stack.pop()
                else:
                    s_list[i] = ""

        # remove the inital (
        for i in stack:
            s_list[i] = ""

        return "".join(s_list)
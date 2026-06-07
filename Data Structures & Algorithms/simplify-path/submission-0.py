class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = [] # more like cache for all the operation
        paths = path.split("/") # "", "neetcode", "pratice", "", "...", "", "", "..", "courses"
        for cur in paths:
            if cur == "..":
                if stack:
                    stack.pop()
            elif cur == "." or cur == "":
                continue
            else:
                stack.append(cur)

        # stack = "neetcode", "practice", "courses"
        return "/" + "/".join(stack)
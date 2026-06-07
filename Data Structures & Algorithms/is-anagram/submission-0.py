class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        visited, visited_t = dict(), dict()
        for i in range(len(s)):
            if s[i] in visited:
                visited[s[i]] += 1
            else:
                visited[s[i]] = 0

        for i in range(len(t)):
            if t[i] in visited_t:
                visited_t[t[i]] += 1
            else:
                visited_t[t[i]] = 0

        if visited == visited_t:
            return True

        else:
            return False
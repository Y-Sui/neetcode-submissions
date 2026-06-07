class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {} # key: index; value: True/False
        def dfs(start_index):
            if start_index in memo:
                return memo[start_index]
            
            if start_index ==len(s):
                return True

            for w in wordDict:
                if s.startswith(w, start_index):
                    if dfs(start_index + len(w)):
                        memo[start_index] = True
                        return True


            memo[start_index] = False
            return False

        return dfs(0)
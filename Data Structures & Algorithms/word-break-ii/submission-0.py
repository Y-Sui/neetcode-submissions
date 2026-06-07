class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # s, wordDict
        # add spaces to s

        wordSet = set(wordDict)
        memo = {}

        def backtrack(i):
            if i in memo:
                return memo[i]
            
            # base case
            if i == len(s):
                return [""]
            
            res = []
            for j in range(i, len(s)):
                w = s[i: j+1]
                if w in wordSet:
                    sub_list = backtrack(j+1)
                    
                    for sub in sub_list:
                        if sub == "":
                            res.append(w)
                        else:
                            res.append(w + " " + sub)

            memo[i] = res
            return res

        return backtrack(0)
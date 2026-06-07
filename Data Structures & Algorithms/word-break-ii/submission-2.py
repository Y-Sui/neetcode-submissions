class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # s, wordDict
        # add spaces to s

        word_set = set(wordDict)
        memo = {} # key is the string, value is a list of sentences

        # find all the sentences starting from index i
        def backtrack(curr_s):
            # check memo
            if curr_s in memo:
                return memo[curr_s]
            
            # base case, end of string reached
            if not curr_s:
                return [""]

            res = []
            
            # iterate through possible words
            for word in word_set:
                if curr_s.startswith(word):
                    # recurse on the remainder
                    suffix = curr_s[len(word):]
                    sub_sentences = backtrack(suffix)

                    # build the sentence
                    for sub in sub_sentences:
                        if sub == "":
                            # reach the end of string, just add the word
                            res.append(word)
                        else:
                            res.append(word + " " + sub)

            memo[curr_s] = res
            return res

        return backtrack(s)
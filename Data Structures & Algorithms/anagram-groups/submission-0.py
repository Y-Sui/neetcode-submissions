class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1 or len(strs) == 0:
            return [strs]

        res = defaultdict(list)
        for s in strs:
            # sorting
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)

        return list(res.values())

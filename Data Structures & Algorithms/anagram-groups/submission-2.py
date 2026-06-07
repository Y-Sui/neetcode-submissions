class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1 or len(strs) == 0:
            return [strs]

        # res = defaultdict(list)
        # for s in strs:
        #     count = [0] * 26 # 把key先固定为26个字母的placeholder, otherwise, 可以用sorted来获得
        #     for c in s:
        #         count[ord(c) - ord('a')] += 1
        #     res[tuple(count)].append(s)

        # return list(res.values())


        res = defaultdict(list)
        for s in strs:
            sorted_s = "".join(sorted(s))
            res[sorted_s].append(s)

        return list(res.values())
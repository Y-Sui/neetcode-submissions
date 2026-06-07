class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) or not s or not t:
            return False
        anagram_dict_s = collections.defaultdict(int)
        anagram_dict_t = collections.defaultdict(int)
        for i in range(len(s)):
            anagram_dict_s[s[i]] += 1
            anagram_dict_t[t[i]] += 1
        
        return anagram_dict_s == anagram_dict_t

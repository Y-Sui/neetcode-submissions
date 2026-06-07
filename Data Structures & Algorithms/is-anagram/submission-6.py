class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_dict_s, char_dict_t = {}, {}
        for i in range(len(s)):
            char_dict_s[s[i]] = char_dict_s.get(s[i], 0) + 1
            char_dict_t[t[i]] = char_dict_t.get(t[i], 0) + 1

        if char_dict_s != char_dict_t:
            return False
        else:
            return True

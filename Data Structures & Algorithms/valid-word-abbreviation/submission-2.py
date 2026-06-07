class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        if word == abbr:
            return True

        p1 = p2 = 0 # p1 -> word, p2 -> abbr

        while p1 < len(word) and p2 < len(abbr):
            if abbr[p2].isdigit():
                if abbr[p2] == '0':
                    return False # leading zero, invalid
                num_val = 0
                while p2 < len(abbr) and abbr[p2].isdigit():
                    num_val = num_val * 10 + int(abbr[p2])
                    p2 += 1

                p1 += num_val
            else:
                if word[p1] != abbr[p2]:
                    return False
                p1 += 1
                p2 += 1

        return p1 == len(word) and p2 == len(abbr)
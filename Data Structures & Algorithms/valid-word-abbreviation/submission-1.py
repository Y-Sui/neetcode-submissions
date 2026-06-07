class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        if word == abbr:
            return True

        p1 = p2 = 0 # p1 -> pointer to word; p2 -> pointer to abbr

        while p1 < len(word) and p2 < len(abbr):
            # abbr start with digital
            if abbr[p2].isdigit(): 
                if abbr[p2] == '0':
                    return False

                # 解析整个数字
                num_val = 0
                while p2 < len(abbr) and abbr[p2].isdigit():
                    num_val = num_val * 10 + int(abbr[p2])
                    p2 += 1

                # i 跳跃
                p1 += num_val

            else:
                # abbr 当前字符是字母
                if word[p1] != abbr[p2]:
                    return False
                p1 += 1
                p2 += 1

        # 最后必须两个指针都刚好走完才算匹配成功
        return p1 == len(word) and p2 == len(abbr)
           
            
            
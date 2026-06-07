class Solution:

    def encode(self, strs: List[str]) -> str:
        # "4#neet4#code4#love3#you"
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            # 先读，直到读到 #，用另一个指针j
            j = i
            while s[j] != '#':
                j += 1
            
            # 循环结束，j在#的位置
            length = int(s[i:j])

            # 读取4个字符, 字符串开头在#之后
            start = j + 1
            end = start + length
            res.append(s[start:end])

            # 重复
            i = end

        return res

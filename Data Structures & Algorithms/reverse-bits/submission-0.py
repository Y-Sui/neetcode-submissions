class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        
        # 因为题目明确说是 32 位无符号整数
        # 所以不管 n 变成 0 了没，我们必须硬着头皮搬运 32 次
        # (比如 n=1，前面那 31 个 0 也要被翻转成 1 放到后面去)
        for _ in range(32):
            # 1. 把 res 往左挪一格，给新来的腾位置
            res = res << 1
            
            # 2. 拿出 n 的最后一位 (0 或 1)
            bit = n & 1
            
            # 3. 把这一位加到 res 的末尾
            res = res | bit  # 也可以写 res += bit
            
            # 4. 把 n 往右挪一格，扔掉刚才处理过的那一位
            n = n >> 1
            
        return res
    
    # 极简写法（利用 Python 字符串黑魔法，面试不建议只写这个）
    # def reverseBits(self, n: int) -> int:
    #     # 转二进制 -> 倒序 -> 转回十进制
    #     return int('{:032b}'.format(n)[::-1], 2)
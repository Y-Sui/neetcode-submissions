class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            # 动作 1：检查当前最后一位是不是 1
            # 如果是 1，res 加 1；如果是 0，res 加 0
            res += n & 1
            
            # 动作 2：把最后一位挤出去，让下一位补上来
            n = n >> 1

        return res
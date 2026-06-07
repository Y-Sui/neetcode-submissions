class Solution:

    def __init__(self, w: List[int]):
        self.prefix = [] # [1, 4] for input [1, 3]
        cur = 0
        for w_num in w:
            cur += w_num
            self.prefix.append(cur)

    def pickIndex(self) -> int:
        target = self.prefix[-1] * random.random()

        l, r = 0, len(self.prefix) - 1

        # 二分查找，寻找左侧边界，或者说寻找第一个大于target的位置
        while l <= r:
            mid = (l + r) // 2
            if self.prefix[mid] >= target:
                # mid的值大于target，说明mid可能是答案，或者答案在左边
                r = mid -1 
            else:
                l = mid + 1
        return l


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sum = [0]
        # prefix sum list
        for wgt in w:
            self.prefix_sum.append(self.prefix_sum[-1] + wgt)

    def pickIndex(self) -> int:
        # prefix_sum[-1] 总的权重，random.random()生成[0.0, 1.0)之间的浮点数
        # target是在[0, 总长度]之间随机选择的点
        target = self.prefix_sum[-1] * random.random()

        # 找prefix[i] <= target < prefix[i+1] 的那个 i
        l, r = 1, len(self.prefix_sum)
        while l < r:
            mid = (l + r) // 2
            if self.prefix_sum[mid] <= target:
                l = mid + 1
            else:
                r = mid

        return l - 1


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
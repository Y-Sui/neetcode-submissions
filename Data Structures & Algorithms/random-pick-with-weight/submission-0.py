class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.index_probablity = dict() # key: index; value: probablity

    def pickIndex(self) -> int:
        sum_value = sum(self.w)
        for i, w_num in enumerate(self.w):
            self.index_probablity[i] = w_num / sum_value

        sorted_dict = sorted(self.index_probablity.items(), key=lambda x: x[1], reverse=True)

        return sorted_dict[0][0]


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
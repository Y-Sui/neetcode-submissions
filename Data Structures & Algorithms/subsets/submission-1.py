class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # consider backtracking, 实际上是在树上做DFS搜索
        res = []
        path = []

        def backtrack(start_index):
            res.append(path.copy())

            # 横向遍历，选择nums[start_index]及其后面的所有数字
            for i in range(start_index, len(nums)):
                # choose
                path.append(nums[i])
                backtrack(i + 1)
                # traceback
                path.pop()

        backtrack(0)
        return res
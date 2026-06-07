class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # consider backtracking
        # “每个数字都有两条路：选，或者不选。”
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            # --- 分支 1：选当前这个数 (左孩子) ---
            subset.append(nums[i])  # 动作：把 nums[i] 装进包里
            dfs(i+1)                # 递归：带着这个数，去考虑下一个数

            # --- 回溯 (Backtracking) ---
            # 刚才试过了“选”的情况，现在我要反悔，恢复现场
            subset.pop()            # 动作：把 nums[i] 拿出来

            # --- 分支 2：不选当前这个数 (右孩子) ---
            dfs(i+1)                # 递归：不带这个数，去考虑下一个数

        dfs(0)
        return res
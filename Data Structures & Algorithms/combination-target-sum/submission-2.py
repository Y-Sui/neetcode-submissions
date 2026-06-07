class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def backtrack(start_index, curr_sum):
            if curr_sum == target:
                res.append(path.copy())
                return 
            if curr_sum > target:
                return

            for i in range(start_index, len(nums)):
                # pruning
                if curr_sum + nums[i] > target:
                    continue

                path.append(nums[i])
                backtrack(i, curr_sum + nums[i])
                path.pop()

        backtrack(0, 0)
        return res
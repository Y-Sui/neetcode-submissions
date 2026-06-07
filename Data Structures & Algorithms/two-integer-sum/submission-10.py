class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx, val in enumerate(nums):
            complement = target - val
            if complement not in seen:
                seen[val] = idx
            else:
                return [seen[complement], idx]
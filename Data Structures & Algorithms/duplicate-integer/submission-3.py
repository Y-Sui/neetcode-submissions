class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # nums.sort()
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return True
        # return False

        visited = set()
        for i in range(len(nums)):
            if nums[i] in visited:
                return True

            visited.add(nums[i])
        
        return False

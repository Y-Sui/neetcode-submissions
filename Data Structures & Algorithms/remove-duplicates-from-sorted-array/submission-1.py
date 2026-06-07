class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        slow = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[slow] = nums[i]

                slow += 1

        return slow
        
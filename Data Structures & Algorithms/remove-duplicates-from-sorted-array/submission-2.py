class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return []

        n = len(nums)
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r] # 现在这种方式nums的前l元素就是去重之后的结果
                l += 1

        return l


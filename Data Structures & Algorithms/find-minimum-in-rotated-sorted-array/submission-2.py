class Solution:
    def findMin(self, nums: List[int]) -> int:
        # rotated array有一个特性：一侧总是sorted，而另一侧包含rotation（以及最小的elements）
        # use binary search to identify which side is sorted
        # if the left half is sorted, then the mini cannot be there, so we search the right half
        # if the right half is sorted, then the mini must be in left half (or at the midpoint)
        # this let us eliminate half of the array and quickly narrow down to smallest value.
        if not nums:
            return None
        l, r = 0, len(nums) -1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[r]:
                # 说明mid在低位置，最小值可能是mid，也可能在mid的左侧
                r = mid
            elif nums[mid] > nums[r]:
                # 说明mid在高位置, 最小值应该mid的右侧
                l = mid + 1

        # 循环结束， l==r
        return nums[l]

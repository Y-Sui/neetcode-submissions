class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return None
        l, r = 0, len(nums) -1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] < nums[r]:
                # 说明mid在低位置，最小值可能是mid，也可能在mid的左侧
                r = mid
            elif nums[mid] > nums[r]:
                # 说明mid在高位置, 最小值应该mid的右侧
                l = mid + 1

        # 循环结束， l==r
        return nums[l]

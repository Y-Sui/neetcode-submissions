class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 核心在于我们可以把旋转数组看作两段上升的斜坡，一段在高处（大数值区），一段在低处（小数值区）。
        # 需要找到斜坡的分界在哪里
        # 传统的二分查找，通常拿mid和target比较，但在不知道最小值的具体大小时，应该拿mid和右边界nums[r]比较
        # 因为右边界代表低段位的上限，如果mid比右边界还大，说明mid在高段位，则应该移动l到mid+1
        # 如果mid比右边界还小，说明mid在低段位，则应该移动r到mid
        if not nums:
            return None
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l+r) // 2
            if nums[mid] < nums[r]:
                r = mid
            elif nums[mid] > nums[r]:
                l = mid + 1

        return nums[l]
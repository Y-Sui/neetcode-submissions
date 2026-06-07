class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) -1
        while l <= r:
            mid = l + (r - l) // 2
            if target == nums[mid]:
                return mid
            
            # 说明断崖不在这个左半部分
            if nums[l] <= nums[mid]:
                # 看看target在不在这部分，如果target不在这部分，说明一定在右半部分，l就可以移动到mid+1了
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                # target在这个部分，r就可以移动到mid-1
                else:
                    r = mid - 1
            # 断崖不在右半部分
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1
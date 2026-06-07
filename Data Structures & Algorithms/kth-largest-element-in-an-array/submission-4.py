import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # quick select
        target_index = len(nums) - k

        def quick_select(l, r):
            pivot_idx = random.randint(l, r) # random pickup to avoid O(n^2)

            # for easy control, move to the right
            # swap here
            nums[pivot_idx], nums[r] = nums[r], nums[pivot_idx]
            pivot = nums[r]

            # standard partition
            p_index = l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p_index], nums[i] = nums[i], nums[p_index]
                    p_index += 1

            # put the pivot to the right place
            nums[p_index], nums[r] = nums[r], nums[p_index]

            # 
            if p_index == target_index:
                return nums[p_index]
            elif p_index < target_index:
                return quick_select(p_index + 1, r)
            else:
                return quick_select(l, p_index - 1)

        return quick_select(0, len(nums) - 1)
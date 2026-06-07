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

            # standard partition, p_index is the leftest index that part the nums, value smaller than pivot are swapped to the p_index
            p_index = l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p_index], nums[i] = nums[i], nums[p_index]
                    p_index += 1

            # put the pivot to the right place
            # 现在是【比pivot小的，基准p_index, 比pivot大的】
            nums[p_index], nums[r] = nums[r], nums[p_index]

            # 现在p_index 已经在该在的位置上了，判断一下符不符合要求
            if p_index == target_index:
                return nums[p_index]
            # 如果不符合，基准位置在目标左边，说明答案在右边，扔掉所有左半边
            elif p_index < target_index:
                return quick_select(p_index + 1, r)
            else:
                return quick_select(l, p_index - 1)

        return quick_select(0, len(nums) - 1)
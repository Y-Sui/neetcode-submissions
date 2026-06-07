class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # binary search

        # 1. 我们二分的是 "数值范围"，不是数组下标
        #    答案肯定在 1 到 len(nums)-1 之间
        left, right = 1, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # 2. 统计阶段：
            #    遍历整个数组，看看有多少个数是 "小于等于 mid" 的
            #    注意：这里不需要数组是有序的，我们只是单纯地计数
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            
            # 3. 判断阶段 (抽屉原理)：
            #    原本 [1, mid] 区间里应该只有 mid 个数。
            #    如果现在的 count 超过了 mid，说明 "前半段" 有人重复了。
            if count > mid:
                right = mid  # 答案在 [left, mid]
            else:
                left = mid + 1 # 答案在 [mid+1, right]
                
        return left
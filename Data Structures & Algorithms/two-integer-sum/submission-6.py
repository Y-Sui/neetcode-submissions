class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return []
        
        # visited = dict()
        # for i in range(len(nums)):
        #     complement  = target - nums[i]

        #     if complement in visited:
        #         return [visited[complement], i]
        #     visited[nums[i]] = i

        # return []




        # two pointers
        nums_with_index = [(num, i) for i, num in enumerate(nums)]
        nums_with_index.sort()

        l, r = 0, len(nums_with_index) - 1
        while l < r:
            two_sum = nums_with_index[l][0] + nums_with_index[r][0]
            if two_sum < target:
                l += 1
                # # 重复值
                # while l < r and nums_with_index[l][0] == nums_with_index[l-1][0]: 
                #     l += 1
            elif two_sum > target:
                r -= 1
                # while l < r and nums_with_index[r][0] == nums_with_index[r+1][0]:
                #     r -= 1
            else:
                return sorted([nums_with_index[l][1], nums_with_index[r][1]])
        
        return []
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # pruning
            if a > 0:
                break
            
            # 跳过a的重复，如果当前的a和之前的a相同，跳过
            if i > 0 and a == nums[i-1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                threeSum = a + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    res.append([a, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # 跳过b的重复，和之前跳过a的逻辑一致，很巧妙
                    while nums[left] == nums[left -1] and left < right:
                        left += 1
                    
                    # # # 需要跳过c的重复吗？不需要，a，b不重复，c也不会重复
                    # # while nums[right] == nums[right +1] and left < right:
                    # #     right -= 1

        return res
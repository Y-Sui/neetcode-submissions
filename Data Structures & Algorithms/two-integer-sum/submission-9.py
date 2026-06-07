class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # check whether nums is sorted and keep the original indices
        enumerated_nums = [(val, i) for i, val in enumerate(nums)]
        enumerated_nums.sort()
        
        # enumerate_nums[0] = (value, original_index)
        i, j = 0, len(enumerated_nums) - 1
        while i <= j:
            two_sum = enumerated_nums[i][0] + enumerated_nums[j][0]
            first_idx = enumerated_nums[i][1]
            second_idx = enumerated_nums[j][1]
            if two_sum == target:
                return [first_idx, second_idx] if first_idx < second_idx else [second_idx, first_idx] 
            elif two_sum > target:
                j -= 1
            else:
                i += 1

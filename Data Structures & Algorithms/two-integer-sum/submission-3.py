class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return []
        
        visited = dict()
        for i in range(len(nums)):
            complement  = target - nums[i]

            if complement in visited:
                return [visited[complement], i]
            visited[nums[i]] = i

        return []
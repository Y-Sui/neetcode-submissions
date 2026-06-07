class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []
        for i, num in enumerate(nums):
            A.append([num, i]) # store the original index
        A.sort()

        left = 0
        right = len(nums) - 1
        while left < right:
            _sum = A[left][0] + A[right][0]
            if _sum < target:
                left += 1
            elif _sum > target:
                right -= 1
            else:
                return [min(A[left][1], A[right][1]), max(A[left][1], A[right][1])]
        return 
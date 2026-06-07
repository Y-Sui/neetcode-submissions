class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return []
        left, right = 0, len(numbers) - 1

        while left < right:
            _sum = numbers[left] + numbers[right]
            if _sum < target:
                left += 1
            elif _sum > target:
                right -= 1
            else:
                return [left + 1, right + 1]
        return []
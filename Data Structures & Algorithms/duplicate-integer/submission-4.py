class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # test cases
        if not nums:
            return False
        visited = set()
        for num in nums:
            if num not in visited:
                visited.add(num)
            else:
                return True
        return False
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        L = 0

        for R in range(len(nums)):
            # maintain the size of the window
            if R - L > k:
                window.remove(nums[L])
                L += 1
            # check duplication
            if nums[R] in window:
                return True
            window.add(nums[R])

        return False

        
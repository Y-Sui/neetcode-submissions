class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        L = 0

        # 从左到右扫描数组，对于当前位置R，我只需要知道，前面的K个位置有没有和nums[R]相同的数，有就返回，没有就加入window
        for R in range(len(nums)):
            if R - L > k:
                window.remove(nums[L])
                L += 1

            if nums[R] in window:
                return True

            window.add(nums[R])

        return False
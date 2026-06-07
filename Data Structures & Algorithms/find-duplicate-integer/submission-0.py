class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # using O(1) space complexity, 快慢指针 Floyd 判圈算法
        # 这道题太好了，实际上是把array当做了一个linked list来做，这种情况下array中的重复值就可以变成linked list里的cycle
        
        # stage 1 快慢指针找相遇点
        slow = 0
        fast = 0

        while True:
            slow = nums[slow] # slow 走一步
            fast = nums[nums[fast]] # fast 走两步
            if slow == fast: # 如果相遇，说明有环
                break

        # stage 2 找到环的入口
        slow = 0

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
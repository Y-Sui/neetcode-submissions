class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = []
        for i, num in enumerate(nums):
            heapq.heappush(max_heap, -num)

        for _ in range(k):
            value = heapq.heappop(max_heap)
        
        return -value
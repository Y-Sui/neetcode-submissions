class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # # O(nlogn)
        # # max_heap
        # # heappop k times, and the top is the res
        # max_heap = []
        # for num in nums:
        #     heapq.heappush(max_heap, -num)

        # for _ in range(k):
        #     value = heapq.heappop(max_heap)
        
        # return -value


        # min-heap size K
        # no need to store all the num, only maintain a min-heap with size K, and the smallest one is the target
        # O(nlogk)
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return min_heap[0]
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


        # # min-heap size K
        # # no need to store all the num, only maintain a min-heap with size K, and the smallest one is the target
        # # O(nlogk)
        # min_heap = []
        # for num in nums:
        #     heapq.heappush(min_heap, num)

        #     if len(min_heap) > k:
        #         heapq.heappop(min_heap)

        # return min_heap[0]


        # quick select
        # O(n)
        # idea is to use quicsort using a pivot element, element >= pivot element, go left, element < pivot element, go right
        # converts finding the kth largest to finding the (n-k)th smallest, simplifies the partitioning logic
        # find 2nd in a array of size 5 == find 3th in ascending order


        # i, j pointers, swapping elements on the wrong side of the pivot.

        # if you need to find the 3rd tallest person in a room of 100 people, you don't need to arrange all 100 people in height order. 
        # You just need to ensure that exactly 2 people are taller than your answer, and everyone else is shorter or equal.

        k = len(nums) - k

        def quickSelect(l, r):
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if p > k:
                return quickSelect(l, p - 1)
            elif p < k:
                return quickSelect(p + 1, r)
            else:
                return nums[p]

        return quickSelect(0, len(nums) - 1)




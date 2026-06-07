class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # 每次都需要拿到 当前最大的两个值，max-heap
        # 注意heapq是最小堆，只会把最小的数放在堆顶，heapify_max
        

        # 用取反来找
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            # 变成正数
            y = -heapq.heappop(max_heap)
            x = -heapq.heappop(max_heap)
            if x != y:
                new_stone = y - x
                # 变回负数，放进堆里
                heapq.heappush(max_heap, -new_stone)


        if max_heap:
            return -max_heap[0]
        else:
            return 0
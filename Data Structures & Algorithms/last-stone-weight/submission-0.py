class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # 每次都需要拿到 当前最大的两个值，max-heap
        # 注意heapq是最小堆，只会把最小的数放在堆顶，heapify_max
        heapq.heapify_max(stones)

        while len(stones) > 1:
            y = heapq.heappop_max(stones)
            x = heapq.heappop_max(stones)

            if x != y:
                new_stone = y - x
                heapq.heappush_max(stones, new_stone)

        if stones:
            return stones[0]
        else:
            return 0
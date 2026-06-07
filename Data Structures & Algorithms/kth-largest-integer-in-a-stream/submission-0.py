class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        
        # 1. 把列表原地转化为堆 (O(N))
        heapq.heapify(self.heap)
        
        # 2. 如果堆里的元素太多，就一直把最小的踢出去
        # 直到只剩下 k 个元素 (保留最大的 k 个)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        # 1. 新人进堆
        heapq.heappush(self.heap, val)
        
        # 2. 此时如果超员了 (有 k+1 个)，把最弱的踢出去
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
            
        # 3. 现在的堆顶，就是这 k 个牛人里垫底的，也就是第 k 大
        return self.heap[0]
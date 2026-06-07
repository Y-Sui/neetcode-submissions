class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 搜索空间，最小值：koko至少每个小时吃一根香蕉
        # 最大值：最极端情况koko必须在h小时吃完，而h可能等于piles的长度，即每堆一小时吃完
        l, r = 1, max(piles)
        res = r
        while l <= r:
            mid = l + (r - l) // 2
            
            totalTime = 0
            for p in piles:
                # 向上取整的整除，3根香蕉，一小时2根，需要1.5小时，但向上取整，需要2h
                totalTime += math.ceil(float(p) / mid)

            if totalTime <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 最优解，bucket sort
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)


        # create bucket O(N) space
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in count.items():
            buckets[freq].append(num)

        res = []
        for i in range(len(nums), 0, -1):
            if buckets[i]:
                for num in buckets[i]:
                    res.append(num)
                    if len(res) == k:
                        return res

        return res
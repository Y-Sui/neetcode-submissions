class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 最优解，bucket sort
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        # count = {
        #     "1": 1,
        #     "2": 2,
        #     "3", 3
        # }

        # create bucket O(N) space, store the 
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in count.items():
            buckets[freq].append(num)
        
        # index of buckets refers to the frequency, and the value list refers to the number fit the condition (has that frequency)
        # buckets = [
        #     [0],
        #     [1],
        #     [2],
        #     [3],
        #     [0],
        #     [0],
        #     [0]
        # ]

        res = []
        for i in range(len(nums), 0, -1):
            if buckets[i]:
                for num in buckets[i]:
                    res.append(num)
                    if len(res) == k:
                        return res

        return res
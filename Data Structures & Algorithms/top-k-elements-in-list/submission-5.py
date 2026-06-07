class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # key is the num, value is the frequency; e.g., {"1": 1, "2": 2, "3": 3}
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        # one way is to do sorting, O(nlogn)
        sorted_num = sorted(count.items(), key=lambda x: x[1])
        res = []

        while len(res) < k:
            res.append(sorted_num.pop()[0])

        return res
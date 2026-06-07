class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # key is the num, value is the frequency; e.g., {"1": 1, "2": 2, "3": 3}
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        # sacrifice space to acheive time efficiency
        # [
        #     [], []
        # ]
        # the index is the frequency, the value list is a list of number whcih number has this frequency
        freq_list = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            freq_list[freq].append(num)

        res = []
        for i in range(len(nums), 0, -1):
            if freq_list[i]:
                for num in freq_list[i]:
                    res.append(num)
                    if len(res) == k:
                        return res

        return res
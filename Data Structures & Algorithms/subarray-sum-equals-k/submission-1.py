class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # key is the value of prefix_sum, value is the count number
        prefix_sum_count = defaultdict(int)
        prefix_sum_count[0] = 1
        curr_sum = 0
        res = 0
        for num in nums:
            curr_sum += num
            # curr_sum - previous_prefix_sum = k 
            res += prefix_sum_count[curr_sum - k] # count 
            prefix_sum_count[curr_sum] += 1

        return res
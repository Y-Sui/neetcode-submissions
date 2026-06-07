class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return 0

        # 2. 初始化
        # res 记录全局见过的最大值
        # cur_max 记录以当前位置结尾的最大积
        # cur_min 记录以当前位置结尾的最小积
        res = nums[0]
        cur_max = nums[0]
        cur_min = nums[0]

        # 3. iterate from index 1
        for i in range(1, len(nums)):
            num = nums[i]

            # 
            prev_max = cur_max

            # 核心状态转移
            cur_max = max(num, prev_max * num, cur_min * num)
            cur_min = min(num, prev_max * num, cur_min * num)

            # 更新全局结果
            res = max(res, cur_max)

        return res

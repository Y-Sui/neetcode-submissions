class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        # 1. 处理 k，防止 k 越界
        #    (例如 n=7, k=10 和 k=3 效果一样)
        k = k % n
        
        if k == 0:
            # 如果 k 是 n 的倍数，不需要旋转
            return

        # 2. 定义一个辅助函数来反转数组的
        #    从 [start, end] 闭区间的元素
        def reverse(arr: list[int], start: int, end: int):
            while start < end:
                # 交换元素
                arr[start], arr[end] = arr[end], arr[start]
                # 移动指针
                start += 1
                end -= 1

        # 3. 执行三次反转
        
        # 步骤 1: 反转整个数组 (索引 0 到 n-1)
        reverse(nums, 0, n - 1)
        
        # 步骤 2: 反转前 k 个元素 (索引 0 到 k-1)
        reverse(nums, 0, k - 1)
        
        # 步骤 3: 反转剩余的 n-k 个元素 (索引 k 到 n-1)
        reverse(nums, k, n - 1)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # using hashset
        # 1. 将所有数放入hashset
        numSet = set(nums)
        longest = 0

        # 2. 遍历nums数组
        for num in numSet:
            # 3. 关键：只从 序列的起点开始计算，只有num-1不在列表中时候才开始
            if (num-1) not in numSet:
                currNum = num
                currLength = 1

                # 4. 循环查找序列的长度
                while (currNum + 1) in numSet:
                    currNum += 1
                    currLength += 1

                longest = max(currLength, longest)

            # 不是起点，先跳过
            else:
                continue

        return longest
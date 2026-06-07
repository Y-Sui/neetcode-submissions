class Solution:
    def trap(self, height: List[int]) -> int:
        # 在i位置能存储的水 = min（i左边的最高墙，i右边的最高墙） - i自己的高度
        # water[i] = max(0, min(max_left[i], max_right[i]) - height[i])
        # 总的水量等于全部加起来

        if not height:
            return 0

        left, right = 0, len(height) - 1
        max_left, max_right = 0, 0
        total_water = 0

        while left < right:
            if height[left] <= height[right]:
                # 左边是短板, 处理left指针
                if height[left] >= max_left:
                    # 发现一个新的，更高的柱子
                    max_left = height[left]
                else:
                    # 这根柱子比max left矮，可以存水
                    # 水量 = （左墙 - 自己的高度）
                    total_water += (max_left - height[left])
                left += 1

            else:
                # 右边是短板，处理right指针
                if height[right] >= max_right:
                    max_right = height[right]
                else:
                    total_water += (max_right - height[right])

                right -= 1

        return total_water
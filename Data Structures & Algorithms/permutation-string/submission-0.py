class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # using sliding window
        len1, len2 = len(s1), len(s2)
        
        # 1. 边缘情况：如果 s1 比 s2 长，s2 不可能包含 s1 的排列
        if len1 > len2:
            return False

        # 2. 初始化两个频率数组，大小 26 (a-z)
        s1_counts = [0] * 26
        window_counts = [0] * 26

        # 辅助函数：将 'a'->0, 'b'->1, ...
        def char_index(c):
            return ord(c) - ord('a')

        # 3. 填充 s1_counts 和 s2 的第一个窗口 (window_counts)
        for i in range(len1):
            s1_counts[char_index(s1[i])] += 1
            window_counts[char_index(s2[i])] += 1
        
        # 4. 检查第一个窗口是否匹配
        if s1_counts == window_counts:
            return True

        # 5. 滑动窗口
        # i 代表新进入窗口的字符 (right)
        # i - len1 代表刚离开窗口的字符 (left_prev)
        for i in range(len1, len2):
            
            # 6. 更新窗口：添加新字符，移除旧字符
            # 添加右侧新字符
            window_counts[char_index(s2[i])] += 1
            # 移除左侧旧字符
            window_counts[char_index(s2[i - len1])] -= 1
            
            # 7. 检查当前窗口是否匹配
            if s1_counts == window_counts:
                return True

        # 8. 遍历结束，没有找到匹配
        return False
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 挺难的，首先理解一下题目意思，results是说 再过多少天 气温会比今天高
        res = [0] * len(temperatures) # 用一个等长的array来记录
        stack = [] # 用于记录还没找到更高温度那一天的索引

        for curr_day, curr_temp in enumerate(temperatures):
            while stack and curr_temp > temperatures[stack[-1]]:
                prev_day = stack.pop() # 如果满足条件，说明prev_day这天已经找到答案了，可以从stack剔除
                res[prev_day] = curr_day - prev_day

            stack.append(curr_day)

        return res
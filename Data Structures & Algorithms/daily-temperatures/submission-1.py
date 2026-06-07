class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # edge cases
        if not temperatures:
            return []

        res = [0] * len(temperatures)
        stack = [] # store the index of the day

        # temperatures = [30,38,30,36,35,40,28]
        for day, temperature in enumerate(temperatures):
            # stack = [0], day is 1, temperature is 38, 38 > 30
            while stack and temperature > temperatures[stack[-1]]:
                # previous_day = 0, curr_day = 1, res[0] =1
                previous_day = stack.pop()
                res[previous_day] = day - previous_day

            stack.append(day)

        return res
        
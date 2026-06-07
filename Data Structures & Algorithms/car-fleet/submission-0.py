class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # (position, speed)
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(key=lambda x: x[0], reverse=True) # 距离target近的排在前面

        stack = []
        for p, s in pair:
            time = (target - p) / s
            stack.append(time)

            # 判断是否合并，后来的车的时间 <= 先来的车，说明后车比前车快，会被挡住，成为一个车队
            if len(stack) >=2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
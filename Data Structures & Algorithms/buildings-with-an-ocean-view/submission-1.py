class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = [] # store the buildings that still can see the ocean

        for i, height in enumerate(heights):
            while stack and heights[stack[-1]] <= height:
                stack.pop()

            stack.append(i)

        return stack
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        res = []

        for i in range(n):
            flag = True
            for j in range(i+1, n):
                if heights[i] <= heights[j]:
                    flag = False
                    break

            if flag:
                res.append(i)

        return res
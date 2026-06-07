class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if not matrix:
            return res

        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # left -> right 沿着上边界top走
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1

            # top -> bottom
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1

            # right -> left:
            # 【关键判断】：因为 top 刚才加过了，这里要确认是否越界
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1

            # bottom -> top:
            # 【关键判断】：因为 right 刚才减过了，这里要确认是否越界
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1

        return res
            
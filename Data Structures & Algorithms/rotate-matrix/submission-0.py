class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # 旋转是个常见的操作，需要原地进行，可以利用几何变换的组合
        # 顺时针旋转90度，等价=（1）transpose，沿着主对角线（左上到右下）翻转；（2）reverse rows，每一行左右颠倒
        n = len(matrix)

        # step 1: transpose 沿对角线翻转
        for i in range(n):
            # 注意j从i+1开始，这样只遍历对角线右上方的内容，避免重复交换
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
        # step 2: reverse each row
        for i in range(n):
            # matrix[i].reverse() 

            left, right = 0, n-1
            while left < right:
                matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
                right -= 1
                left += 1
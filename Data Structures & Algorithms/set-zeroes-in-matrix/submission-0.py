class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        rows, cols = len(matrix), len(matrix[0])

        # 1. check 单独检查第一行和第一列是否包含 0
        first_row_has_zero, first_col_has_zero = False, False

        for c in range(cols):
            if matrix[0][c] == 0:
                first_row_has_zero = True
                break

        for r in range(rows):
            if matrix[r][0] == 0:
                first_col_has_zero = True
                break

        # 2. flag
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        # 3. 根据标志位，将内部置零
        for r in range(1, rows):
            for c in range(1, cols):
                # 只要行首或列首有一个是 0，这个位置就该是 0
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        # 4. 最后处理第一行和第一列
        if first_row_has_zero:
            for c in range(cols):
                matrix[0][c] = 0

        if first_col_has_zero:
            for r in range(rows):
                matrix[r][0] = 0
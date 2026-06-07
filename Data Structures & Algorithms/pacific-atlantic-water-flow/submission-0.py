class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # graph traversal 的过程，
        # 这道题不是很好理解，实际上是说水往低处流（或者平处流）。
        # 也就是说，如果你在格子 A，你想流到格子 B，那么 A 的高度必须大于等于 B 的高度 (Height[A] >= Height[B])。
            ##一旦流到了矩阵的边缘，就算流入了大海。



        # 思路是
        # 太平洋队 (Pacific)：从矩阵的 左边界 和 上边界 出发，向内陆“爬山”。凡是能爬到的点，说明这些点也能流回太平洋。用一个集合 pacific_reachable 记录。
        # 大西洋队 (Atlantic)：从矩阵的 右边界 和 下边界 出发，向内陆“爬山”。凡是能爬到的点，都记录在 atlantic_reachable 里。
        # 交集 (Intersection)：既在太平洋集合里，又在大西洋集合里的点，就是我们要找的答案。

        if not heights:
            return []

        rows, cols = len(heights), len(heights[0])
        pac_visited = set()
        atl_visited = set()

        # prev_height: 上一个点的高度 (我们需要 当前 >= 上一个 才能流过来)
        def dfs(r, c, visited, prev_height):
            if ((r, c) in visited or 
                r < 0 or
                c < 0 or
                r >= rows or
                c >= cols or
                heights[r][c] < prev_height):
                return

            visited.add((r, c))

            dfs(r+1, c, visited, heights[r][c])
            dfs(r-1, c, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])

        for c in range(cols):
            # 第一行 -> 属于太平洋
            dfs(0, c, pac_visited, heights[0][c])
            # 最后一行 -> 属于大西洋
            dfs(rows-1, c, atl_visited, heights[rows-1][c])

        for r in range(rows):
            # 第一列 -> 属于太平洋
            dfs(r, 0, pac_visited, heights[r][0])
            # 最后一列 -> 属于大西洋
            dfs(r, cols-1, atl_visited, heights[r][cols-1])

        # 取交集
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac_visited and (r, c) in atl_visited:
                    res.append([r, c])

        return res
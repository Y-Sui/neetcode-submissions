class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_area = 0

        def bfs(r, c):
            queue = deque([(r, c)])
            grid[r][c] = 0
            area = 0
            while queue:
                curr_r, curr_c = queue.popleft()
                area += 1
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in directions:
                    nr, nc = curr_r + dr, curr_c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        queue.append((nr, nc))
                        grid[nr][nc] = 0

            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    curr_area = bfs(r, c)
                    max_area = max(curr_area, max_area)


        return max_area
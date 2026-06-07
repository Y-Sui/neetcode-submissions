class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # edge cases
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        # shortest path
        queue = collections.deque([(0, 0, 1)]) # (row idx, col idx, curr_step_num)
        
        # 避免走回头路，走过了就直接设置为1
        grid[0][0] = 1

        # eight directions
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]

        # bfs
        while queue:
            r, c, dist = queue.popleft()

            # arrive at the right, bottom corner
            if r == n - 1 and c == n - 1:
                return dist

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    grid[nr][nc] = 1 # 标记已经访问
                    queue.append((nr, nc, dist+1))

        return -1
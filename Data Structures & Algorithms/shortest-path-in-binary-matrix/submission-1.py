class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # edge cases
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        # ****parent[(子行，子列)] = (父行，父列)
        parent = {(0, 0): None}

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
                # return dist
                # ********
                path = []
                curr = (n-1, n-1)
                while curr:
                    path.append(curr)
                    curr = parent[curr]
                return len(path[::-1]) # 因为是倒着找的，所以需要反转列表

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    grid[nr][nc] = 1 # 标记已经访问
                    queue.append((nr, nc, dist+1))

                    # ***********
                    # 把邻居加入队列的同时，记录他是从(r,c)来的
                    parent[(nr, nc)] = (r, c)

        return -1
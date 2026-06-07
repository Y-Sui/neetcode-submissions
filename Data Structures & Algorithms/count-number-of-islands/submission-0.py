class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        is_lands = 0
        visited = set()

        def dfs(r, c):
            if (r < 0 or
                c < 0 or 
                r >= rows or 
                c >= cols or
                grid[r][c] == "0" or
                (r, c) in visited):
                return 

            visited.add((r,c))
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
            # visited.remove((r, c)), 注意这道题不应该是回溯

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    is_lands += 1

        return is_lands
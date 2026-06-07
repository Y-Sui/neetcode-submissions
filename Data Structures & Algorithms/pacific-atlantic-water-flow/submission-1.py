class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        valid_p_set = set()
        valid_a_set = set()

        pacific_queue = deque()
        atlantic_queue = deque()

        for c in range(cols):
            pacific_queue.append((0, c))
            atlantic_queue.append((rows-1, c))

        for r in range(rows):
            pacific_queue.append((r, 0))
            atlantic_queue.append((r, cols-1))

        def bfs(queue, valid_set):
            for r, c in queue:
                valid_set.add((r, c))
            directions = [(1,0), (-1, 0), (0, 1), (0, -1)]
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in valid_set and heights[nr][nc] >= heights[r][c]:
                        valid_set.add((nr, nc))
                        queue.append((nr, nc))

        bfs(pacific_queue, valid_p_set)
        bfs(atlantic_queue, valid_a_set)

        return [[r, c] for r, c in valid_p_set & valid_a_set]
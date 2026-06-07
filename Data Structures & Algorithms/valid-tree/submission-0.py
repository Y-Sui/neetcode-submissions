class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        在图论中，要判断一个无向图是不是一棵“树”，必须同时满足两个核心条件：

没有环 (No Cycles)：不能绕一圈回到原点。

全连通 (Fully Connected)：所有节点都必须连在一起，不能有孤岛。
        """


        # 0. 快速判断：树的边数必须是 n - 1
        # 这一步可以省掉，但写了能剪枝
        if len(edges) != n - 1:
            return False

        # 1. 建图 (邻接表)
        adj = {i: [] for i in range(n)}
        # undirected graph
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()

        # DFS 函数
        # node: 当前节点
        # prev: 上一个节点 (父节点)，防止我们回头看父节点误报为环
        def dfs(node, prev):
            # 标记当前节点
            visited.add(node)
            
            for neighbor in adj[node]:
                # 这一步很关键！因为是无向图，A连B，B也连A
                # 我们从A走到B，B肯定会看到A。
                # 如果看到的邻居是刚才过来的“爸爸”，直接跳过，不算环
                if neighbor == prev:
                    continue
                
                # 如果看到的邻居已经被访问过了（且不是爸爸）
                # 说明绕了一圈回来了 -> 有环！
                if neighbor in visited:
                    return False
                
                # 递归下去，如果下面发现有环，立刻向上汇报 False
                if not dfs(neighbor, node):
                    return False
            
            return True

        # 2. 从 0 开始检查
        # 如果 dfs 返回 False (有环)，或者 visited 数量不够 (不连通)
        if not dfs(0, -1):
            return False
        
        return len(visited) == n
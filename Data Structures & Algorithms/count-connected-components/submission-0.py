class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # 1. 构建邻接表
        adj = [[] for _ in range(n)]
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visited = set()
        count = 0
        
        def dfs(node):
            # 标记当前节点
            visited.add(node)
            # 遍历它的邻居
            for neighbor in adj[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        # 2. 遍历所有节点
        for i in range(n):
            if i not in visited:
                # 发现未访问节点，说明发现了新的连通分量
                count += 1
                dfs(i) # 把这一整串都标记了
                
        return count
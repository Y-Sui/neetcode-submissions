"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {} # key: original node; value: cloned node

        def dfs(node):
            if not node:
                return None
            if node in visited:
                return visited[node]

            copied_node = Node(node.val, [])
            visited[node] = copied_node # add to the dict
            for neighbor in node.neighbors:
                copied_node.neighbors.append(dfs(neighbor))
            return copied_node

        return dfs(node) if node else None
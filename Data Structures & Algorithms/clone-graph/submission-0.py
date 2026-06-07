"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        # 注意一下题目，graph是一个无向图，也就是说像example 1的情况下
        # 当我已经复制了1指向2，此时3也只能指向1链接的那个2，而不能重新创建一个，所以要使用hash map来记录
        old_to_new = {} # key 原来的node，value，克隆后的node

        def dfs(node):
            if node in old_to_new:
                return old_to_new[node]

            copy = Node(node.val)
            old_to_new[node] = copy

            # 递归克隆所有的邻居
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy
        
        return dfs(node) if node else None
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # DFS (深度优先搜索) + 状态传递
        # 状态传递记录 最大值

        def dfs(node, max_val):
            if not node:
                return 0

            # 1. check whether the current node is "good node"
            res = 0
            if node.val >= max_val:
                res = 1
            else:
                res = 0 

            # 2. update the max value
            new_max = max(max_val, node.val)

            # 3. iterate
            res += dfs(node.left, new_max)
            res += dfs(node.right, new_max)

            return res
        
        # init，max_val is the root.val
        return dfs(root, root.val)
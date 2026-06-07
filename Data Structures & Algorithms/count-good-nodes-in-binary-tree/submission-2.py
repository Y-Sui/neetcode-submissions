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
            
            # 只需要判断对于当前节点，是不是一个good node
            is_good = 1 if node.val >= max_val else 0

            next_max = max(max_val, node.val)
            
            return is_good + dfs(node.left, next_max) + dfs(node.right, next_max)
        
        # init，max_val is the root.val
        return dfs(root, root.val)
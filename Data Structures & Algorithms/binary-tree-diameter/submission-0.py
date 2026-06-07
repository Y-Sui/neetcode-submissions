# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # 经过某个节点的最长路径 = 该节点的左子树深度 + 该节点的右子树深度。
        
        self.res = 0

        def dfs(root):
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            # 核心逻辑，计算经过当前node的长度，左臂长+右臂长，如果这个长度比之前记录的self.ans大，则更新他
            self.res = max(self.res, left + right)

            # 标准的maxDepth返回逻辑
            return 1 + max(left, right)

        dfs(root)
        return self.res
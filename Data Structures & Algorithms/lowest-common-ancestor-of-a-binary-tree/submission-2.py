# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # post traversal

        # if root is None, we're at leaf node, return None;
        # if root equals p or q, found our target node, return it 
        if root in (None, p, q):
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # decision logic
        # if left and right are not-null. it means current node is LCA
        # if only left is not-null
        # if only rigt is not-null
        # if both left and right are null. return None, neither node was found in the subtree
        return root if (left and right) else (left or right)
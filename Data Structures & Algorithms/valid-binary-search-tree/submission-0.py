# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(node: Optional[TreeNode], left_val: float, right_val: float):
            if not node:
                return True
            if not (left_val < node.val < right_val):
                return False
            return valid(node.left, left_val, node.val) and valid(node.right, node.val, right_val)

        return valid(root, float("-inf"), float("inf"))
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # 任务B：在森林里寻找“匹配点” (isSubtree)   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # 任务A：比较两棵树是否完全相同 (sameTree)
        def sameTree(root, subRoot):
            if not root and not subRoot:
                return True
            if root and subRoot and root.val == subRoot.val:
                return (sameTree(root.left, subRoot.left) and sameTree(root.right, subRoot.right))
            else:
                return False
        
        if not subRoot:
            return True
        if not root:
            return False

        # 判断当前位置匹配吗，如果现在这棵树和子树相同，则返回
        if sameTree(root, subRoot):
            return True
        # 如果不匹配，看看当前树的子树有没有匹配的，or，左右子树任意一个匹配，返回True
        else:
            return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

        
        
            
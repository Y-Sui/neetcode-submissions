# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # hashmap
        # we want to know the index of root node in the inorder list in O(1) time complexity
        index_map = {val: i for i, val in enumerate(inorder)}

        # -> the node we want to process in the preorder, which is the root node
        self.pre_idx = 0

        def helper(l, r):
            if l > r:
                return None
            
            # find the root node
            root_val = preorder[self.pre_idx]
            root = TreeNode(root_val)

            # process next node from preorder
            self.pre_idx += 1

            # find the index of the root node in the inorder list
            split_idx = index_map[root_val]

            # 构建左子树
            root.left = helper(l, split_idx - 1)
            # 右子树
            root.right = helper(split_idx + 1, r)

            return root

        return helper(0, len(inorder) -1)








# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# https://algo.monster/liteproblems/314

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # traversal the entire tree, either BFS or DFS
        # DFS, track information (depth, offset)
        # collecting nodes with (offset, depth) during DFS, later sort it and group them

        # root, column/offset = 0, go left, column/offset - 1, go right, column/offset + 1; depth + 1
        # track (1) column position (offset): which vertical column the node belongs to
        # track (2) depth (row): How far down the node is from the root

        # dictionary/hashmap where the key is the column offset, and the value is a list of (depth, node_value) pairs.

        def dfs(root, depth, offset):
            if root is None:
                return
            column_values[offset].append((depth, root.val))
            dfs(root.left, depth+1, offset-1)
            dfs(root.right, depth+1, offset+1)

        
        column_values = defaultdict(list) # key is the column index, value is the list of (depth, node_value) tuples
        dfs(root, 0, 0)

        res = []
        for column_index in sorted(column_values.keys()):
            nodes_in_column = column_values[column_index]
            nodes_in_column.sort(key=lambda x: x[0])

            res.append([node_val for depth, node_val in nodes_in_column])

        return res




        # time: O(nlogn)
        # space: O(n)
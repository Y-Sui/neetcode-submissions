"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # 变成链表的写法了，找交点
        # A=ptr1到LCA的距离；B=ptr2到LCA的距离
        # ptr1的总长度是A+C，ptr2的总长度是B+C
        ptr1, ptr2 = p, q
        while ptr1 != ptr2:
            ptr1 = ptr1.parent if ptr1 else q
            ptr2 = ptr2.parent if ptr2 else p

        return ptr1
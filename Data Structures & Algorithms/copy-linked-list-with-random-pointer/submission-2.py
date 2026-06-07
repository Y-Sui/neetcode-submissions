"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # store the map between old node and the new node
        # key is the original node, and the value is the new copied node
        reference_map = {None: None}

        curr = head
        while curr:
            new_node = Node(curr.val)
            reference_map[curr] = new_node
            curr = curr.next

        curr = head
        while curr:
            new_node = reference_map[curr]
            new_node.next = reference_map[curr.next]
            new_node.random = reference_map[curr.random]
            curr = curr.next

        return reference_map[head]

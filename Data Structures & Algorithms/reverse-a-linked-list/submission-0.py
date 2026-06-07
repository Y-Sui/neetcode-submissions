# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head # prev 记录翻转后的linkedlist，curr指向正在处理的节点

        while curr:
            temp = curr.next # 记录下下一个需要处理的节点
            curr.next = prev # 断开当前节点和下一个需要处理的节点，把当前节点next连接到翻转列表上，现在prev变成0 -> None
            prev = curr # prev现在 变成 0 -> None 的0了
            curr = temp # curr变成 1 -> 2 -> 3

        return prev
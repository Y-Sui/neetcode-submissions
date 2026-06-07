# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        # 步骤 1: 找到中间节点，并断开链表
        l1 = head
        l2 = self.split_list(head)
        
        # 步骤 2: 反转后半部分链表
        l2_reversed = self.reverse_list(l2)
        
        # 步骤 3: 合并两个链表
        self.merge_lists(l1, l2_reversed)

    def split_list(self, head: ListNode) -> Optional[ListNode]:
        """
        使用快慢指针找到中点，并断开链表。
        返回后半部分的头节点。
        """
        slow = head
        fast = head
        
        # 我们让 slow 停在前半部分的 *最后一个* 节点
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        # 此时 slow 是前半部分的尾巴
        # slow.next 是后半部分的开头
        second_head = slow.next
        
        # 断开
        slow.next = None
        
        return second_head

    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        (这就是你上一题的代码)
        反转一个链表并返回新的头节点。
        """
        prev = None
        curr = head
        
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
            
        return prev

    def merge_lists(self, l1: ListNode, l2: Optional[ListNode]):
        """
        "拉链式"交错合并两个链表。
        l1 是前半部分，l2 是反转后的后半部分。
        """
        while l2:
            # 1. 保存 l1 和 l2 的“下一个”
            l1_next = l1.next
            l2_next = l2.next
            
            # 2. l1 -> l2
            l1.next = l2
            
            # 3. l2 -> l1_next
            l2.next = l1_next
            
            # 4. 移动指针到下一次迭代的位置
            l1 = l1_next
            l2 = l2_next
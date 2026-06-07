# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy # 上一组的结尾

        while True:
            # 1. 从groupPrev开始往后数k个
            kth = self.getKth(groupPrev, k)
            # 如果剩余节点不足 k 个，则不反转，直接结束。
            if not kth:
                break

            # 2. 记录这一组的边界
            groupNext = kth.next # 下一组的开头
            curr = groupPrev.next # 这一组的原本的头

            # 3. 反转
            prev = groupNext
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp

        return dummy.next


    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
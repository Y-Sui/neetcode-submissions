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
        # 边界情况：如果原始链表为空，返回 None
        if not head:
            return None
            
        # 步骤 1: 创建哈希表
        # key: 原始节点, value: 深度复制的新节点
        # 我们提前加入 {None: None} 来优雅地处理
        # 那些 next 或 random 指向 null 的情况
        mapping = {None: None}

        # ----------------------------------------------------
        # 第一次遍历: 只创建所有的新节点，并填充哈希表
        # ----------------------------------------------------
        curr = head
        while curr:
            # 复制节点，只复制 val
            new_node = Node(curr.val)
            
            # 建立 "旧 -> 新" 的映射
            mapping[curr] = new_node
            
            # 移动到下一个原始节点
            curr = curr.next
            
        # ----------------------------------------------------
        # 第二次遍历: 连接所有新节点的 next 和 random 指针
        # ----------------------------------------------------
        curr = head
        while curr:
            # 1. 找到当前旧节点 "curr" 对应的 "新节点"
            new_node = mapping[curr]
            
            # 2. 找到 "curr.next" 对应的 "新节点"
            #    (如果 curr.next 是 None, mapping[None] 会返回 None)
            new_node.next = mapping[curr.next]
            
            # 3. 找到 "curr.random" 对应的 "新节点"
            #    (如果 curr.random 是 None, mapping[None] 会返回 None)
            new_node.random = mapping[curr.random]
            
            # 移动到下一个原始节点
            curr = curr.next
            
        # ----------------------------------------------------
        # 步骤 3: 返回
        # ----------------------------------------------------
        # mapping[head] 就是新链表的头节点
        return mapping[head]
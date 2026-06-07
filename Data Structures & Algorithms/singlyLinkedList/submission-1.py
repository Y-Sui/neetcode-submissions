
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
        
class LinkedList:
    def __init__(self):
        # Init the list with a 'dummy' node which makes 
        # removing a node from the beginning of list easier.
        self.head = ListNode(-1)
        self.tail = self.head
        
    def get(self, index: int) -> int:
        """
        will return the value of the ith node (0-indexed). If the index is out of bounds, return -1.
        """
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
            
        return -1
        
    def insertHead(self, val:int) -> None:
        """
        will insert a node with val at the head of the list.
        """
        newNode = ListNode(val)
        if not self.head.next:
            self.head.next = newNode
            self.tail = newNode
        else:
            newNode.next = self.head.next
            self.head.next = newNode
    
    def insertTail(self, val) -> None:
        """
        will insert a node with val at the tail of the list.
        """
        self.tail.next = ListNode(val)
        self.tail = self.tail.next
        
    def remove(self, index) -> bool:
        """
        will remove the ith node (0-indexed). If the index is out of bounds, return false, otherwise return true.
        """
        i = 0
        curr = self.head
        while i < index and curr:
            i+=1
            curr = curr.next
            
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False
            
    def getValues(self) -> List[int]:
        """
        return an array of all the values in the linked list, ordered from head to tail.
        """
        curr = self.head.next
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res
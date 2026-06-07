"""


Design a Double-ended Queue class.

Your Deque class should support the following operations:

Deque() will initialize an empty queue.
bool isEmpty() will return whether the queue is empty or not.
void append(int value) will insert value at the end of the queue.
void appendleft(int val) will insert value at the beginning of the queue.
int pop() will remove and return the value at the end of the queue. If the queue is empty, return -1.
int popleft() will remove and return the value at the beginning of the queue. If the queue is empty, return -1.
Note: You should implement each operation in O(1) time complexity.

"""

# Doubly linked list node
class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head


    def isEmpty(self) -> bool:
        return self.head.next == self.tail
        

    def append(self, value: int) -> None:
        new_node = Node(value)
        last_node = self.tail.prev
        
        last_node.next = new_node
        new_node.prev = last_node
        new_node.next = self.tail
        self.tail.prev = new_node
        

    def appendleft(self, value: int) -> None:
        new_node = Node(value)
        first_node = self.head.next

        self.head.next = new_node
        new_node.prev = self.head
        new_node.next = first_node
        first_node.prev = new_node


    def pop(self) -> int:
        if self.isEmpty():
            return -1
        
        last_node = self.tail.prev
        value = last_node.value
        prev_node = last_node.prev
        
        prev_node.next = self.tail
        self.tail.prev = prev_node
        
        return value

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        
        first_node = self.head.next
        value = first_node.value
        next_node = first_node.next
        
        self.head.next = next_node
        next_node.prev = self.head
        
        return value

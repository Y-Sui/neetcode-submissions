class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # map key to node
        
        # initialize the double linked list
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def _remove_node_from_list(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def _insert_to_tail(self, node):
        # the node is the most recent used
        prev, nxt = self.right.prev, self.right
        prev.next = node
        node.prev = prev
        node.next = nxt
        nxt.prev = node

    def get(self, key: int) -> int:
        # get also means one action to the linked list, so we have to move the node to the right side
        if key in self.cache:
            self._remove_node_from_list(self.cache[key])
            self._insert_to_tail(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        # first check whether the key exists, if so, remove it from the linked list (update)
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove_node_from_list(self.cache[key])
            self._insert_to_tail(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self._insert_to_tail(node)
            
            # only if add new node, we need to check the capacity
            if len(self.cache) > self.cap:
                # remove the lru node
                lru = self.left.next
                self._remove_node_from_list(lru)
                del self.cache[lru.key]
        

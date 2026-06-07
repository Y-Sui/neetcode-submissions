# using bst to implement sets and maps, to allow O(logn) time for insertion, deletion and search operations

# https://neetcode.io/problems/binarySearchTree


class TreeNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    # will initialize an binary search tree map.    
    def __init__(self):
        self.root = None
        

    def insert(self, key: int, val: int) -> None:
        """
        insert当作public func给用户调用，具体的递归方法用私有函数实现
        公共方法：向树中插入一个 (key, val) 对。
        如果 key 已存在，则更新其 val。
        """
        self.root = self._insert(self.root, key, val)
        
    def _insert(self, root: TreeNode, key: int, val: int):
        """
        私有辅助函数：
        在以 'node' 为根的子树中递归地插入 (key, val)。
        返回这棵子树的新根节点。
        """
        if not root:
            return TreeNode(key, val)
        
        if key < root.key:
            root.left = self._insert(root.left, key, val)
        elif key > root.key:
            root.right = self._insert(root.right, key, val)
        else:
            # key exist, 按照map的约定，更新value
            root.val = val
        
        return root

    def get(self, key: int) -> int:
        """
        return the value mapped with the key. If the key is not present in the tree, return -1.
        """
        return self._get(self.root, key)
        
    def _get(self, root: TreeNode, key: int) -> int:
        if not root:
            return -1
        
        if key == root.key:
            return root.val
        
        if key < root.key:
            return self._get(root.left, key)
        else:
            return self._get(root.right, key)


    def getMin(self) -> int:
        if not self.root:
            return -1
        
        curr = self.root
        while curr and curr.left:
            curr = curr.left
            
        return curr.val

    def getMax(self) -> int:
        if not self.root:
            return -1
        
        curr = self.root
        while curr and curr.right:
            curr = curr.right
            
        return curr.val


    def remove(self, key: int) -> None:
        """
        remove the key-value pair with the given key from the tree.
        """
        self.root = self._remove(self.root, key)
        
        
    def _remove(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        
        if key < root.key:
            root.left = self._remove(root.left, key)
            
        elif key > root.key:
            root.right = self._remove(root.right, key)
            
        else:
            # key == root.key
            if not root.left:
                return root.right
            
            elif not root.right:
                return root.left
            
            else:
                successor = root.right
                while successor and successor.left:
                    successor = successor.left
                    
                root.key = successor.key
                root.val = successor.val
                root.right = self._remove(root.right, successor.key)
                
        return root
        

    def getInorderKeys(self) -> List[int]:
        """
        return an array of the keys in the tree in ascending order.
        """
        
        keys_list = []
        self._inorder(self.root, keys_list)
        return keys_list
        
    
    def _inorder(self, root: TreeNode, keys_list: list):
        if not root:
            return
        
        self._inorder(root.left, keys_list)
        keys_list.append(root.key)
        self._inorder(root.right, keys_list)

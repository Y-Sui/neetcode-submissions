class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_word = True

    def search(self, word: str) -> bool:
        # 注意题目要求.可以当作通配符，代替任何字母，所以需要设计dfs
        def dfs(node, index):
            if index == len(word):
                return node.is_word
            char = word[index]

            # case 1, 通配符 .
            if char == ".":
                for child in node.children.values():
                    # 只要有一条路能走得通
                    if dfs(child, index + 1):
                        return True
                return False

            # case 2, 普通字母
            else:
                if char not in node.children:
                    return False
                return dfs(node.children[char], index + 1)

        return dfs(self.root, 0)
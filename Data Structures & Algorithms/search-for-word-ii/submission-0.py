class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        # 应该先把words添加到trie中，然后遍历整个board，看是不是存在
        root = TrieNode()
        for w in words:
            root.addWord(w)

        rows, cols = len(board), len(board[0])
        res = set() # 最后的返回时存在的word
        visited = set()

        def dfs(r, c, node, word):
            if (r < 0 or 
                c < 0 or 
                r >= rows or 
                c >= cols or 
                ((r, c) in visited) or 
                board[r][c] not in node.children):
                return

            visited.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.is_word:
                res.add(word)

            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r, c-1, node, word)
            visited.remove((r, c))


        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")

        return list(res)


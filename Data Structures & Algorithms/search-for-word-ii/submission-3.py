class TrieNode:
    def __init__(self):
        self.children = [None]  * 26
        self.isWord = False

    def addWord(self,word):
        curr = self
        for c in word:
            index = ord(c) - ord('a')
            if curr.children[index] is None:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m,n = len(board), len(board[0])
        path = set()
        res = set()
        root = TrieNode()
        for word in words:
            root.addWord(word)

        def dfs(r,c,word,node):
            if (r < 0 or c < 0 or r >= m or c >= n or (r,c) in path):
                return
            idx = ord(board[r][c]) - ord('a')
            if node.children[idx] is None:
                return

            path.add((r,c))
            word += board[r][c]
            node = node.children[idx]
            if node.isWord:
                res.add(word)

            dfs(r + 1, c, word, node)
            dfs(r, c + 1, word, node)
            dfs(r - 1, c, word, node)
            dfs(r, c - 1, word, node)
            path.remove((r,c))
        
        for i in range(m):
            for j in range(n):
                dfs(i,j,"",root)
        
        return list(res)


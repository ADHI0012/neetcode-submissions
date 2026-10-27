class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if curr.children[idx] is None:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        curr.isWord = True

    def search(self, word: str) -> bool:
        def dfs(i, curr):
            if curr is None:
                return False
            if i == len(word):
                return curr.isWord
            
            if word[i] == '.':
                for j in range(26):
                    if curr.children[j]:
                        if dfs(i + 1, curr.children[j]):
                            return True
                return False
            else:
                idx = ord(word[i]) - ord('a')
                if curr.children[idx] is None:
                    return False
                return dfs(i + 1, curr.children[idx])

        return dfs(0, self.root)
        

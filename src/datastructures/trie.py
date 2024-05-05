class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.endWord = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
    
    def addWord(self, word: str) -> None:
        temp = self.root

        for ch in word:
            if ch in temp.children:
                temp = temp.children[ch]
            else:
                node = TrieNode()
                temp.children[ch] = node
                temp = temp.children[ch]
        temp.endWord = True

    def search(self, word: str) -> None:
        temp = self.root
        for ch in word:
            if ch in temp.children:
                temp = temp.children[ch]
            else:
                return False    
        return temp.endWord
    
    def searchPrefix(self, prefix: str) -> None:
        temp = self.root
        for ch in prefix:
            if ch in temp.children:
                temp = temp.children[ch]
            else:
                return False    
        return True



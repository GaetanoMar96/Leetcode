from datastructures.trie import Trie

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        m, n = len(board), len(board[0])
        visited = set()
        def bt(i, j, node, visited, word):
            if (i,j) in visited:
                return
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
                return #out of bounds
            if board[i][j] not in node.children:
                return
            word += board[i][j]
            node = node.children[board[i][j]]
            if node.endWord:
                res.append(word)
                node.endWord = False #avoid duplicates
                 
            visited.add((i,j))
            #check all positions
            bt(i+1, j, node, visited, word)
            bt(i-1, j, node, visited, word)
            bt(i, j+1, node, visited, word)
            bt(i, j-1, node, visited, word)
            visited.remove((i,j))

        res = []
        trie = Trie()
        for word in words:
            trie.addWord(word)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie.root.children:
                    bt(i,j,trie.root, visited, '')
                        
        return res
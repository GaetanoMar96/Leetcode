class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        visited = set()
        def dfs(i,j,k):
            if (i,j) in visited:
                return False
            visited.add((i,j))
            if k > len(word) or i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
                return False
            if k == len(word):
                return True
            #check row
            if i+1 < len(board) and word[k] == board[i+1][j]:
                if dfs(i+1, j, k+1):
                    return True 
            #check col
            if j+1 < len(board[0]) and word[k] == board[i][j+1]:
                if dfs(i, j+1, k+1):
                    return True 

            #check row back
            if i-1 >= 0 and word[k] == board[i-1][j]:
                if dfs(i-1, j, k+1):
                    return True 

            #check col back
            if j-1 >= 0 and word[k] == board[i][j-1]:
                if dfs(i, j-1, k+1):
                    return True 

            visited.remove((i,j))
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i,j,1):
                        return True
                    visited = set()
        return False

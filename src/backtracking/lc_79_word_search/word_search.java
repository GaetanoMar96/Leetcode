import java.util.*;
class Solution {

    public int lenrow;
    public int lencol;
    public Set<String> visited = new HashSet<>();
    public int length;

    public boolean exist(char[][] board, String word) {
        this.lenrow = board.length;
        this.lencol = board[0].length;
        this.length = word.length();
        
        for(int i = 0; i < lenrow; i++) {
            for(int j = 0; j < lencol; j++) {
                if (board[i][j] == word.charAt(0)) {
                    if(bt(i,j,1,board, word)) 
                        return true;
                    visited.clear();
                }
            }    
        }
        return false;
    }

    public boolean bt(int i, int j, int k, char[][] board, String word) {
        if (visited.contains(i + "," + j))
            return false;
        visited.add(i + "," + j);
        if (k > length || i < 0 || j < 0 || i >= lenrow || j >= lencol)
            return false;
        if (k == length)
            return true;
        if(i+1 < lenrow && board[i+1][j] == word.charAt(k)) {
            if(bt(i+1, j, k+1,board, word))
                return true;
        }
        if(j+1 < lencol && board[i][j+1] == word.charAt(k)) {
            if(bt(i, j+1, k+1,board, word))
                return true;
        }
        if(i-1 >= 0 && board[i-1][j] == word.charAt(k)) {
            if(bt(i-1, j, k+1,board, word))
                return true;
        }
        if(j-1 >= 0 && board[i][j-1] == word.charAt(k)) {
            if(bt(i, j-1, k+1,board, word))
                return true;
        }
        
        visited.remove(i + "," + j);
        return false;
    }
}
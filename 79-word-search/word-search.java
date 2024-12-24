class Solution {
    public boolean exist(char[][] board, String word) {
        int n = board.length;
        int m = board[0].length;

        // Iterate over the board to find the starting character
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (board[i][j] == word.charAt(0) && backtrack(board, word, i, j, 0)) {
                    return true;
                }
            }
        }

        return false;
    }

    private boolean backtrack(char[][] board, String word, int i, int j, int index) {
        int n = board.length;
        int m = board[0].length;

        // If the entire word is found
        if (index == word.length()) {
            return true;
        }

        // Check boundaries and character match
        if (i < 0 || i >= n || j < 0 || j >= m || board[i][j] != word.charAt(index)) {
            return false;
        }

        // Temporarily mark the cell as visited
        char temp = board[i][j];
        board[i][j] = '#';

        // Explore all 4 possible directions
        boolean found = 
            backtrack(board, word, i, j + 1, index + 1) || // Right
            backtrack(board, word, i + 1, j, index + 1) || // Down
            backtrack(board, word, i - 1, j, index + 1) || // Up
            backtrack(board, word, i, j - 1, index + 1);   // Left

        // Restore the cell's original value
        board[i][j] = temp;

        return found;
    }
}
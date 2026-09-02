class Solution:
    def dfs(self, board, word,r, c, index):
        #base case
        if index == len(word):
            return True
        
        if r >= len(board) or r < 0 or c >= len(board[0]) or c < 0 or board[r][c] != word[index]:
            return False
        
        originWord = board[r][c]
        board[r][c] = '#'

        found = self.dfs(board, word, r+1, c, index+1) or self.dfs(board, word, r-1, c, index+1) or self.dfs(board, word, r, c + 1, index+1) or self.dfs(board, word, r, c - 1, index+1)

        board[r][c] = originWord

        return found
    def exist(self, board: List[List[str]], word: str) -> bool:
        res = False

        for i in range (len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, word, i , j, 0):
                    return True
        
        return False
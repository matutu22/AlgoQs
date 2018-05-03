# 79. Word Search


Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:  

    board =
    [
      ['A','B','C','E'],
      ['S','F','C','S'],
      ['A','D','E','E']
    ]

Given word = "ABCCED", return true.  
Given word = "SEE", return true.  
Given word = "ABCB", return false.  
---

##### Solution 1:
    class Solution(object):
        def exist(self, board, word):
            """
            :type board: List[List[str]]
            :type word: str
            :rtype: bool
            """
            def helper(board, word,i,j):
                if i<0 or j<0 or i >= len1 or j >= len2 or board[i][j] != word[0]:
                    return False

                if not word or word == board[i][j]:
                    return True


                temp = board[i][j] 
                board[i][j] = 0
                if helper(board, word[1:],i-1,j) or helper(board,word[1:],i+1,j) \
                    or helper(board,word[1:], i, j-1) or helper(board,word[1:], i, j+1):
                    return True
                board[i][j] =temp

                return False

            if not board:
                return False
            if not word:
                return True

            len1 = len(board)
            len2 = len(board[0])

            for i in range(len1):
                for j in range(len2):
                    if helper(board,word,i,j):
                        return True
            return False

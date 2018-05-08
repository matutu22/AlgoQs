# 212. Word Search II

Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example:

Input: 
words = ["oath","pea","eat","rain"] and board =  

    [
      ['o','a','a','n'],
      ['e','t','a','e'],
      ['i','h','k','r'],
      ['i','f','l','v']
    ]

Output: ["eat","oath"]  
Note:  
You may assume that all inputs are consist of lowercase letters a-z.


---


##### Solution 1:
    class TrieNode:
        def __init__(self):
            self.next = {}
            self.word = None

    class Solution(object):
        def findWords(self, board, words):
            """
            :type board: List[List[str]]
            :type words: List[str]
            :rtype: List[str]
            """

            if not board or not words:
                return []

            result = []
            tree = self.buildTree(words)
            self.l1 = len(board)
            self.l2 = len(board[0])
            for i in range(self.l1):
                for j in range(self.l2):
                    self.search(board, tree, i, j, result)

            return result


        def search(self, board, tree, i, j, result):

            char = board[i][j]
            if char == 0 or char not in tree.next:
                return

            tree = tree.next[char]
            if tree.word:
                result.append(tree.word)
                # Avoid duplicate
                tree.word = None

            board[i][j] = 0 # Avoid check twice    
            if i>0:
                self.search(board, tree, i-1, j, result)
            if j>0:
                self.search(board, tree, i, j-1, result)
            if i<self.l1-1:
                self.search(board, tree, i+1, j, result)
            if j<self.l2-1:
                self.search(board, tree, i, j+1, result)
            board[i][j] = char


        def buildTree(self, words):
            root = TrieNode()
            for word in words:
                temp = root

                for letter in word:

                    if letter not in temp.next:
                        temp.next[letter] = TrieNode()
                    temp = temp.next[letter]
                temp.word = word
            return root



# 73. Set Matrix Zeroes


Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:  


Input:  

    [  
      [1,1,1],  
      [1,0,1],  
      [1,1,1]  
    ]  

Output:   

      [  
        [1,0,1],  
        [0,0,0],  
        [1,0,1]  
      ]  

Example 2:  
  
  
Input: 

    [  
      [0,1,2,0],  
      [3,4,5,2],  
      [1,3,1,5]  
    ]  

Output:   

    [  
      [0,0,0,0],  
      [0,4,5,0],  
      [0,3,1,0]  
    ]  

Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
  
---

##### Solution 1:
	class Solution(object):
      def setZeroes(self, matrix):
          """
          :type matrix: List[List[int]]
          :rtype: void Do not return anything, modify matrix in-place instead.
          """
          b1 = False
          len1 = len(matrix)
          len2 = len(matrix[0])
          for i in range(len1):
              if matrix[i][0] == 0:
                  b1 = True
              for j in range(1,len2): # 1 here
                  if matrix[i][j] == 0:
                      matrix[i][0] = 0
                      matrix[0][j] = 0

          for i in range(len1-1,-1,-1): 
              for j in range(len2-1,0,-1): # Start from 1
                  if matrix[i][0] == 0 or matrix[0][j] == 0:
                      matrix[i][j] = 0

              if b1: # Deal with first column
                  matrix[i][0] = 0



##### Solution 2:

        b1 = False
        b2 = False
        len1 = len(matrix)
        len2 = len(matrix[0])
        for i in range(len1):

            for j in range(len2):
                if matrix[i][j] == 0:
                    if i == 0: b2 = True
                    if j == 0: b1 = True
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1,len1):  # Ignore 0,0
            for j in range(1,len2):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if b1:
            for i in range(len1):
                matrix[i][0] = 0 
        if b2:
            for i in range(len2):
                matrix[0][i] = 0

        
        
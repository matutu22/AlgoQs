# 54. Spiral Matrix


Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:  

    [
     [ 1, 2, 3 ],
     [ 4, 5, 6 ],
     [ 7, 8, 9 ]
    ]  
    
Output: [1,2,3,6,9,8,7,4,5]  

**Example 2:**

Input:  

    [
      [1, 2, 3, 4],
      [5, 6, 7, 8],
      [9,10,11,12]
    ]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

---

##### Solution:
	class Solution(object):
        def spiralOrder(self, matrix):
            """
            :type matrix: List[List[int]]
            :rtype: List[int]
            """
            if not matrix:
                return []

            result = []
            rowlo = 0
            rowhi = len(matrix) - 1
            collo = 0
            colhi = len(matrix[0]) - 1 

            while rowlo <= rowhi and collo <= colhi:
                for i in range(collo,colhi+1):
                    result.append(matrix[rowlo][i])
                rowlo += 1

                for i in range(rowlo,rowhi+1):
                    result.append(matrix[i][colhi])
                colhi -= 1

                if rowlo <= rowhi:
                    for i in range(collo,colhi+1)[::-1]:
                        result.append(matrix[rowhi][i])
                rowhi -= 1

                if collo <= colhi:
                    for i in range(rowlo,rowhi+1)[::-1]:
                        result.append(matrix[i][collo])
                collo += 1
            return result 
# 240. Search a 2D Matrix II



Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
For example,

Consider the following matrix:

    [
      [1,   4,  7, 11, 15],
      [2,   5,  8, 12, 19],
      [3,   6,  9, 16, 22],
      [10, 13, 14, 17, 24],
      [18, 21, 23, 26, 30]
    ]  

Given target = 5, return true.  


Given target = 20, return false.  

---

##### Solution 1:
	class Solution:
        def searchMatrix(self, matrix, target):
            """
            :type matrix: List[List[int]]
            :type target: int
            :rtype: bool
            """
            if not matrix:
                return False

            len1 = len(matrix)
            len2 = len(matrix[0])
            ro = 0
            co = len2 - 1 

            while ro <=  len1 -1 and co >=0:
                a = matrix[ro][co]
                if a == target:
                    return True
                elif a > target:
                    co -= 1
                else:
                    ro += 1

            return False 
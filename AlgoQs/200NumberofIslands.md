# 200. Number of Islands



Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

    11110
    11010
    11000
    00000
Answer: 1

Example 2:

    11000
    11000
    00100
    00011
Answer: 3

---

##### Solution:
	class Solution(object):
        def numIslands(self, grid):
            """
            :type grid: List[List[str]]
            :rtype: int
            """
            if not grid:
                return 0

            length1 = len(grid)
            length2 = len(grid[0])

            def helper(grid,coor):
                x,y = coor
                grid[x][y] = '0'
                if x < length1-1 and grid[x+1][y] == '1':
                    helper(grid,(x+1,y))
                if y < length2-1 and grid[x][y+1] == '1':
                    helper(grid,(x,y+1))
                if x >0 and grid[x-1][y] == '1':
                    helper(grid,(x-1,y))
                if y > 0 and grid[x][y-1] == '1':
                    helper(grid,(x,y-1))

            count = 0
            for i in range(length1):
                for j in range(length2):
                    if grid[i][j] == '1':
                        helper(grid,(i,j))
                        count += 1
            return count
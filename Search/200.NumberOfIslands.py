"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.
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
---------------------------------Approach----------------------------------
Analysis:

This is a typical recursive problem which can be solved by either Depth First Search(DFS) or Breath First Search (BFS).

Briefly speaking, DFS is to search every possible directions(solutions) whenever meet the new one.
BFS is to search and store every possible directions(solutions) using a queue usually,
then search from the head of the queue each time.
In this problem, possible directions are left, right, top, bottom, with constrains that the new location
is '1' and has not been visited before. Therefore, we can define a bool matrix (of same size) to store the status of
each element in the grid, set it to false when it is not available(been visited).
Complexity:
Time O(mn)
Space O(mn)
"""
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        row = len(grid)
        if row == 0:
            return 0
        col = len(grid[0])
        queue = []
        res = 0
        mark = [[True for j in range(col)] for i in range(row)]
        for i in range(row):
            for j in range(col):
                if mark[i][j] == True and grid[i][j] == '1':
                    queue.append([i, j])
                    mark[i][j] = False
                    while queue:
                        ii = queue[0][0]
                        jj = queue[0][1]
                        queue.pop(0)
                        if ii - 1 >= 0 and grid[ii-1][jj] == '1' and mark[ii-1][jj] == True:
                            queue.append((ii-1, jj))
                            mark[ii-1][jj] = False
                        if ii + 1 < row and grid[ii+1][jj] == '1' and mark[ii+1][jj] == True:
                            queue.append((ii+1, jj))
                            mark[ii+1][jj] = False
                        if jj - 1 >= 0 and grid[ii][jj-1] == '1' and mark[ii][jj-1] == True:
                            queue.append((ii, jj-1))
                            mark[ii][jj-1] = False
                        if jj + 1 < col and grid[ii][jj+1] == '1' and mark[ii][jj+1] == True:
                            queue.append((ii, jj+1))
                            mark[ii][jj+1] = False
                    res += 1
        return res

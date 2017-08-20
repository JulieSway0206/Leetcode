"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5]
----------------------Attention--------------------------
if - elif
"""
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        lst = []
        n = len(matrix)
        if n != 0:
            m = len(matrix[0])
        else:
            return lst


        l = 0
        r = m - 1
        up = 0
        down = n-1
        dir = 0
        while(l <= r and up <= down):
            if dir == 0:
                for i in range(l, r+1):
                    lst.append(matrix[up][i])
                up += 1
                dir = 1
            elif dir == 1:
                for i in range(up, down+1):
                    lst.append(matrix[i][r])
                r -= 1
                dir = 2
            elif dir == 2:
                for i in range(r, l-1, -1):
                    lst.append(matrix[down][i])
                down -= 1
                dir = 3
            elif dir == 3:
                for i in range(down, up-1, -1):
                    lst.append(matrix[i][l])
                l += 1
                dir = 0
        return lst

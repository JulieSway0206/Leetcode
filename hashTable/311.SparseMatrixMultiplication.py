"""
Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.
Example:

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]


     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |

-------------------------------------Approach-----------------------------------
1*7+0*0+0*0 = 7
-1*7+0*0+3*0 = -7
-1*0+0*0+3*1 = 3
这道题让我们实现稀疏矩阵相乘，稀疏矩阵的特点是矩阵中绝大多数的元素为0，而相乘的结果是还应该是稀疏矩阵，
即还是大多数元素为0，那么我们使用传统的矩阵相乘的算法肯定会处理大量的0乘0的无用功，所以我们需要适当的优化算法，
使其可以顺利通过OJ，我们知道一个 i x k 的矩阵A乘以一个 k x j 的矩阵B会得到一个 i x j 大小的矩阵C，
那么我们来看结果矩阵中的某个元素C[i][j]是怎么来的，起始是A[i][0]*B[0][j] + A[i][1]*B[1][j] + ... + A[i][k]*B[k][j]，
那么为了不重复计算0乘0，我们首先遍历A数组，要确保A[i][k]不为0，才继续计算.


"""
class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        rowA = len(A)
        colArowB = len(A[0])
        colB = len(B[0])
        C = [[0 for j in range(colB)] for i in range(rowA)]

        for m in range(rowA):
            for n in range(colArowB):
                if A[m][n] != 0:
                    for k in range(colB):
                        C[m][k] += A[m][n] * B[n][k]
        return C

"""
Implement pow(x, n).
---------------------------------Approach----------------------------------
Binary Search
python 2
-1/2 = -1
1/2 = 0
so dealing with n < 0 is necessary.
"""
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1

        if n < 0:
            n = -n
            x = 1/x

        if n % 2 == 0:
            return self.myPow(x*x, n/2)
        else:
            return x*self.myPow(x*x, n/2)

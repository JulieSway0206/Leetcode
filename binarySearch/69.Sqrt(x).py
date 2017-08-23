"""
Implement int sqrt(int x).
Compute and return the square root of x.
-------------------------------Approach------------------------------------------
Binary Search
when x = 2 -------> return 1
so the three condition judgements:
mid^2 > = < x is not appropriate here
if mid^2 > x but (mid-1)^2 < x
then there will comes to one point left == right == mid-1, then return mid
since we always fetch the lower bound, right = mid-1 when mid^2 > x is right here.
"""
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left = 0
        right = 2 ** 31 - 1
        while(left <= right):
            mid = (left + right) / 2
            if mid * mid > x:
                right = mid - 1
            elif (mid+1) * (mid+1) > x:
                return mid
            else:
                left = mid + 1

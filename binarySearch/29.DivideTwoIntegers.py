"""
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
-----------------------------------------------Approach-------------------------------------------------
Math, Binary Search
1. take the sign into considerations
2. take care of edge cases
3. Find the largest multiple so that (divisor * multiple <= dividend),
whereas we are moving with stride 1, 2, 4, 8, 16...2^n for performance reason. Think this as a binary search.
4. Handle overflow
"""
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        maxInt = 2 ** 31 -1
        minInt = -2 ** 31

        #step 1
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            sign = -1
        else:
            sign = 1
        dividend = abs(dividend)
        divisor = abs(divisor)

        #step 2
        if divisor == 0:
            return maxInt
        if dividend < divisor or dividend == 0:
            return 0

        #step 3
        def div(dividend, divisor):
            #Recursion exit condition
            if dividend < divisor:
                return 0

            sum = divisor
            multiple = 1
            while (sum + sum <= dividend):
                sum += sum
                multiple += multiple
            #Look for additional value for the multiple from the reminder (dividend - sum) recursively.
            return multiple + div(dividend - sum, divisor)

        ans = div(dividend, divisor)

        #step 4
        if ans > maxInt:
            if sign == 1:
                return maxInt
            else:
                return minInt
        else:
            return ans * sign

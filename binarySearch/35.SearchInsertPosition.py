"""
Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.

Here are few examples.
----------------------------------Approach-----------------------------------------
Binary search
(1)The desired index is between [low, high+1] ---> low <= high+1
(2)after the end of the loop, low > high, that is low >= high+1
(3)from (1) and (2) we know low == high+1, so the index now is in [low, low], so
low is the desired answer, high + 1 can also be the answer.
"""

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0

        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high)/2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return low

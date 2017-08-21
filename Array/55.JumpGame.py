"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2, 3, 1, 1, 4], return true.
A = [3, 2, 1, 0, 4], return false.
----------------------------------Approach--------------------------------------
A = [2,3], if you are in position 0 (2), you can jump 1 or 2 steps.
1. the reason to loop through the array is, if there is one i that cannot be reached, then you cannot use the ith
positon to jump to the end, and the positons behind i will not be reached.
2. get the max steps of the previous positions, if the max step cannot reach i, then no step can reach i.
"""
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        maximum = 0
        for i in range(n):
            if i  > maximum:
                return False

            maximum = max(maximum, nums[i] + i)

        return True

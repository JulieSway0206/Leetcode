"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
Note: The solution set must not contain duplicate triplets.

[-1,2,-1] and [-1,-1,2] are duplicate.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
------------------------------------------------Approach-----------------------------------------------------------
The idea is to sort an input array and then run through all indices of a possible first element of a triplet.
For each possible first element we make a standard bi-directional 2Sum sweep of the remaining part of the array.
Also we want to skip equal elements to avoid duplicates in the answer.
-----------------------------------------------Complexity----------------------------------------------------------
Time: O(n^2)
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        if n < 3:
            return [] #must return a list, it can not be null(None)

        lst = []
        elem = []
        nums.sort()

        for i in range(n-2):
            if (i > 0 and nums[i] == nums[i-1]):
                continue

            lo = i + 1
            hi = n - 1
            target = -nums[i]
            while lo < hi:
                sum = nums[lo] + nums[hi]
                if sum == target:
                    elem = [nums[i], nums[lo], nums[hi]]
                    lst.append(elem)
                    while(lo < hi and nums[lo] == nums[lo+1]):
                        lo += 1
                    while(lo < hi and nums[hi] == nums[hi-1]):
                        hi -= 1
                    lo += 1
                    hi -= 1
                elif sum < target:
                    while(lo < hi and nums[lo] == nums[lo+1]):
                        lo += 1
                    lo += 1
                else:
                    while(lo < hi and nums[hi] == nums[hi-1]):
                        hi -= 1
                    hi -= 1
        return lst

"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(ie. 0,1,2,4,5,6,7 might become 4,5,6,7,0,1,2).
You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
-----------------------------------------Approach----------------------------------------------
Binary search
1. what is rotated sorted array?
0,1,2,4,5,6,7 --> 0,1,5,6,7,2,4 is not rotated sorted array
2. so there are two situations:
(1) sorted array, (increase monotonically)
(2) rotated, the first half (ascending) elements are all greater than the second half(ascending)
4,5,6,7,0,1,2 --> 4 > 0
3.So when doing binary search, we can make a judgement that which part is ordered and whether the target is in that range,
if yes, continue the search in that half, if not continue in the other half.
(1)if nums[start] <= nums[mid]:
always -------> situation1
the mid is in first half -- > 4,5,6,7 situation2
(2)else in the second half --> 0,1,2
"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return -1

        start = 0
        end = n-1
        while start <= end:
            mid = (start + end)/2
            if target == nums[mid]:
                return mid

            if nums[start] <= nums[mid]: #there must be"=", otherwise [3,1] , 1 will be wrong result.
                if target >= nums[start] and target < nums[mid]: # there must be "=", otherwise [5,1,3], 5 will be wrong result.
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if target > nums[mid] and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1

"""
Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].
For example,
Given [5, 7, 7, 8, 8, 10] and target value 8, return [3, 4].
--------------------------------------Approach-----------------------------------------------------
Binary Search
1. Time complexity = O(log n) is mostly a hint that you can  use binary search. (T(n) = T(n/2) + O(1))
2. There must be two indices in the array. Which means, we can just simply apply to binary search twice to find each index of the target element.
3. Initially index = -1, because if the target is not found, we should return [-1, -1].
4. For the findFirst function:
if target == nums[mid], go left to find another target in the front
use index to record the currently foremost target


"""
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        if n == 0:
            return [-1, -1]

        def findFirst(nums, target):
            index = -1
            start = 0
            end = len(nums) - 1
            while start <= end:
                mid = (start + end) / 2
                if target <= nums[mid]:#-----------if target == nums[mid], go left to find another target in the front
                    end = mid - 1
                else:
                    start = mid + 1
                if target == nums[mid]:#-------------use index to record the currently foremost target
                    index = mid
            return index

        def findLast(nums, target):
            index = -1
            start = 0
            end = len(nums) - 1
            while start <= end:
                mid = (start + end) / 2
                if target >= nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
                if target == nums[mid]:
                    index = mid
            return index

        result = []
        first= findFirst(nums, target)
        result.append(first)
        last = findLast(nums, target)
        result.append(last)
        return result

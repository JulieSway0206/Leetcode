"""
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
--------------------------------------------Approach-----------------------------------------------
This approach is based on the fact that when we rotate the array k times, k elements from the back end of the array come to the front and the rest of the elements from the front shift backwards.

In this approach, we firstly reverse all the elements of the array. Then, reversing the first k elements followed by reversing the rest n-kn−k elements gives us the required result.
Let n = 7 and k = 3.
Original List                   : 1 2 3 4 5 6 7
After reversing all numbers     : 7 6 5 4 3 2 1
After reversing first k numbers : 5 6 7 4 3 2 1
After revering last n-k numbers : 5 6 7 1 2 3 4 --> Result
Complexity Analysis

Time complexity : O(n). nn elements are reversed a total of three times.

Space complexity : O(1). No extra space is used.
"""
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        leng = len(nums)
        k %= leng
        self.reverseNum(nums, 0, leng-1)
        self.reverseNum(nums, 0, k-1)
        self.reverseNum(nums, k, leng-1)

    def reverseNum(nums, start, end):
        while(start < end):
            temp = nums[end]
            nums[end] = nums[start]
            nums[start] = temp

            start += 1
            end -= 1
        

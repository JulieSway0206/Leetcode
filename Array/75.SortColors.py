"""
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent,
with the colors in the order red, white and blue. Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
----------------------------------------------------Approach----------------------------------------------------------
Two Pointers Sort
Why when nums[index] == 2: index -= 1

0000 1  11  1     1201  2   22
     p0    index        p2

when index > p0, elements between p0 and index are all "1"s.
so after swap nums[index] and nums[p0] we don't need to check nums[index] again, since nums[index] == 1,
then index += 1
when nums[index] == 2, after swap nums[index] and nums[p2], nums[index] need to be checked, so index -= 1 then index += 1.
"""
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        p0 = 0
        p2 = len(nums) - 1
        index = 0

        while index <= p2:

            if nums[index] == 0:
                nums[index] = nums[p0]
                nums[p0] = 0
                p0 += 1

            elif nums[index] == 2:
                nums[index] = nums[p2]
                nums[p2] = 2
                p2 -= 1
                index -= 1

            index += 1

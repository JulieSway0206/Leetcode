"""
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],
Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the new length.
----------------------------------------Approach-------------------------------------------------------
Two Pointers
Use i to indicate the positon where there is confirmed no duplicates from the beginning to this position,
use j to loop through nums. Since the array is already sorted, so when nums[j] != nums[i], we can make sure
that nums[i] won't appear any more. So we can move i one more step forward.
If nums[j] == nums[i],
i should move one step forward, and copy nums[j] to nums[i].
As long as nums[i] == nums[j], we increment j to skip the duplicate.

j
1233445
i

 j
1233445
i

  j
1233445
 i

   j
1233445
  i
    j
1233445
  i

     j
1234445
   i

      j
1234445
   i

01234
1234545
    i
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return n

        i = 0
        for j in range(n):
            if nums[i] == nums[j]:
                continue
            else:
                i += 1
                nums[i] = nums[j]
        return i + 1

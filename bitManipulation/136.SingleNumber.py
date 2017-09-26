"""
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
-------------------------------------------Approach---------------------------------------
1.Bit Manipulation
binary xor: ^
0 0 0
0 1 1
1 0 1
1 1 0
So if the array is {2,1,4,5,2,4,1} then it will be like we are performing this operation
((2^2)^(1^1)^(4^4)^(5)) => (0^0^0^5) => 5.
Hence picking the odd one out ( 5 in this case).
Complexity
______________
Time - O(N)
SPace - O(1)
2. Hash Table: dictionary
dic.get(num, 0)
if key num cannot be found in dictionary dic, then it will return 0.
"""
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for num in nums:
            result = result ^ num

        return result

# class Solution(object):
#     def singleNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         dic = {}
#         for num in nums:
#             dic[num] = dic.get(num, 0) + 1
#
#         for key, val in dic.items():
#             if val == 1:
#                 return key

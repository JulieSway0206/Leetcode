"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1, 1, 2] have the following unique permutations:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
------------------------------------Approach------------------------------------
Backtracking
handle duplication:
[2,2,1,1]:
122, 212, 221
for the last "1":
1122
break
1212
2112
break
1221
2121
2211
break
The idea is the nth element in the array, which is gonna inserted into arrays formed in the first (n-1)
elements, only take responsibility for the parts before encounter with a number that is equal to the nth
element. For example, 122 ---> {1}122, other formations like 12{1}2 is not the last "1"'s responsibility.
Since for 1,2,2, it already has a formation of 212.
"""
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
#         n = len(nums)
#         res = []

#         for i in range(n):
#             if i == 0:
#                 res.append([nums[i]])
#             else:
#                 removal = []
#                 for ls in res:
#                     if len(ls) == i:
#                         removal.append(ls)
#                         for j in range(i+1):
#                             array = []
#                             array += ls
#                             array.insert(j, nums[i])
#                             res.append(array)
#                             if j < len(ls) and ls[j] == nums[i]:
#                                 break
#                 for elm in removal:
#                     res.remove(elm)
#         return res
        n = len(nums)
        res = []
        for i in range(n):
            if i == 0:
                res.append([nums[i]])
            else:
                ans = []
                for ls in res:
                    for j in range(len(ls)+1):
                        array = []
                        array += ls
                        array.insert(j, nums[i])
                        ans.append(array)
                        if j < len(ls) and ls[j] == nums[i]: #for the problem of 46.permutationsI, in
                                break                       #which the given array contains distinct numbers, this step
                res = ans                                   #of handling duplication is not needed.
        return res

        # ans = [[]]
        # for n in nums:
        #     new_ans = []
        #     for l in ans:
        #         for i in xrange(len(l)+1):
        #             new_ans.append(l[:i]+[n]+l[i:])
        #             if i<len(l) and l[i]==n: break              #handles duplication
        #     ans = new_ans
        # return ans

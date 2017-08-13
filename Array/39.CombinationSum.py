"""
Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7,
A solution set is:
[
  [7],
  [2, 2, 3]
]
-----------------------------------------Approach---------------------------------------------
Dynamic Programming
For each candidate "c" we run through all combinations for target t-c starting with the value
greater or equal than c to avoid duplicates and store only ordered combinations.
"""
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = list(set(candidates))
        nums.sort()
        n = len(nums)
        dp = [[] for i in range(target + 1)]

        for num in nums:
            if num <= target:
                dp[num].append([num])


        for i in range(target + 1):
            for j in range(n):
                if i - nums[j] < 0:
                    continue
                elif len(dp[i-nums[j]]) != 0:
                    for lst in dp[i-nums[j]]:
                        if nums[j] <= lst[0]:
                            array = []               # array = lst , array.append(nums[j]), dp[i].append(array) is not applicable,
                            array.append(nums[j])    # since when array = lst, the array points to the same position as lst, if change
                            array += lst             # array, then lst will also be changed.
                            dp[i].append(array)
        return dp[target]

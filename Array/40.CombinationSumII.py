"""
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
------------------------------------------Approach------------------------------------------------
Recursion
S(i, s) = S(i-1, s) + S(i-1, s-candidates[i])
1.S(i-1,s) -----------> for loop --> for i in range(start, len(candidates))
2.S(i-1, s-candidates[i]) ----------------> recursion ----> for ls in search(i+1, target - candidates[i], candidates)
3.avoid duplicates:
if i != start and candidates[i] == candidates[i-1]:
    continue
4. if candidates[i] > target:
    break
then return []
up to one layer
for ls in search(i+1, target - candidates[i], candidates): #recursion
    res.append([candidates[i]]+ls)
there is no ls since [] is returned,
so res won't add anything
"""
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        return self.search(0, target, candidates)

    def search(self, start, target, candidates):
        if target == 0:
            return [[]]

        res = []

        for i in range(start, len(candidates)): #for loop
            if candidates[i] > target:
                break
            if i != start and candidates[i] == candidates[i-1]: #avoid duplicates
                continue
            for ls in search(i+1, target - candidates[i], candidates): #recursion
                res.append([candidates[i]]+ls)
        return res

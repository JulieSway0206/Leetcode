"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
----------------------------------Approach-------------------------------------------------
Backtracking
open records the number of '(', close records the number of ')'.
Under the condition that open is less than the pair number n, we can add a '(' first. Then we always have two choices:
1. add one more '(' if open < n
2. add a ')' if close < open
"""
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []

        lst = []

        def backtrack(str, open, close, pairNum):
            if len(str) == 2 * pairNum:
                lst.append(str)

            if open < pairNum:
                backtrack(str+'(', open+1, close, pairNum)
            if close < open:
                backtrack(str+')', open, close+1, pairNum)

        backtrack('', 0, 0, n)
        return lst

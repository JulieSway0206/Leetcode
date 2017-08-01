"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
Example
Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
--------------------------------------Approach------------------------------------------------------
Dynamic Programming
dp(i, j) represents whether s(i ... j) can form a palindromic substring, dp(i, j) is true('1') when s(i) equals to s(j)
and s(i+1 ... j-1) is a palindromic substring.
if (s[i]==s[j] and (j-i < 3 or dp[i+1][j-1] == 1))
When we found a palindrome, check if it's the longest one.
If it is the longest one,
substring = s[i:j+1].
-------------------------------------Complexity-----------------------------------------------------
Time:
O(n^2)
Space(n^2)
"""






class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        dp = [[0]*n for i in range(n)]
        length = 0
        substring = ''
        if n == 0:
            return None


        for i in reversed(range(n)):
            for j in range(i, n):
                if (s[i]==s[j] and (j-i < 3 or dp[i+1][j-1] == 1)):#how to find palindromic substring
                    dp[i][j] = 1
                    if j-i+1 > length:
                        length = j-i+1
                        substring = s[i:j+1]
        return substring

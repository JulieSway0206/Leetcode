"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

"""
Approach
---------------------------------------------------------------
Two Pointers

substring[i,j]

j
abcat
i

 j
abcat
i

  j
abcat
i

   j
abcat
i

   j
abcat
 i

    j
abcat
 i
----------------------------------------------------------------------
Complexity

Time
O(2n ) = O(n)
In the worst case, each character will be visited twice by i and j.

Space
The size of the Set is upper bounded by the size of the string n and and the size of the charset/alphabet m.
O(min(m,n))

"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0:
            return 0

        i = j = 0

        substring = set()
        ans = 0

        while (i < n and j < n):
            if (s[j] not in substing):
                substring.add(s[j])
                j += 1
                ans = max(ans, j-i)

            else:
                substring.remove(s[i])
                i += 1

        return ans

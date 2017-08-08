"""
Implement strStr().
Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
-------------------------------------Approach------------------------------------------------------------
Two pointers
3 situations:
1. if j == m:
return i
\\m+1
2. after looping over all the haystack string, there is no needle matched, for ex. "abc"-"d":
i + j = i = n:
return -1
3. haystack[i+j] != needle[j]:
break
"""
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(haystack)
        m = len(needle)
        if m == 0:
            return 0
        if n == 0:
            return -1

        for i in range(n+1):
            for j in range(m+1):
                if j == m:
                    return i
                if i + j == n:
                    return -1
                if haystack[i+j] != needle[j]:
                    break

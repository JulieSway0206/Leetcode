"""
Given a string containing just the characters '(',')','{','}','[' and ']', determine
if the input string is valid. The brackets must close in correct order,"({})" and "()[]"
are all valid, but "[{}" is not.
-----------------------------Approach-------------------------------------------
Stack
First In Last Out ('(', '{', '[')
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        if n < 2 or n % 2 != 0:
            return False

        stack = []

        mapping = {
        ')' : '(',
        '}' : '{',
        ']' : '['
        }

        for i in range(n):
            if s[i] in mapping.values():
                stack.append(s[i])
            elif s[i] in mapping.keys():
                if stack == [] or mapping[s[i]] != stack.pop():
                    return False
                else:
                    continue
            else:
                return False
        return stack == []

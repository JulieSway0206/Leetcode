"""
Implement atoi to convert a string to an integer.
Hint: Carefully consider all possible input cases.
----------------------Approach-------------------------------
1.discards whitespaces of two ends
str = str.strip(' ')
2.sign of the number
str[0]='-': sign = -1, start = 1
str[0]='+': sign = 1, start = 1
else: sign = 1, start = 0
3.overflow
max(-2**31,min(sum * sign, 2**31-1))
java: Integer.MAX_VALUE, Integer.MIN_VALUE
4.invalid input
str[i].isdigit():
ord(str[i]) - ord('0')
"""

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        n = len(str)
        if n == 0:
            return 0
        str = str.strip(' ')
        sum = 0
        firstChar = str[0]
        if firstChar == '+':
            sign = 1
            start = 1
        elif firstChar == '-':
            sign = -1
            start = 1
        else:
            sign = 1
            start = 0
        for i in range(start, len(str)):
            if not str[i].isdigit():
                return max(-2**31, min(sum*sign, 2**31-1))
            else:
                digit = ord(str[i]) - ord('0')
                sum = sum * 10 + digit
        return  max(-2**31, min(sum*sign, 2**31-1))

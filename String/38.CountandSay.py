"""
The count-and-say sequence is the sequence of integers with the first five terms as following:
1.     1
2.     11
3.     21
4.     1211
5.     111221

1 is read off as "One 1" ---> 11
11 is read off as "Two 1s" --> 21
21 is read off as "one 2, then one 1" --> 1211

Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

ex1:                           ex2:
Input: 1                       Input: 4
Output: "1"                    Output: "1211"
"""
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n <= 0:
            return ""

        def countSay(s):
            string = ""
            count = 1
            c = s[0]
            n = len(s)
            for i in range(1, n):
                if s[i] == c:
                    count += 1
                else:
                    string += str(count)
                    string += c
                    count = 1
                    c = s[i]
            string += str(count)
            string += c
            return string

        s = "1"
        for i in range(n-1):
            s = countSay(s)
        return s

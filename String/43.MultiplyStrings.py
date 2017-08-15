"""
Given two non-negative integers num1 and num2, represented as strings, return the product of
num1 and num2.
Note:

1.The length of both num1 and num2 is < 110.
2.Both num1 and num2 contains only digits 0-9.
3.Both num1 and num2 does not contain any leading zero.
4.You must not use any built-in BigInteger library or convert the inputs to integer directly.
--------------------------------Approach------------------------------------------
Math/String
1. m digits number multiplies n digits number, the result number is at most m+n digits:
999 * 99 < 1000 * 100 = 100000, at most 3+2 = 5 digits.
2. reverse the number string to calculate from least significant digit
3. num1[i]*num2[j], the result should be added to the digit res[i+j]
4. the most significant digit cannot be 0
5. convert list to string
"""
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n = len(num1)
        m = len(num2)
        res = [0] * (m + n) #step1

        num1 = num1[::-1] #step2
        num2 = num2[::-1]

        for i, b1 in enumerate(num1): #step3
            for j, b2 in enumerate(num2):
                res[i+j] += int(b1) * int(b2)
                res[i+j+1] += res[i+j] / 10
                res[i+j] %= 10

        while len(res) > 1 and res[-1] == 0: #step4
            res.pop()

        return ''.join(map(str, res[::-1])) #step5

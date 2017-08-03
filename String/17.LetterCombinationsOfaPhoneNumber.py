"""
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

Example
Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

mapping = {
            '0': '0',
            '1': '1',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
            }
-----------------------------------Approach-------------------------------------------------------------
FIFO
[s1, s2, s3]
find those strings that need to be added to a letter : while (len(lst[0]) == i)
grab the first string in list, and delete it from the list
then loop through the letter of mapping[digits[i]], add the letter to the string grabbed and add to the list
s1+ le1, s1+ le2, s1 + le3
"""
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = {
            '0': '0',
            '1': '1',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
            }  #don't forget to add quote of keys, wrong:1, correct:'1'

        n = len(digits)
        if n == 0:
            return [] #wrong['']

        lst = ['']

        #FIFO
        for i in xrange(0, n):
            while (len(lst[0]) == i):
                elem = lst[0]
                lst.remove(lst[0])
                for str in mapping[digits[i]]:
                    lst.append(elem + str)
        return lst

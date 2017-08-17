"""
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:
[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note: All inputs will be in lower-case.
--------------------------------------Approach-------------------------------------------
Prime Number
the hash table in python can be dictionary
Since prime number has no divisors, different anagrams' get unique keys.
the hash table -- dictionary map, is to record the position of a group of anagrams in the array res.
"""
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]
        map = {}
        res = []
        for i in range(len(strs)):
            key = 1
            for letter in strs[i]:
                key *= prime[ord(letter) - ord('a')]

            if key in map:
                lst = res[map[key]]
                lst.append(strs[i])
            else:
                lst = []
                lst.append(strs[i])
                res.append(lst)
                map[key] = len(res) - 1
        return res

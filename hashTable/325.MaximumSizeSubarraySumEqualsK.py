"""
Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

Note:
The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

Example 1:
Given nums = [1, -1, 5, -2, 3], k = 3,
return 4. (because the subarray [1, -1, 5, -2] sums to 3 and is the longest)

Example 2:
Given nums = [-2, -1, 2, 1], k = 1,
return 2. (because the subarray [-1, 2] sums to 1 and is the longest)

Follow Up:
Can you do it in O(n) time?
-----------------------------------Approach-----------------------------------
In the map, acc is the accumulative value of num
key is acc value, and value is the index
if nums = [a, b, c]
1.if a + b + c - k = a
then b + c = k
2.if a + b = k
then a + b - k = 0
so we set map[0] = -1
注意这道题不要先生成hashmap再遍历map找和，因为key有可能重复，就会把之前的相同key覆盖，越靠前的key产生的subarray越长，就会漏掉答案。
"""
class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans , acc = 0 , 0
        map = {0 : -1}

        for i in range(len(nums)):
            acc += nums[i]
            if acc not in map:
                map[acc] = i

            if acc - k in map:
                ans = max(ans, i - map[acc-k])

        return ans

"""
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1, 3], [2, 6], [8, 10], [15, 18],
return [1, 6], [8, 10], [15, 18].
-----------------------------------Approach-------------------------------------
1.Merge Sort:
The code template for merge sort is sort function below.
Time Complexity:
T(n) = 2T(n/2) + O(n) = O(nlogn)
2.max over the end of intervals
3.out.append(interval) vs out += [interval]
first, if use "+", there must be two iterables to combine.
second, "append" uses less time than "+", "+" exceeds time limit here.
"""
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        def sort(intervals):
            n = len(intervals)
            if n < 2:
                return intervals
            else:
                A1 = sort(intervals[0:n/2])
                A2 = sort(intervals[n/2:])
                n = len(A1)
                m = len(A2)
                i = 0
                j = 0
                B = []
                while(i < n and j < m):
                    if A1[i].start > A2[j].start:
                        B.append(A2[j])
                        j += 1
                    else:
                        B.append(A1[i])
                        i += 1
                while(i < n):
                    B.append(A1[i])
                    i += 1
                while(j < m):
                    B.append(A2[j])
                    j += 1
                return B

        Intervals = sort(intervals)
        out = []
        for interval in Intervals:
            if out and interval.start <= out[-1].end:
                out[-1].end = max(out[-1].end, interval.end)
            else:
                out.append(interval)
        return out

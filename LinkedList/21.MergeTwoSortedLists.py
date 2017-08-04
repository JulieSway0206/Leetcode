"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
-------------------------------Approach--------------------------------------------------
Recursion
recursively call the function itself, the first four lines(judge if l1 or l2 is None) is important, one reason is it reaches the end of the
recursion.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None: #cannot use null here
            return l2
        if l2 == None:
            return l1

        head = l1
        if l1.val < l2.val:
            head = l1
            head.next = self.mergeTwoLists(l1.next, l2) ## don't forget self here
        else:
            head = l2
            head.next = self.mergeTwoLists(l1, l2.next)
        return head

"""
Given a linked list, remove the nth node from the end of list and return its head.

For example,
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.
Try to do this in one pass.
"""
"""
-------------------------------Approach One--------------------------------------
Counting from back
Instead of really removing the nth node, I remove the nth value.
I recursively determine the indexes (counting from back), then shift the values for all indexes larger than n, and then always drop the head.
"""
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        def index(node):
            if not node:
                return 0
            else:
                pos = index(node.next) + 1
                if pos > n:
                    node.next.val = node.val
            return pos
        index(head)
"""
------------------------------------Approach Two---------------------------------
Two pointers
slow, fast, head are all pointers. At beginning, three pointers are all poninted at the end of the linked list.
Use fast pointer to move first, after move fast n steps, move slow pointer.
If fast = None, which means fast passes the whole linked list, and the one where slow poninted at should be removed.

1. if the last one should be removed(len(linkedlist)==n), when fast = None, slow points to the end of linkedlist, so
return head.next.

0
1 -> 2 -> 3       n = 3
    fast

     1
1 -> 2 -> 3       n = 3
         fast

          2
1 -> 2 -> 3  None   n = 3
             fast

2. the one that need to be removed is in the middle. So we should stop one element before the target, when fast reaches
the start one of linked list, and let slow.next = slow.next.next. Then return head.

0
1 -> 2 -> 3 -> 4 -> 5      n = 2
    fast

          1
1 -> 2 -> 3 -> 4 -> 5      n = 2
s         f


1 -> 2 -> 3 -> 4 -> 5  n = 2
     s         f

             target
1 -> 2 -> 3 -> 4 -> 5  n = 2   fast.next = None
          s         f



1 -> 2 -> 3 -> 5    slow.next = slow.next.next

-----------------------------------------------------------------

class Solution(object):
    def removeNthFromEnd(self, head, n):
        fast = slow = head
        for i in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head

"""

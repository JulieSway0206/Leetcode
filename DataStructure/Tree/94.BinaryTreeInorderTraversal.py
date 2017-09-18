"""
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree [1, null, 2, 3],
  1
    \
     2
    /
  3
return [1, 3, 2].
Note: Recursive solution is trivial, could you do it iteratively?
-----------------------------------Approach----------------------------------
Tree Traversals (Inorder, Preorder, Postorder)
(a) Inorder (Left, Root, Right)
(b) Preorder (Root, Left, Right)
(c) Postorder (Left, Right, Root)
Algorithm Inorder(tree)
   1. Traverse the left subtree, i.e., call Inorder(left-subtree)
   2. Visit the root.
   3. Traverse the right subtree, i.e., call Inorder(right-subtree)
1. recursive solution
Time Complexity = O(n)
Space Complexity = O(logn)
2. iterative solution (with stack)
Time Complexity = O(n)
Space Complexity = O(logn)
3. Morris Traversal (haven't done)
Time Complexity = O(n)
Space Complexity = O(1)
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#recursive solution
# class Solution(object):
#     def inorderTraversal(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[int]
#         """
#         res = []
#         self.helper(res, root)
#         return res
#
#     def helper(self, lst, root):
#         if root:
#             self.helper(lst, root.left)
#             lst.append(root.val)
#             self.helper(lst, root.right)

#iterative solution
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []

        while(root or len(stack) != 0):
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                res.append(root.val)
                root = root.right
        return res

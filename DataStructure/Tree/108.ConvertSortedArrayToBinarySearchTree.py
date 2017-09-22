"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
--------------------------------------------Approach------------------------------------------
Binary Search Tree
Binary Search Tree, is a node-based binary tree data structure which has the following properties:

1.The left subtree of a node contains only nodes with keys less than the node’s key.
2.The right subtree of a node contains only nodes with keys greater than the node’s key.
3.The left and right subtree each must also be a binary search tree. There must be no duplicate nodes.

Height balanced
the root is approximately equal to ascending array's middle item

Depth-first Search
The idea is to find the root first, then recursively build each left and right subtree.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None

        mid = len(nums) / 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root

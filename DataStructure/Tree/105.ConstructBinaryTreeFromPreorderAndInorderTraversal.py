"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
------------------------------------Approach------------------------------------
Depth-first Search
(a) Inorder (Left, Root, Right)
(b) Preorder (Root, Left, Right)

                1
        2              3
   4         5      6

Inorder[4,2,5,1,6,3]
Preorder[1,2,4,5,3,6]


1.root.left should in front of root.right since in preorder left is before right.
2.preorder pops out the first element in root.left function, then in root.right the
preorder does not contain this element which pops out in root.left step.
3.array = [4], array[0:0] = [], array[1:] = []
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind+1:])
            return root

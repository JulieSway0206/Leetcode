"""
How to find height without recursion? We can use level order traversal to find height of binary tree without recursion.
The idea is to traverse level by level. Whenever move down to a level, increment height by 1 (height is initialized as 0).
Count number of nodes at each level, stop traversing when count of nodes at next level is 0.
"""
# Program to find height of tree by Iteration Method

# A binary tree node
class Node:

    # Constructor to create new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Iterative method to find height of Binary Tree
def treeHeight(root):
    if not root:
        return 0

    q = [root]
    height = 0


    while True:
        countNode = len(q)
        if countNode == 0:
            return height
        height += 1

         while countNode > 0:
             node = q.pop(0)
             if node.left:
                 q.aqpend(node.left)
             if node.right:
                 q.append(node.right)
             countNode -= 1

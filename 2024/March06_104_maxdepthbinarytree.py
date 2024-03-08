from typing import Optional
"""
104. Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root 
node down to the farthest leaf node.

Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: 3

Example 2:
    Input: root = [1,null,2]
    Output: 2

Constraints:
    The number of nodes in the tree is in the range [0, 104].
    -100 <= Node.val <= 100
"""

#######################
# Solution Attempt #1 #
#######################

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
I don't have much experience with BSTs but my initial thoughts to use recursion and just try to go down both
the left and right sides and return the maximum depth from each side
"""
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:

def maxDepth(root):
    if not root:
        return 0
    else:
        left_depth = maxDepth(root.left)
        right_depth = maxDepth(root.right)
        return max(left_depth, right_depth) + 1
    
# Construct the tree for Example 1: [3,9,20,null,null,15,7]
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20, TreeNode(15), TreeNode(7))

print(maxDepth(root))

# Construct the tree for Example 2: [1,null,2]
root2 = TreeNode(1)
root2.right = TreeNode(2)

print(maxDepth(root2))  # Output: 2

"""
ACCEPTED
    Runtime 49ms
    Beats 6.39% of users with Python3

Memory
    17.72MB
    Beats 30.89% of users with Python3
"""


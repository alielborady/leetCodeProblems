"""

Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.


"""

# Definition for a binary tree node.
from typing import List

from pyparsing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if not root: return False

        targetSum -= root.val
        return not (targetSum or root.left or root.right) or \
            (self.hasPathSum((root.left), targetSum)) or \
            (self.hasPathSum((root.right), targetSum))

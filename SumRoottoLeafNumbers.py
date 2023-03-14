"""
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that 
the answer will fit in a 32-bit integer.

A leaf node is a node with no children.

https://leetcode.com/problems/sum-root-to-leaf-numbers/
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def helper(root, sum):

            if not root:
                return 0

            sum *= 10 
            sum += root.val
            if not root.left and not root.right:
                return sum
            return helper(root.left, sum) + helper(root.right, sum)
            
         
        return helper(root, 0)



print(Solution().sumNumbers(TreeNode(val=1, left=TreeNode(val=2), right=TreeNode(val=3))))
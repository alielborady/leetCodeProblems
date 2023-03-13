"""

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

https://leetcode.com/problems/symmetric-tree/

"""

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    
        def helper(t1: Optional[TreeNode], t2: Optional[TreeNode]):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            
            return (t1.val == t2.val) and helper(t1.left,t2.right)
        
        return helper(root, root)
        


print(Solution().isSymmetric(TreeNode(val=1, left=TreeNode(val=2, left=TreeNode(val=3), right=(TreeNode(val=4))),right=(TreeNode(val=2, left=TreeNode(val=4), right=TreeNode(val=3))))))
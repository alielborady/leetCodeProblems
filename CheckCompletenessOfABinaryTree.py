"""
Given the root of a binary tree, determine if it is a complete binary tree.

In a complete binary tree, every level, except possibly the last, is completely filled, 
and all nodes in the last level are as far left as possible. It can have between 1 and 
2h nodes inclusive at the last level h.


https://leetcode.com/problems/check-completeness-of-a-binary-tree/
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        queue = []
        queue.append(root)
        is_last = False

        while len(queue) > 0:
            curr = queue.pop(0)

            if curr.left:
                if is_last:
                    return False
                queue.append(curr.left)
            else:
                is_last = True

            if curr.right:
                if is_last:
                    return False
                queue.append(curr.right)
            else:
                is_last = True

        return True
            
print(Solution().isCompleteTree(TreeNode(val=1, left=TreeNode(val=2,left=TreeNode(val=4), right=TreeNode(val=5)),right=TreeNode(val=3, left=TreeNode(val=6)))))
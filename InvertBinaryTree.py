"""
Given the root of a binary tree, invert the tree, and return its root.

"""


# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        self.dfs(root)

        return root

    def dfs(self, root):
        if root is None: return

        self.dfs(root.left)
        # if 
        root.left, root.right = root.right, root.left
        self.dfs(root.left)


x = TreeNode(val=4, left=TreeNode(val=2, left=TreeNode(val=1), right=TreeNode(val=3)), right=TreeNode(val=7, left=TreeNode(val=6), right=TreeNode(val=9)))
sth = Solution()
print(sth.invertTree(x).val)

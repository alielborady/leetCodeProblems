"""
Given the root of a Binary Search Tree (BST), return 
the minimum difference between the values of any two different nodes in the tree.

"""

### Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:

        ### only provides difference between consecutive nodes
        # def dfs(self, root, diff):
        #     if root:
        #         if root.left:
        #             diff = min(diff, abs(root.val-root.left.val))
        #         if root.right:
        #             diff = min(diff, abs(root.val-root.right.val))
        #         # diff = min(abs(diff-root.right.val), abs(diff-root.left.val))
        #         return min(dfs(self, root.left, diff), dfs(self,root.right, diff))
        #     else: return diff 
            
        # return dfs(self,root, 10000)
        
        self.ans = 10000
        self.pred = None
        self.inOrder(root)
        return self.ans

    def inOrder(self, root:TreeNode) -> None:

        if root is None:
            return
        
        self.inOrder(root.left)
        if self.pred != None:
            self.ans = min(self.ans, abs(root.val-self.pred))
        self.pred = root.val
        self.inOrder(root.right)


x = TreeNode(val=4, left=TreeNode(val=2, left=TreeNode(val=1), right=TreeNode(val=3)), right=TreeNode(val= 6))
x = TreeNode(val=90, left=TreeNode(val=69, left=TreeNode(val=49,right=TreeNode(val=52)), right=TreeNode(val=89)))
sth = Solution()
print(sth.minDiffInBST(x))

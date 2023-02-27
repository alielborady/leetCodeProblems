"""
Given the root of a binary tree, return the zigzag level order 
traversal of its nodes' values. (i.e., from left to right, 
then right to left for the next level and alternate between).
"""


### Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        self.level = 0
        self.values = []
        
        self.helper(root)
        return self.values

    def helper(self, root: Optional[TreeNode]) -> None:
            
        if root is None:
            return

        try :
            if self.level % 2 == 0:
                self.values[self.level].append(root.val)
            else:
                self.values[self.level] = [root.val] + self.values[self.level]
        except IndexError:
            self.values.append([root.val])
        
        self.level +=  1
        self.helper(root.left)
        self.helper(root.right)
        self.level -= 1



sth = Solution()
x = TreeNode(val=3,left=TreeNode(val=9), right=TreeNode(val=20, left=TreeNode(val=15), right=TreeNode(val=7)))
print(sth.zigzagLevelOrder(x))
"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along 
the longest path from the root node down to the farthest leaf node.
"""


from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ### DFS 
        # def dfs(self, root: Optional[TreeNode], level):
        #     if root :
        #         level +=1
        #         return max(dfs(self,root.left, level), dfs(self,root.right,level))
        #     else: return level
        
        # return dfs(root,0)

        ### BFS
        level = 0
        queue = deque([(1, root)]) if root else []

        while queue:
            level, node = queue.popleft()

            if node.left: queue.append((level+1,node.left))
            if node.right: queue.append((level+1,node.right))

        return level



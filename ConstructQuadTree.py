"""
Given a n * n matrix grid of 0's and 1's only. We want to 
represent the grid with a Quad-Tree.

Return the root of the Quad-Tree representing the grid.

Notice that you can assign the value of a node to True or 
False when isLeaf is False, and both are accepted in the answer.

A Quad-Tree is a tree data structure in which each internal 
node has exactly four children. Besides, each node has two attributes:

val: True if the node represents a grid of 1's or False if 
the node represents a grid of 0's.
isLeaf: True if the node is leaf node on the tree or False if 
the node has the four children.

https://leetcode.com/problems/construct-quad-tree/
"""

# Definition for a QuadTree node.
from typing import List
import numpy as np


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        
        def helper(n, r, c):
            
            allSame = True
            for i in range(n):
                for j in range(n):
                    if grid[r][c] != grid[r+i][c+j]:
                        allSame = False
                        break

            if allSame:
                return Node(grid[r][c],True, None, None, None, None)

            n = n//2
            topLeft = helper(n, r, c)
            topRight = helper(n, r, c+n)
            bottomLeft = helper(n, r+n, c)
            bottomRight = helper(n, r+n, c+n)

            return Node(1, False, topLeft, topRight, bottomLeft, bottomRight)
        
        return helper(len(grid), 0, 0)


sth = Solution()
print(sth.construct([[1, 1, 1, 1, 0, 0, 0, 0],[1, 1, 1, 1, 0, 0, 0, 0],[1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 0, 0, 0, 0],[1, 1, 1, 1, 0, 0, 0, 0],[1, 1, 1, 1, 0, 0, 0, 0],[1, 1, 1, 1, 0, 0, 0, 0]]))
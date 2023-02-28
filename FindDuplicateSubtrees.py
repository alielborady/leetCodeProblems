"""
Given the root of a binary tree, return all duplicate subtrees.

For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with the same node values.

https://leetcode.com/problems/find-duplicate-subtrees/
"""
from typing import Optional, List
from collections import defaultdict

### Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        myDict = {}
        ans = []
        walahaga = []

        def helper(root, mylist):
            if root is None: return [None]
            tempList = [i for i in mylist]
            tempList.append(root.val)
            tempList.extend(helper(root.left, mylist))
            tempList.extend(helper(root.right, mylist))

            if tuple(tempList) in myDict:
                if myDict[tuple(tempList)]==2 :
                    return tempList
                myDict[tuple(tempList)] = 2
                ans.append(root)
                walahaga.append(tempList)
            else:
                myDict[tuple(tempList)] = 1

            # myDict[tuple(tempList)] +=1
            return tempList


        helper(root,[])
        # print(walahaga)
        return ans

sth = Solution()
# print([i.val for i in sth.findDuplicateSubtrees(TreeNode(val=1, left=TreeNode(2, left=TreeNode(val=4)), right=TreeNode(val=3, left=TreeNode(val=2, left=TreeNode(val=4)), right=TreeNode(val=4))))])
print([i.val for i in sth.findDuplicateSubtrees(TreeNode(val=0, left=TreeNode(val=0, left=TreeNode(val=0)), right=TreeNode(val=0, right=TreeNode(val=0, right=TreeNode(val=0)))))])
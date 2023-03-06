"""
Given an array arr of positive integers sorted in a strictly increasing 
order, and an integer k.

Return the kth positive integer that is missing from this array.

https://leetcode.com/problems/kth-missing-positive-number/
"""


from typing import List

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:


        ans = []
        arr = set(arr)
        
        i = 1
        while len(ans) < k:

            if i not in arr:
                ans.append(i)
                
            i += 1
        return ans[-1]

sth = Solution()
print(sth.findKthPositive([2,3,4,7,11], 5))
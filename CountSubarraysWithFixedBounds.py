"""
You are given an integer array nums and two integers minK and maxK.

A fixed-bound subarray of nums is a subarray that satisfies the following conditions:

The minimum value in the subarray is equal to minK.
The maximum value in the subarray is equal to maxK.
Return the number of fixed-bound subarrays.

A subarray is a contiguous part of an array.


Example 1:

Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
Output: 2
Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].

https://leetcode.com/problems/count-subarrays-with-fixed-bounds/
"""

from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        
        bad = mini = maxi = -1

        res = 0

        for i, n in enumerate(nums):
            if not minK<=n<=maxK :
                bad = i
            if n == minK:
                mini = i
            if n == maxK:
                maxi = i
            
            start = min(mini, maxi)

            if start>bad:
                res += start - bad

        return res


sth = Solution()
print(sth.countSubarrays([1,3,5,2,7,5], 1, 5))
"""
Given an unsorted array of integers nums, return 
the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set(nums)
        longest = 0

        for n in nums:
            if (n-1) not in numSet:
                length = 1
                while(n+length) in numSet:
                    length+= 1
                    # print(length)
                longest = max(longest, length)
        return longest



sth = Solution()
print(sth.longestConsecutive([100,4,200,1,3,2]))
print(sth.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
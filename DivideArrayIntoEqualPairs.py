"""
You are given an integer array nums consisting of 2 * n integers.

You need to divide nums into n pairs such that:

Each element belongs to exactly one pair.
The elements present in a pair are equal.
Return true if nums can be divided into n pairs, otherwise return false.

"""

from typing import List
from collections import Counter

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        
        # for i in list(dict.fromkeys([nums.count(x) for x in nums])):
        #     if i%2 != 0 : 
        #         return False
        # return True

        return all([(x%2 == 0 ) for x in list(Counter(nums).values())])
        

sth = Solution()
print(sth.divideArray([15,1,4,8,12,11,4,10,4,10,10,15,20,7]))
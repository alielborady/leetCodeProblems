"""

Given an integer array nums, return true if any value appears at least 
twice in the array, and return false if every element is distinct.

"""

from typing import List
from collections import Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ### too slow
        # return False if (max([nums.count(x) for x in nums]) == 1) else True
        
        return False if (max(list(Counter(nums).values())) == 1) else True
        


sth = Solution()
print(sth.containsDuplicate([1,2,3,1]))
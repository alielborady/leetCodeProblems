"""
Given an integer array nums and an integer k, return the k most 
frequent elements. You may return the answer in any order.

"""

from collections import defaultdict
from typing import List


class Solution:
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myHash = defaultdict(int)
        for i in nums:
            myHash[i] += 1

        myHash = sorted(myHash.items(), key=lambda x:x[1], reverse=True)
        return [x[0] for x in myHash[:k]]



sth = Solution()
print(sth.topKFrequent([1,1,1,2,2,3], 2))
print(sth.topKFrequent([4,1,-1,2,-1,2,3], 2))
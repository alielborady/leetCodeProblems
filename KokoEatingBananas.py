"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. 
The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile 
of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats 
all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

https://leetcode.com/problems/koko-eating-bananas/
"""

from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        if len(piles) == 1:
            return 1 if h>piles[0] else 2
        
        k = right = max(piles)
        left = 1
        tempH=  0
        
        while left <= right:
            
            tempH = 0
            mid = (left + right) //2
            for i in piles:
                tempH += math.ceil(i/mid)
            if tempH <= h:
                k = min(mid, k)
                right = mid -1
            else:
                left = mid +1

        return k
        
x = [332484035,524908576,855865114,632922376,222257295,690155293,112677673,679580077,337406589,290818316,877337160,901728858,679284947,688210097,692137887,718203285,629455728,941802184]

sth = Solution()
print(sth.minEatingSpeed([3,6,7,11],8))
print(sth.minEatingSpeed([30,11,23,4,20],5))
print(sth.minEatingSpeed([30,11,23,4,20],6))
print(sth.minEatingSpeed(x,823855818))
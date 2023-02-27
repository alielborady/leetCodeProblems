"""
Given two non-negative integers low and high. 
Return the count of odd numbers between low and high (inclusive).
"""
import math


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low%2==0:
            if high%2==0:
                ## both even
                return int((high-low)/2)
        elif high%2 != 0:
                ## both odd
                return int(((high-low)/2)+1)
        return int(math.ceil((high-low)/2))
        


sth = Solution()
print(sth.countOdds(21,22))
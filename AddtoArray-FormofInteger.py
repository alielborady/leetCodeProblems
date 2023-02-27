"""
The array-form of an integer num is an array representing 
its digits in left to right order.

For example, for num = 1321, the array form is [1,3,2,1].
Given num, the array-form of an integer, and an integer k, 
return the array-form of the integer num + k.

https://leetcode.com/problems/add-to-array-form-of-integer/
"""

from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:

        return [int(x) for x in [*str(int("".join(str(e) for e in num)) + k)]]


sth = Solution()
print(sth.addToArrayForm([1,2,0,0],34))
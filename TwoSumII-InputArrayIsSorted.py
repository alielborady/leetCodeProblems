"""
Given a 1-indexed array of integers numbers that is already sorted
 in non-decreasing order, find two numbers such that they add up 
 to a specific target number. Let these two numbers be numbers[index1] 
 and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by 
one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You 
may not use the same element twice.

Your solution must use only constant extra space.

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
"""

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ### O(n^2)
        # for i in range(len(numbers)):
        #     for j in range(len(numbers)):
        #         if i == j:
        #             continue
        #         if numbers[i] + numbers[j] == target:
        #             return [min(i,j)+1,max(i,j)+1]

        ### correct but too much space complexity
        # myDict ={}
        # for index,i in enumerate(numbers):
        #     myDict[i] = index
        # numbers = set(numbers)

        # for x in numbers:
        #     print(x)
        #     if (9-x) in numbers:
        #         return [myDict[min(x,9-x)]+1,myDict[max(x,9-x)]+1]
        

        i,fin = 0,len(numbers) -1
        while i<fin:
            if (numbers[i] + numbers[fin]) < target:
                i +=1
            elif (numbers[i] + numbers[fin]) > target:
                fin -= 1
            else :
                return [i+1,fin+1]


sth = Solution()
print(sth.twoSum([2,7,11,15],9))
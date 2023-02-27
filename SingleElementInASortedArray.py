"""
You are given a sorted array consisting of only integers 
where every element appears exactly twice, except for one 
element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.
"""

from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
    
        while len(nums) > 1:
            mid = len(nums) //2

            if len(nums[:mid]) % 2 == 0:
                if nums[mid] == nums[mid+1]:
                    nums = nums[mid+2:]
                elif nums[mid] == nums[mid-1]:
                    nums = nums[:mid-1]
                else:
                    return nums[mid]
            else:
                if nums[mid] == nums[mid+1]:
                    nums = nums[:mid]
                elif nums[mid] == nums[mid-1]:
                    nums = nums[mid+1:]
                else:
                    return nums[mid]

        return nums[0]




sth = Solution()
print(sth.singleNonDuplicate([1,1,2,3,3,4,4,8,8]))
print(sth.singleNonDuplicate([3,3,7,7,10,11,11]))
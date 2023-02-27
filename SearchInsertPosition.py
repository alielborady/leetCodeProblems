"""
Given a sorted array of distinct integers and a target value, 
return the index if the target is found. If not, return the 
index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        leftCursor = 0
        rightCursor = len(nums) -1

        if len(nums) == 0:
            return 0
        if nums[-1] < target:
            return len(nums)
        if nums[0] >= target:
            return 0

        while leftCursor <= rightCursor:
            mid = (leftCursor + rightCursor) //2
            if nums[mid] == target:
                return mid
            elif (nums[mid] < target):
                leftCursor = mid + 1
                if (nums[mid + 1] >= target):
                    return mid+1
            else:
                rightCursor = mid - 1    
                if (nums[mid - 1] < target):
                    return mid

        ### same approach but with improvements
        # low = 0
        # high = len(nums) - 1

        # while low <= high:
        #     mid = (low + high) // 2
        #     if nums[mid] < target:
        #         low = mid + 1
        #     else:
        #         high = mid - 1
        # return low
                    


sth = Solution()
# print(sth.searchInsert([1,3,5,6], 7))
print(sth.searchInsert([3,4,5,6,7,8], 6))
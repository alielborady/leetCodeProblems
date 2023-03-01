"""
Given an array of integers nums, sort the array in ascending 
order and return it.

You must solve the problem without using any built-in functions in 
O(nlog(n)) time complexity and with the smallest space complexity possible.

https://leetcode.com/problems/sort-an-array/
"""

import random
from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        ### Quick Sort
        # def quickSort(nums):
            
        #     if len(nums) <= 1:
        #         return nums

        #     pivot = nums[0]
        #     smaller = []
        #     bigger = []
        #     for i in nums[1:]:
        #         if i <= pivot:
        #             smaller.append(i)

        #         else:
        #             bigger.append(i)



        #     return quickSort(smaller) + [pivot] + quickSort(bigger)

        # return quickSort(nums)

        ### Merge Sort
        def mergeSort(nums):

            if len(nums) == 1:
                return nums
            
            mid = len(nums) //2
            left = mergeSort(nums[:mid])
            right = mergeSort(nums[mid:])

            return merge(left, right) 
            
        def merge(left, right):

            i=j=0

            merged = []

            while i < len(left) and j < len(right):

                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1

            merged += left[i:]    
            merged += right[j:]    
            return merged

            
        return mergeSort(nums)
    



sth = Solution()
# print(sth.sortArray([5,2,3,1]))
# print(sth.sortArray([5,1,1,2,0,0]))
print(sth.sortArray([-1,2,-8,-10]))

"""

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ### Time complexity of O(n^2)
        # newNums = [1] * len(nums)
        # for i, e in enumerate(nums):
        #     for j, e1 in enumerate(nums):
        #         if i ==j :
        #             continue
        #         newNums[i] *= nums[j]
        # return newNums

        productAsc = [1] * len(nums)
        productDesc = [1] * len(nums)

        carryOn = 1
        for i in range(len(nums)):
            carryOn *= nums[i]
            productAsc[i] = carryOn

        carryOn = 1
        for i in range(len(nums)-1, -1, -1):
            carryOn *= nums[i]
            productDesc[i] = carryOn
        
        # print(productDesc)
        # print(productAsc)

        for i, elem in enumerate(nums):
            if i == 0:
                nums[i] = productDesc[i+1]
            elif i == (len(nums)-1):
                nums[i] = productAsc[i-1]
            else:
                nums[i] = productDesc[i+1]*productAsc[i-1]
        return nums




sth = Solution()
print(sth.productExceptSelf([-1,1,0,-3,3]))
print(sth.productExceptSelf([1,2,3,4]))

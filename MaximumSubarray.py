"""
Given an integer array nums, find the 
subarray with the largest sum, and return its sum.

"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ### wrong solution
        # return sum([x for x in nums if x > 0])
        
        ### O(n^3) time complexity
        # newNums = []
        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):
        #         newNums.append(nums[i:j+1])

        # return max([sum(x) for x in newNums])

        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        ### failed a few tests
        # sums = [0]
        # for i in nums:
        #     sums.append(sums[-1]+i)

        # maxEnd = sums[-1]
        # res = False
        # for i in range((len(sums) -2) , -1, -1):
        #     maxEnd = max(maxEnd, sums[i+1])
        #     res = max(res or maxEnd - sums[i], maxEnd-sums[i])

        # return res

        maxSub = nums[0]
        curSum = 0

        for i in nums:
            if curSum < 0:
                curSum = 0
            curSum += i
            maxSub = max(curSum, maxSub)
        return maxSub

sth = Solution()
print(sth.maxSubArray([-1,0]))
print(sth.maxSubArray([5,4,-1,7,8]))
print(sth.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
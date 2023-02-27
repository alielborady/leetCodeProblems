"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

https://leetcode.com/problems/two-sum/

"""

from typing import List


class TwoSum:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # for index, i in enumerate(nums):

        #     for index2, i2 in enumerate(nums):

        #         if ((i+i2) == target) & (index != index2):
        #             return[index, index2]

        #########################################################
                
        # for index, i in enumerate(nums):
        #     try:
        #         if nums.index(target-i) != index:
        #             return[index, nums.index(target-i)]
        #     except ValueError:
        #         pass

        ##########################################################

        myDict = {}
        for index, i in enumerate(nums):
            if i in myDict:
                myDict[i] = [myDict[i],index]
            else:
                myDict[i] = index
                
        for index, i in enumerate(nums):
            try:
                if type(myDict[target-i]) == int:
                    if (myDict[target-i] != index):
                        return [myDict[target-i],index]
                else:
                    return myDict[target-i]
            except KeyError:
                pass
        
myObj = TwoSum()
print(myObj.twoSum([3,3],6))
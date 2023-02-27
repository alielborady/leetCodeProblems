"""
A conveyor belt has packages that must be shipped from 
one port to another within days days.

The ith package on the conveyor belt has a weight of 
weights[i]. Each day, we load the ship with packages on 
the conveyor belt (in the order given by weights). We 
may not load more weight than the maximum weight capacity 
of the ship.

Return the least weight capacity of the ship that will 
result in all the packages on the conveyor belt being 
shipped within days days.

Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
Output: 15
Explanation: A ship capacity of 15 is the minimum to ship 
all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10

Note that the cargo must be shipped in the order given, so 
using a ship of capacity 14 and splitting the packages into 
parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.

https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
"""


from typing import List

from traitlets import Bool


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        ### time complexity O(nlogn) space O(n)
        # currentCap = max(weights)
        
        # def loop(weights, daily, currentCap):

        #     temp = []
        #     sum = 0

        #     for i in weights:

        #         if not (sum + i > currentCap):
        #             sum += i
        #             temp.append(i)

        #         else:
        #             daily.append(temp)
        #             sum = i
        #             temp = [i]
        #     daily.append(temp)

        # # print(daily)
        
        # while True:

        #     daily = []
        #     loop(weights, daily, currentCap)
            
        #     if len(daily) > days:
        #         currentCap += 1
        #     else:     
        #         break


        # return currentCap

        def helper(weights, capacity, days) -> Bool:

            currentCap = 0
            for i in weights:
                if i > capacity:
                    return False

                if currentCap + i > capacity:
                    days -= 1
                    currentCap = 0
                currentCap += i

            return days > 0

        left, right = max(weights), sum(weights)
        while left < right:

            mid = (left + right) // 2
            
            if helper(weights, mid, days):
                right = mid
            else:
                left = mid + 1

        return left

sth = Solution()
print(sth.shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5))
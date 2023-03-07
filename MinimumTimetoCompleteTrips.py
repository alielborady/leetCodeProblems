
"""
You are given an array time where time[i] denotes the time taken by the ith bus to complete one trip.

Each bus can make multiple trips successively; that is, the next trip can start immediately after 
completing the current trip. Also, each bus operates independently; that is, the trips of one bus 
do not influence the trips of any other bus.

You are also given an integer totalTrips, which denotes the number of trips all buses should make 
in total. Return the minimum time required for all buses to complete at least totalTrips trips.

https://leetcode.com/problems/minimum-time-to-complete-trips/
"""

from typing import List

class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:

        ### brute force
        if totalTrips == 1:
            return min(time)
        
        # sums = [0]*len(time)
        # d = 0
        # x = 0

        # while x <= totalTrips:
        #     for i,item in enumerate(time):

        #         net =  (int(d /item) - sums[i])
        #         sums[i] += net
        #         x += net

        #     if x >= totalTrips:
        #         return d
            
        #     d+=1


        ### binary search
        totTrips = 0
        mini = 1
        max = totalTrips * min(time)

        while mini < max:
            mid = (mini + max) // 2

            for i in time:
                totTrips += mid // i

            if totTrips >= totalTrips:
                max = mid
            else:
                mini = mid +1
            
            totTrips = 0

        return mini
    



    
sth = Solution()
print(sth.minimumTime([1,2,3], 5))
print(sth.minimumTime([5,10,10], 9))
print(sth.minimumTime([2], 1))
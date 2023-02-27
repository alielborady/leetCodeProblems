"""
Suppose LeetCode will start its IPO soon. In order to sell a good 
price of its shares to Venture Capital, LeetCode would like to 
work on some projects to increase its capital before the IPO. Since
it has limited resources, it can only finish at most k distinct 
projects before the IPO. Help LeetCode design the best way to 
maximize its total capital after finishing at most k distinct projects.

You are given n projects where the ith project has a pure profit 
profits[i] and a minimum capital of capital[i] is needed to start it.

Initially, you have w capital. When you finish a project, you 
will obtain its pure profit and the profit will be added to your
total capital.

Pick a list of at most k distinct projects from given projects 
to maximize your final capital, and return the final maximized capital.

The answer is guaranteed to fit in a 32-bit signed integer."""

from typing import List
import heapq



class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        ### brute force. Time complexity O(k*n^2), space complexity O(n)
        # def helper(w: int, profits: List[int], capital: List[int]) -> int:
        #     currentProf = 0
        #     ind = None
        #     for i in range(len(capital)):
        #         if (capital[i] <= w) and (profits[i] > currentProf):
        #             currentProf += profits[i]
        #             ind = i
        #     return ind
        
        # for i in range(k):
        #     ind = helper(w, profits, capital)
        #     w += profits[ind]
        #     profits.pop(ind)
        #     capital.pop(ind)
        
        # return w

        projects = [(capital[i], profits[i]) for i in range(len(profits))]
        
        heapq.heapify(projects)
        available = []

        for i in range(k):
            while projects and projects[0][0] <=w:
                heapq.heappush(available,-projects[0][1])
                heapq.heappop(projects)
            if not available:
                break
            w -= heapq.heappop(available)

        return w

sth = Solution()
print(sth.findMaximizedCapital(2,0,[1,2,3],[0,1,1]))
print(sth.findMaximizedCapital(3,0,[1,2,3],[0,1,2]))
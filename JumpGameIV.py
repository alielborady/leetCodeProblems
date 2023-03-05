"""
Given an array of integers arr, you are initially positioned at the first index of the array.

In one step you can jump from index i to index:

i + 1 where: i + 1 < arr.length.
i - 1 where: i - 1 >= 0.
j where: arr[i] == arr[j] and i != j.
Return the minimum number of steps to reach the last index of the array.

Notice that you can not jump outside of the array at any time.

https://leetcode.com/problems/jump-game-iv/
"""

from typing import List, DefaultDict


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        myDict = DefaultDict(list)

        if len(arr) == 1:
            return 0

        for i, n in enumerate(arr):
            myDict[n].append(i)


        ### not optimal
        # steps = 0
        # index = 0
        # while index < (len(arr)-1):
        #     forward = -1
        #     backward = -1
        #     jump = -1
            
        #     if myDict[arr[index]][-1] > index:
        #         jump = myDict[arr[index]][-1]

        #     try:
        #         if myDict[arr[index-1]][-1] > index and (index!= 0):
        #             backward = myDict[arr[index-1]][-1] 
        #     except IndexError:
        #         pass

        #     try:
        #         if myDict[arr[index+1]][-1] > index :
        #             forward = myDict[arr[index+1]][-1]
        #     except IndexError:
        #         pass

        #     if jump>=forward and jump>=backward:
        #         index = jump
        #     elif forward> backward:
        #         index += 1
        #     else:
        #         index -= 1
            
        #     steps +=1

        # return steps

        queue = []
        steps = 0
        visited = set()

        queue.append(0)
        visited.add(0)

        while queue:
            queue_len = len(queue)
            for _ in range(queue_len):
                index = queue.pop(0)

                if index == len(arr) - 1:
                    return steps

                for adj_index in myDict.get(arr[index]):
                    if adj_index not in visited:
                        queue.append(adj_index)
                        visited.add(adj_index)

                myDict[arr[index]] = []
                if (index - 1 > -1) and (index-1) not in visited:
                    queue.append(index-1)
                    visited.add(index-1)

                if (index + 1 < len(arr)) and (index+1) not in visited:
                    queue.append(index+1)
                    visited.add(index+1)

            steps += 1

        return -1




sth = Solution()
# print(sth.minJumps([100,-23,-23,404,100,23,23,23,3,404]))
# print(sth.minJumps([7,6,9,6,9,6,9,7]))
print(sth.minJumps([7,7,2,1,7,7,7,3,4,1]))
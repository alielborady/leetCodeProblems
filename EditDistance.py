"""
You are given an array nums of n positive integers.

You can perform two types of operations on any element of the array 
any number of times:

If the element is even, divide it by 2.
For example, if the array is [1,2,3,4], then you can do this operation 
on the last element, and the array will be [1,2,3,2].
If the element is odd, multiply it by 2.
For example, if the array is [1,2,3,4], then you can do this operation 
on the first element, and the array will be [2,2,3,4].
The deviation of the array is the maximum difference between any two 
elements in the array.

Return the minimum deviation the array can have after performing some 
number of operations.
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # if word1 == word2 :
        #     return 0 
        # if word1 == "":
        #     return len(word2)        
        # if word2 == "":
        #     return len(word1)

        cach = [[float("inf")] * (len(word2) +1) for i in range(len(word1) + 1)]

        for j in range(len(word1) + 1):
            cach[j][-1] = len(word1) - j

        for i in range(len(word2)):
            cach[-1][i] = len(word2) - i

        for i in range(len(word1)-1,-1,-1):
            for j in range(len(word2)-1, -1, -1):

                if word1[i] == word2[j]:
                    cach[i][j] = cach[i+1][j+1]

                else:
                    cach[i][j] = min(cach[i+1][j+1],cach[i+1][j],cach[i][j+1]) +1

            print(cach)
        return cach[0][0]

sth = Solution()
print(sth.minDistance("horse","ros"))
# print(sth.minDistance("","asdf"))
"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.
"""

from collections import Counter, defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        ### time: O(n^2*m), space O(n*m)
        # grouped = []

        # for i in strs:
        #     tempGrouped = []
        #     iCounter = Counter(i)
        #     for j in strs:
        #         if len(i) != len(j):
        #             continue

        #         jCounter = Counter(j)

        #         if  iCounter == jCounter :
        #             tempGrouped.append(j)
            
        #     if tempGrouped not in grouped:
        #         grouped.append(tempGrouped)
        
        # return grouped

        ### right solution but too long
        # myDict = {}
        # for i in strs:
        #     if tuple(sorted([*i])) in myDict:
        #         myDict[tuple(sorted([*i]))] = myDict[tuple(sorted([*i]))] + [i]
        #     else:
        #         myDict[tuple(sorted([*i]))] = [i]
        
        # print(myDict)

        myDict = defaultdict(list)
        for i in strs:
            tempList = [0]*26   # a ... z 

            for lett in i :
                tempList[ord(lett) - ord("a")] += 1
            
            myDict[tuple(tempList)].append(i)
        
        return myDict.values()
            

sth = Solution()
print(sth.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))


"""
Given two strings needle and haystack, return the index of the 
first occurrence of needle in haystack, or -1 if needle is not 
part of haystack.


https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ### easy direct solution
        # return haystack.find(needle)

        if len(needle) == 0 :
            return 0
        
        # haystack += " "
        # j = 0
        for i in range(len(haystack) - len(needle) + 1):
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    break
                if j == len(needle) -1:
                    return i
        return -1
sth = Solution()
print(sth.strStr("sadbutnotsad", "sad"))
print(sth.strStr("leetcode", "leeto"))
print(sth.strStr("a", "a"))
print(sth.strStr("mississippi", "issip"))
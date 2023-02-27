"""

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.


"""

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(t) != len(s):
            return False

        # sCounter = Counter(s)
        # tCounter = Counter(t)
        # return sCounter == tCounter

        sCounter = {}
        for letter in s:
            if letter in sCounter:
                sCounter[letter] += 1
            else:
                sCounter[letter] = 1

        for letter in t:
            if letter not in sCounter:
                return False
            elif sCounter[letter] == 0:
                return False
            else:
                sCounter[letter] -= 1
        return True


        
sth = Solution()
print(sth.isAnagram("anagram","aaarnmg"))
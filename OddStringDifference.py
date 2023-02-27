"""
You are given an array of equal-length strings words. Assume that the length of each string is n.

Each string words[i] can be converted into a difference integer array difference[i] of length n - 1 
where difference[i][j] = words[i][j+1] - words[i][j] where 0 <= j <= n - 2. Note that the difference 
between two letters is the difference between their positions in the alphabet 
i.e. the position of 'a' is 0, 'b' is 1, and 'z' is 25.

For example, for the string "acb", the difference integer array is [2 - 0, 1 - 2] = [2, -1].
All the strings in words have the same difference integer array, except one. You should find that string.

Return the string in words that has different difference integer array.

Input: words = ["adc","wzy","abc"]
Output: "abc"
Explanation: 
- The difference integer array of "adc" is [3 - 0, 2 - 3] = [3, -1].
- The difference integer array of "wzy" is [25 - 22, 24 - 25]= [3, -1].
- The difference integer array of "abc" is [1 - 0, 2 - 1] = [1, 1]. 
The odd array out is [1, 1], so we return the corresponding string, "abc".
"""

from typing import List
from collections import Counter

class OddStringDifference:

    alphabets = {'a': 0,'b': 1,'c': 2,'d': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}

    def oddString(self, words: List[str]) -> str:
        fullList=[]
        for item in words:
            tempList = []
            for i in range(1,(len([*item]))):
                # print([*item][i])
                tempList.append(self.alphabets[[*item][i]]-self.alphabets[[*item][i-1]])
            fullList.append(tempList)

        return words[fullList.index([i for i in fullList if fullList.count(i) ==1][0])]


myClass = OddStringDifference()
print(myClass.oddString(["adc","wzy","abc"]))
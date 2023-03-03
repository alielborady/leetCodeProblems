"""
Given an array of characters chars, compress it using the following 
algorithm:

Begin with an empty string s. For each group of consecutive repeating 
characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, 
be stored in the input character array chars. Note that group lengths 
that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length 
of the array.

You must write an algorithm that uses only constant extra space.

https://leetcode.com/problems/string-compression/
"""

from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        if n == 1:
            return 1
        
        i = 0
        j = 0
        
        while i < n:
            count = 1
            while i < n - 1 and chars[i] == chars[i+1]:
                count += 1
                i += 1
            
            chars[j] = chars[i]
            j += 1
            
            if count > 1:
                for c in str(count):
                    chars[j] = c
                    j += 1
            
            i += 1
        
        print(chars)
        return j


sth = Solution()
print(sth.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))
# print(sth.compress(["a","a","b","b","c","c","c"]))
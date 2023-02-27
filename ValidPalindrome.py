"""

A phrase is a palindrome if, after converting all uppercase letters into lowercase 
letters and removing all non-alphanumeric characters, it reads the same forward 
and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        filtered = ""
        print(filtered)
        for l in s.lower():
            if (ord(l) >= 48 and ord(l) <58) or (ord(l) >= 97 and ord(l) <123):
                filtered += l
        if len(filtered) < 2:
            return True 
        for i in range(int(len(filtered)/2)):
            # last = -1 - i
            if not (filtered[i] == filtered[-1-i]):
                return False
        return True

sth = Solution()
# print(sth.isPalindrome("A man, a plan, a canal: Panama"))
print(sth.isPalindrome("0z;z   ; 0"))
"""
Given two binary strings a and b, return their sum as a binary string.

"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ### returns decimal not binary
        # total = 0
        # for i,l in enumerate(a):
        #     if l=="1":
        #         total += (2^i)
        # for i,l in enumerate(b):
        #     if l=="1":
        #         total += (2^i)
        # return str(total)



        a = a.zfill(max(len(a),len(b)))
        b = b.zfill(len(a))

        result = ''
        carry = 0

        for i in range(len(a)-1,-1, -1):
            match (int(a[i]) + int(b[i]) + carry):
                case 3:
                    result =  "1" + result
                    carry = 1
                case 2:
                    result =  "0" + result
                    carry = 1
                case 1:
                    result =  "1" + result
                    carry = 0
                case 0:
                    result =  "0" + result
                    carry = 0
        if carry==1:
            result = "1" + result

        return result

        ## correct using functions
        # return bin(int(a,2) + int(b,2))[2:]

        

sth = Solution()
print(sth.addBinary("11","1"))
print(sth.addBinary("1010","1011"))
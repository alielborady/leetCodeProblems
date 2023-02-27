class Solution(object):
    
    myDict = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        }


    def isDesc(self, list):
        
        values = []

        for count,item in enumerate(list):

            if count == (len(list)-1):
                values.append(1)
            elif self.myDict[item] >= self.myDict[list[count+1]]:
                values.append(1)
            elif self.myDict[item] < self.myDict[list[count+1]]:
                values.append(0)

        return values


    def romanToInt(self,s):

        seperatedList = [*s]

        listOfOrders = self.isDesc(seperatedList)

        accumulate = 0
        for count, item in enumerate(seperatedList):
            
            if listOfOrders[count] == 1 :
                accumulate += self.myDict[item]
            else :
                accumulate -= self.myDict[item]

        return accumulate




solution = Solution()
output = solution.romanToInt("III")

print(output)
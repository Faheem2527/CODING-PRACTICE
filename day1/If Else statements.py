#Input: n = 4, m = 8
#utput: lesser
#Explanation: 4 < 8 so print 'lesser'.
#Input: n = 8, m = 8
#Output: equal
#Explanation: 8 = 8 so print 'equal'.
#Input: n = 8, m = 4
#Output: greater
#Explanation: 8 > 4 so print 'greater'.


class Solution:
    def compareNM(self, n : int, m : int) -> str:
        if n<m:
            return "lesser"
        elif n==m:
            return "equal"
        else:
            return "greater"
            
        

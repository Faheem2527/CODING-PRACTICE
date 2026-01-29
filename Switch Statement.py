#Given an integer choice denoting the choice of the user and a list containing the single value R or two values L and B depending on the choice.
#If the user's choice is 1, calculate the area of the circle having the given radius(R).  
#Else if the choice is 2, calculate the area of the rectangle with the given length(L) and breadth(B).

#Note : A list arr[], containing the single value R or the two values L and B, as input parameters. Return the area of the desired geometrical figure. Use Math.PI for the value of pi.

#User function Template for python3
import math

class Solution:
    def switchCase(self, choice, arr):
        # Code here
       
        if choice==1:
            r = arr[0]
            return math.pi*r*r
        elif choice==2:
            l= arr[0]
            b= arr[1]
            return l*b

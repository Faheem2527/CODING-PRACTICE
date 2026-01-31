class Solution:
    def isPrime(self, n: int) -> str:
        if n <= 1:
            return "No"
            
  
        for i in range(2, n):
            if n % i == 0:
         
                return "No"
        
       
        return "Yes"

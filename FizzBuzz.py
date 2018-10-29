class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        rs =[]
        s3, s5, s35 = 'Fizz', 'Buzz', 'FizzBuzz'
    
        for i in range(1,n+1):
            if i%3==0 and i%5 !=0:
                rs.append(s3)
            elif i%5==0 and i%3 !=0:
                rs.append(s5)
            elif i%3==0 and i%5 ==0:
                rs.append(s35)
            
            elif i%3!=0 and i%5 !=0:
                rs.append(str(i))
        return rs
                
                
                
        
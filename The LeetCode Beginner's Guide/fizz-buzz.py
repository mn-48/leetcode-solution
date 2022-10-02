class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ls = []
        for i in range(1,n+1):
            divided_by3 = i%3 == 0
            divided_by5 = i%5 == 0
            
            if divided_by3 and divided_by5 :
                 res = "FizzBuzz"
            elif divided_by3:
                res = "Fizz"
            elif divided_by5:
                res = "Buzz"
            else:
                res = str(i)
            ls.append(res)
        return ls
            

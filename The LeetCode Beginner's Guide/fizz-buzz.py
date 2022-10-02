
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ls = []
        for i in range(1,n+1):
            res = str(i)
            if i%3==0 and i%5!=0:
                res = "Fizz"
            if i%3!=0 and i%5==0:
                res = "Buzz"
            if i%3==0 and i%5==0:
                res = "FizzBuzz"
            ls.append(res)
        return ls
            
            

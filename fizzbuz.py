class Solution(object):
    
    def fizzBuzz(self, n):
        y=[]
        for i in range(1,n+1):
            if (i%3==0 and i%5 ==0):
                y.append("Fizzbuzz")
            elif(i%3==0):
                y.append("Fizz")
            elif i%5==0:
                y.append("Buzz")
            else:
                y.append(str(i))
        return y
x=Solution()
x.fizzBuzz(3)
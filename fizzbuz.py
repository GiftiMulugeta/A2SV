class Solution(object):
    
    def fizzBuzz(self, n):
        y=[]
        for i in range(1,n+1):
            if (i%3==0 and i%5 ==0):
                y.append("fizzbuzz")
            elif(i%3==0):
                y.append("fizz")
            elif i%5==0:
                y.append("buzz")
            else:
                y.append(str(i))
        print(y)
x=Solution()
x.fizzBuzz(3)
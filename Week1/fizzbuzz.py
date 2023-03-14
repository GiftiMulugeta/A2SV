# class Solution(object):
    
#     def fizzBuzz(self, n):
#         empty_array=[]
#         for i in range(1,n+1):
#             if (i%3==0 and i%5 ==0):
#                 empty_array.append("FizzBuzz")
#             elif(i%3==0):
#                 empty_array.append("Fizz")
#             elif i%5==0:
#                 empty_array.append("Buzz")
#             else:
#                 empty_array.append(str(i))
#         return empty_array
# fizzbuzz=Solution()
# fizzbuzz.fizzBuzz(3)
lass Solution(object):
    def fizzBuzz(self, n):
        array=[]
        for i in range(1,n+1):
            if (i%3 == 0 and i%5 == 0):
                array.append("FizzBuzz")
            elif(i%5 == 0):
                array.append("Buzz")
            elif(i%3 == 0):
                array.append("Fizz")
            else:
                array.append(str(i))
        return array

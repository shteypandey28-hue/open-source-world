#write a function priunt two numbers and x should be cube and y should be square of the number and
# print result should be the subraction of cube(x) - square(y)
import math
x=int(input("Enter the number"))
def cube(num):
  num**=3
  return num
print(cube(x))
y=int(input("Enter the number"))
def square(num):
  num**=2
  return num
print(square(y))
result = cube(x) - square(y)
print("the subraction of cube - square  = " , result)
